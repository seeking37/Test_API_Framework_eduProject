#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
课程管理 - 新增/修改课程接口测试
"""

import allure
import pytest

from base.apiutil import RequestBase
from common.db_management import MysqlManager
from common.readyaml import get_testcase_yaml
from base.generateId import m_id, c_id
from common.recordlog import logs
from conf.setting import FILE_PATH


@allure.feature(next(m_id) + '课程管理')
@pytest.mark.course_management
@pytest.mark.api_single
@pytest.mark.course_save
@pytest.mark.smoke
class TestCourseSave:
    """课程新增/修改测试类"""

    @pytest.fixture(scope="class", autouse=True)
    def setup_teardown(self):
        mysql_manager = MysqlManager()
        backup_file = None
        try:
            backup_file = mysql_manager.backup_data("course")
            if not backup_file:
                logs.error("课程表备份失败！")
                return
            try:
                mysql_manager.init_data(f"{FILE_PATH['BACKUP']}/init_course.sql")
                logs.info("课程表初始化成功")
            except Exception as e:
                logs.error(f"课程表初始化失败: {str(e)}")
                return
            yield
        except Exception as e:
            logs.error(f"测试过程发生错误: {str(e)}")
        finally:
            if backup_file:
                try:
                    mysql_manager.restore_data(backup_file)
                    logs.info("数据库还原成功")
                except Exception as e:
                    logs.error(f"数据库还原失败: {str(e)}")
    @allure.story(next(c_id) + "新增课程")
    @pytest.mark.run(order=20)
    @pytest.mark.parametrize("base_info, testcase", get_testcase_yaml('./testcase/Single/CourseManagement/course_add_data.yaml'))
    def test_course_add(self, base_info, testcase):
        """
        测试新增课程接口
        """
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)

    @allure.story(next(c_id) + "修改课程")
    @pytest.mark.run(order=21)
    @pytest.mark.parametrize("base_info, testcase", get_testcase_yaml('./testcase/Single/CourseManagement/course_update_data.yaml'))
    def test_course_update(self, base_info, testcase):
        """
        测试修改课程接口
        注意：此测试依赖新增课程测试提取的course_id
        """
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)