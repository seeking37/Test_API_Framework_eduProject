# import allure
# import pytest
#
# from common.readyaml import get_testcase_yaml
# from base.apiutil import RequestBase
# from base.generateId import m_id, c_id
#
#
# @allure.feature(next(m_id) + '用户管理')
# class TestUserManager:
#
#     @allure.story(next(c_id) + "冻结/解冻用户")
#     @pytest.mark.run(order=1)
#     @pytest.mark.parametrize('base_info,testcase', get_testcase_yaml("./testcase/Single/UserManagement/user_login_data.yaml"))
#     def test_login(self, base_info, testcase):
#         allure.dynamic.title(testcase['case_name'])
#         RequestBase().specification_yaml(base_info, testcase)
#
#
