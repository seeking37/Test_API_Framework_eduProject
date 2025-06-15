import allure
import pytest

from common.readyaml import get_testcase_yaml
from base.apiutil_business import RequestBase
from base.generateId import m_id, c_id


@allure.feature(next(m_id) + '用户管理')
class TestUserManager:

    @allure.story(next(c_id) + "查询用户权限（业务场景）")
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('case_info', get_testcase_yaml("./testcase/Business Scenario/user_permissions_data.yaml"))
    def test_user_permissions(self, case_info):
        allure.dynamic.title(case_info['testCase'][0]['case_name'])
        RequestBase().specification_yaml(case_info)
