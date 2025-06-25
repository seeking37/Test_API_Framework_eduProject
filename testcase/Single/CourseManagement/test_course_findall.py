import allure
import pytest

from common.readyaml import get_testcase_yaml
from base.apiutil import RequestBase
from base.generateId import m_id, c_id
from common.recordlog import logs


@allure.feature(next(m_id) + '课程管理')
@pytest.mark.course_management
@pytest.mark.api_single
@pytest.mark.course_query
@pytest.mark.smoke
@pytest.mark.header_auth
class TestCourseManagement:

    @allure.story(next(c_id) + "查询所有课程")
    @pytest.mark.run(order=10)
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml("./testcase/Single/CourseManagement/course_findall_data.yaml"))
    def test_course_findall(self, base_info, testcase):
        """
        测试查询所有课程接口
        验证课程列表的获取功能，包括正常查询和权限验证
        """
        allure.dynamic.title(testcase['case_name'])
        RequestBase().specification_yaml(base_info, testcase)
