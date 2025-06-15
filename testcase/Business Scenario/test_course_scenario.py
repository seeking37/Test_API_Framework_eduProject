import allure
import pytest

from common.readyaml import get_testcase_yaml
from base.apiutil_business import RequestBase
from base.generateId import m_id, c_id
from common.db_management import MysqlManager
from conf.setting import FILE_PATH
from common.recordlog import logs
# 注意：业务场景的接口测试要调用base目录下的apiutil_business文件

@allure.feature(next(m_id) + '课程管理（业务场景）')
class TestEBusinessScenario:

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

    @allure.story(next(c_id) + '查询/添加/修改/更新课程流程')
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize('case_info', get_testcase_yaml('./testcase/Business Scenario/course_scenario.yml'))
    def test_course_scenario(self, case_info):
        allure.dynamic.title(case_info['testCase'][0]['case_name'])
        RequestBase().specification_yaml(case_info)

