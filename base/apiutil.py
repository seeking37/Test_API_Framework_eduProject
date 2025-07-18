import json
import re
from json.decoder import JSONDecodeError

import allure
import jsonpath
import requests
from requests import utils

from common.assertions import Assertions
from common.debugtalk import DebugTalk
from common.readyaml import get_testcase_yaml, ReadYamlData
from common.recordlog import logs
from common.sendrequest import SendRequest
from conf.operationConfig import OperationConfig
from conf.setting import FILE_PATH

"""
类 RequestBase 主要负责 接口自动化测试的核心流程封装，包括参数动态替换、请求发送、响应处理、数据提取、断言验证和报告生成等关键环节。
参数替换 (replace_load)：处理 ${} 动态表达式（如变量提取、函数调用），实现参数化。
请求构造与发送 (specification_yaml)：基于 YAML 数据组装请求（URL、Header、参数等），调用 SendRequest 发送请求。
响应处理 (extract_data/extract_data_list)：从响应中提取数据（支持 JSONPath 和正则），并持久化到 YAML 供后续用例使用。
断言验证(asserts.assert_result)：验证响应状态码和业务字段是否符合预期。在specification_yaml 中
报告增强 (allure_attach_response)：将关键信息附加到 Allure 报告中，提升可读性。
"""


class RequestBase:

    def __init__(self):
        self.run = SendRequest()
        self.conf = OperationConfig()
        self.read = ReadYamlData()
        self.asserts = Assertions()

    def get_host(self, base_info, test_case=None):
        """
        根据接口配置决定使用哪个host
        :param base_info: 接口基础信息
        :param test_case: 测试用例信息
        :return: 选择的host地址
        """
        # 如果测试用例中指定使用mock，则使用mock_host
        if test_case and test_case.get('use_mock', False):
            return self.conf.get_section_for_data('api_envi', 'mock_host')
        # 如果接口配置中指定使用mock，则使用mock_host
        if base_info.get('use_mock', False):
            return self.conf.get_section_for_data('api_envi', 'mock_host')
        # 否则使用真实host
        return self.conf.get_section_for_data('api_envi', 'host')

    def replace_load(self, data):
        """yaml数据替换解析"""
        str_data = data
        if not isinstance(data, str):
            str_data = json.dumps(data, ensure_ascii=False)
            # print('从yaml文件获取的原始数据：', str_data)
        for i in range(str_data.count('${')):
            if '${' in str_data and '}' in str_data:
                start_index = str_data.index('$')
                end_index = str_data.index('}', start_index)
                # 提取完整的表达式，如${get_extract_data(token)}
                ref_all_params = str_data[start_index:end_index + 1]
                # 取出yaml文件的函数名，如get_extract_data
                func_name = ref_all_params[2:ref_all_params.index("(")]
                # 取出函数里面的参数，如token
                func_params = ref_all_params[ref_all_params.index("(") + 1:ref_all_params.index(")")]
                # 传入替换的参数获取对应的值,类的反射----getattr,setattr,del....
                # getattr(object, name) 是 Python 内置函数，用于从对象 (DebugTalk()) 中动态获取名为 func_name 的方法
                extract_data = getattr(DebugTalk(), func_name)(*func_params.split(',') if func_params else "")
                # 处理返回值为列表的情况
                if extract_data and isinstance(extract_data, list):
                    extract_data = ','.join(e for e in extract_data)
                # 替换原始字符串中的表达式 如：${get_extract_data(token)}替换为 一串token值
                str_data = str_data.replace(ref_all_params, str(extract_data))
                # print('通过解析后替换的数据：', str_data)
        # 将字符串类型的str_data还原为原始数据data的类型
        # if data and isinstance(data, dict):
        #     data = json.loads(str_data)
        # else:
        #     data = str_data
        # 如果是空字典也还原为字典类型
        if isinstance(data, dict):
            data = json.loads(str_data)
        else:
            # data = str(json.loads(str_data))
            data = str_data

        return data

    def specification_yaml(self, base_info, test_case):
        """
        接口请求处理基本方法
        核心枢纽：将 YAML 中的 baseInfo 和 testCase 组合成可执行的测试步骤。
        流程控制：依次处理参数、发送请求(run_main，send_request)、提取数据、执行断言，是类的主入口方法。
        :param base_info: yaml文件里面的baseInfo
        :param test_case: yaml文件里面的testCase
        :return:
        """
        try:
            params_type = ['data', 'json', 'params']
            # 根据接口配置选择host
            url_host = self.get_host(base_info, test_case)
            test_case.pop('use_mock', None)
            base_info.pop('use_mock', None)
            api_name = base_info['api_name']
            allure.attach(api_name, f'接口名称：{api_name}', allure.attachment_type.TEXT)
            url = url_host + base_info['url']
            allure.attach(api_name, f'接口地址：{url}', allure.attachment_type.TEXT)
            method = base_info['method']
            allure.attach(api_name, f'请求方法：{method}', allure.attachment_type.TEXT)
            # 处理请求头：支持testCase级别完全覆盖baseInfo的header
            if 'header' in test_case:
                # 如果testCase中有header，则完全使用testCase的header
                header = self.replace_load(test_case.pop('header'))
            elif 'header' in base_info:
                # 否则使用baseInfo中的header
                header = self.replace_load(base_info['header'])
            else:
                header = {}
            
            allure.attach(api_name, f'请求头：{header}', allure.attachment_type.TEXT)
            # 处理cookie
            cookie = None
            if base_info.get('cookies') is not None:
                cookie = eval(self.replace_load(base_info['cookies']))
            # pop：字典 删除case_name键值对并返回case_name的值
            case_name = test_case.pop('case_name')
            allure.attach(api_name, f'测试用例名称：{case_name}', allure.attachment_type.TEXT)
            # 处理断言
            val = self.replace_load(test_case.get('validation'))
            # replace_load将validation从列表转换成了字符串，所以可以使用replace函数
            test_case['validation'] = val
            # validation = eval(test_case.pop('validation'))  为了断言bool值，json和python的bool大小写不一样，改成下面代码
            # validation = eval((test_case.pop('validation')).replace('true', 'True').replace('false', 'False'))
            val = test_case.get('validation')
            test_case.pop('validation')
            # 处理参数提取
            extract = test_case.pop('extract', None)
            extract_list = test_case.pop('extract_list', None)
            # 处理接口的请求参数
            for key, value in test_case.items():
                if key in params_type:
                    test_case[key] = self.replace_load(value)

            # 处理文件上传接口
            file, files = test_case.pop('files', None), None
            if file is not None:
                for fk, fv in file.items():
                    allure.attach(json.dumps(file), '导入文件')
                    files = {fk: open(fv, mode='rb')}
            # run_main ：核心是发送请求。  传入的参数包含有base_info，和test_case中的'data:{xxx}'
            res = self.run.run_main(name=api_name, url=url, case_name=case_name, header=header, method=method,
                                    file=files, cookies=cookie, **test_case)
            if extract is not None:  # extract : {'token': '$.token'}
                self.extract_data(extract, res)
            if extract_list is not None:
                self.extract_data_list(extract_list, res.text)

            status_code = res.status_code
            # 无论 Content-Type 是什么，直接尝试解析 JSON
            try:
                res_json = res.json()  # 强制尝试解析响应内容
                # 附加 JSON 响应到报告
                allure.attach(
                    self.allure_attach_response(res_json),
                    '接口响应信息',
                    allure.attachment_type.TEXT
                )
                validation = eval((self.replace_load(val)).replace('true', 'True').replace('false', 'False'))
                # 处理断言（包含 JSON 数据和状态码）
                self.asserts.assert_result(validation, res_json, status_code)

            except (JSONDecodeError, ValueError) as e:  # 捕获 JSON 解析异常
                # 记录错误日志（明确提示内容非JSON）
                logs.error(f'响应非JSON格式，解析失败: {e}，原始内容: {res.text[:200]}...')

                # 附加原始响应内容到报告（确保非JSON也能展示）
                allure.attach(
                    res.text if res.text else res.content.decode('utf-8', errors='ignore'),
                    '接口响应原始内容',
                    allure.attachment_type.TEXT
                )

                # 仅验证状态码（根据业务需求，可扩展其他非JSON断言。比如验证码接口返回的是图片）
                self.asserts.assert_result(
                    validation,
                    {'status_code': status_code},  # 构造仅包含状态码的模拟数据
                    status_code
                )

        except Exception as e:
            raise e

    @classmethod
    def allure_attach_response(cls, response):
        # 格式化响应数据为易读的 JSON，提升 Allure 报告的可读性。
        if isinstance(response, dict):
            allure_response = json.dumps(response, ensure_ascii=False, indent=4)
        else:
            allure_response = response
        return allure_response

    def extract_data(self, testcase_extract, response):
        """
        提取接口返回值，支持响应体JSONPath/正则表达式提取和cookie提取
        :param  testcase_extract = {
            'token': '$..access_token',           # JSONPath提取响应体
            'message': '$.message',               # JSONPath提取响应体  
            'user_id': '"user_id":"(.+?)"',       # 正则表达式提取响应体
            'session_id': 'cookies:JSESSIONID',   # 提取指定名称的cookie
            'all_cookies': 'cookies:*'            # 提取所有cookies（字典形式）
        }
        :param response: requests.Response 对象
        """
        try:
            extracted = {}
            response_text = response.text

            for key, expr in testcase_extract.items():
                expr = expr.strip()
                value = None

                # Cookie提取
                if expr.startswith('cookies:'):
                    cookie_name = expr.split(':', 1)[1].strip()
                    if cookie_name == '*':
                        # 提取所有cookies，手动构建字典避免同名冲突
                        cookie_dict = {}
                        for cookie in response.cookies:
                            # 如果存在同名cookie，使用域名作为后缀区分
                            key = cookie.name
                            if key in cookie_dict:
                                key = f"{cookie.name}_{cookie.domain}"
                            cookie_dict[key] = f"{cookie.name}={cookie.value}"
                        value = cookie_dict
                    else:
                        # 提取指定名称的cookie，返回完整格式name=value
                        for cookie in response.cookies:
                            if cookie.name == cookie_name:
                                value = f"{cookie.name}={cookie.value}"
                                break
                
                # 响应体提取（JSONPath方式）
                elif expr.startswith('$'):
                    try:
                        data = json.loads(response_text)
                        result = jsonpath.jsonpath(data, expr)
                        value = result[0] if result else None
                    except json.JSONDecodeError:
                        print(f"响应不是有效JSON，无法使用JSONPath提取: {key}")
                
                # 响应体提取（正则表达式方式）
                else:
                    match = re.search(expr, response_text)
                    if match:
                        value = match.group(1) if match.lastindex else match.group(0)
                        # 如果提取的值是数字字符串，转换为整数
                        if isinstance(value, str) and value.isdigit():
                            value = int(value)

                # 保存提取结果
                if value is not None:
                    extracted[key] = value
                    print(f"提取成功: {key} = {value}")
                else:
                    print(f"提取失败: {key} ({expr})")

            # 将提取的数据写入yaml文件
            self.read.write_yaml_data(extracted)
            return extracted

        except Exception as e:
            print(f"数据提取异常: {str(e)}")
            return None

    def extract_data_list(self, testcase_extract_list, response):
        """
        提取多个参数，支持正则表达式和json提取，提取结果以列表形式返回
        :param testcase_extract_list: yaml文件中的extract_list信息
        :param response: 接口的实际返回值,str类型
        :return:
        """
        try:
            for key, value in testcase_extract_list.items():
                if "(.+?)" in value or "(.*?)" in value:
                    ext_list = re.findall(value, response, re.S)
                    if ext_list:
                        extract_date = {key: ext_list}
                        logs.info('正则提取到的参数：%s' % extract_date)
                        self.read.write_yaml_data(extract_date)
                if "$" in value:
                    # 增加提取判断，有些返回结果为空提取不到，给一个默认值
                    ext_json = jsonpath.jsonpath(json.loads(response), value)
                    if ext_json:
                        extract_date = {key: ext_json}
                    else:
                        extract_date = {key: "未提取到数据，该接口返回结果可能为空"}
                    logs.info('json提取到参数：%s' % extract_date)
                    self.read.write_yaml_data(extract_date)
        except:
            logs.error('接口返回值提取异常，请检查yaml文件extract_list表达式是否正确！')


if __name__ == '__main__':
    case_info = get_testcase_yaml(FILE_PATH['YAML'] + '/LoginAPI/login.yaml')[0]
    # print(case_info)
    req = RequestBase()
    # res = req.specification_yaml(case_info)
    res = req.specification_yaml(case_info)
    print(res)
