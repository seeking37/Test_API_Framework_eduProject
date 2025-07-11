import pytest
import allure
from common.readyaml import get_testcase_yaml
from base.apiutil import RequestBase
from common.recordlog import logs
from common.connection import ConnectMysql
from conf.setting import DIR_BASE

"""
-function：每一个函数或方法都会调用
-class：每一个类调用一次，一个类中可以有多个方法
-module：每一个.py文件调用一次，该文件内又有多个function和class
-session：是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module,整个会话只会运行一次
-autouse：默认为false，不会自动执行，需要手动调用，为true可以自动执行，不需要调用
- yield：前置、后置
"""


@pytest.fixture(autouse=True)
def start_test_and_end():
    logs.info('-------------接口测试开始--------------')
    yield
    logs.info('-------------接口测试结束--------------')


@pytest.fixture(scope='session', autouse=True)
@allure.story("登录")
def system_login():
    try:
        # ！使用 pytest 命令运行时，pytest 会自动将项目根目录设置为工作目录，所以 ./data/loginName.yaml 是相对于项目根目录的路径
        # 如果需要在本py文件中运行要改目录地址为../data/loginName.yaml
        # api_info = get_testcase_yaml('./data/loginName.yaml')  # 返回数据见末尾
        api_info = get_testcase_yaml(f"{DIR_BASE}/data/loginName.yml")
        RequestBase().specification_yaml(api_info[0][0], api_info[0][1])
    except Exception as e:
        logs.error(f'登录接口出现异常，导致后续接口无法继续运行，请检查程序！，{e}')
        exit()

# 具体实现需完善更多细节
@pytest.fixture(scope='session', autouse=True)
def datadb_init():
    """
    后置处理器，比如测试之后的数据清理
    数据库可以预先预置一批本次测试的数据，在测试完成之后将这批数据清理，就不会对系统造成影响，也不会产生脏数据
    :return:
    """
    # conn = ConnectMysql()
    # yield
    # sql = "delete from sys_user where login_name='test999'"
    # conn.delete(sql)
    # allure.attach('将测试数据清空', 'fixture后置', allure.attachment_type.TEXT)

    pass

if __name__ == '__main__':
    # api_info = [
    #     [
    #         {'api_name': '用户登录', 'url': '/dar/user/login', 'method': 'post',
    #          'header': {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}},
    #         {'case_name': '用户名和密码确登录验证', 'data': {'user_name': 'test01', 'passwd': 'admin123'},
    #          'validation': [{'contains': {'error_code': 'none'}}, {'eq': {'msg': '登录成功'}}],
    #          'extract': {'token': '$.token'}}
    #     ]
    # ]
    # api_info = get_testcase_yaml('../data/loginName.yml')
    # print(api_info[0][0],"\n",api_info[0][1])
    # RequestBase().specification_yaml(api_info[0][0], api_info[0][1])
    # system_login()
    pass
