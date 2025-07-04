import shutil
import pytest
import os
import webbrowser
from conf.setting import REPORT_TYPE

if __name__ == '__main__':

    if REPORT_TYPE == 'allure':
        pytest.main(
            ['-s', '-v', '--alluredir=./report/allure/temp', './testcase', '--clean-alluredir',
             '--reruns=0', '--reruns-delay=1',
             '--junitxml=./report/allure/results.xml'])
        # '-m', 'course_management',
        shutil.copy('./environment.xml', './report/allure/temp')
        os.system('allure generate ./report/allure/temp -o ./report/allure/html --clean')
        # os.system('allure generate ./report/allure/temp -o ./report/allure/single_html --clean --single-html')  # 全局变量allure/bin?
        # os.system('allure-combine ./report/allure/html --dest ./report/allure/html')
        # if not os.getenv('CI'):
            # os.system('allure serve ./report/allure/temp')
    # （Test Management）
    elif REPORT_TYPE == 'tm':
        pytest.main(['-vs', '--pytest-tmreport-name=testReport.html', '--pytest-tmreport-path=./report/tmreport', 
                     '--reruns=2', '--reruns-delay=1'])
        if not os.getenv('CI'):
            webbrowser.open_new_tab(os.getcwd() + '/report/tmreport/testReport.html')
