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
class TestCourseFindById:

    @allure.story(next(c_id) + "根据课程ID查询课程")
    @pytest.mark.run(order=11)
    @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml("./testcase/Single/CourseManagement/course_findbyid_data.yaml"))
    def test_course_findbyid(self, base_info, testcase):
        """
        测试根据课程ID查询课程接口
        验证通过课程ID获取特定课程信息的功能，包括有效ID、无效ID和权限验证
        """
        allure.dynamic.title(testcase['case_name'])
        logs.info(f"开始执行测试用例: {testcase['case_name']}")
        RequestBase().specification_yaml(base_info, testcase)
