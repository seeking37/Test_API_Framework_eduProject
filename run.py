import shutil
import pytest
import os
import webbrowser
from conf.setting import REPORT_TYPE

if __name__ == '__main__':

    if REPORT_TYPE == 'allure':
        pytest.main(
            ['-s', '-v', '--alluredir=./report/allure/temp', './testcase', '--clean-alluredir',
             '--junitxml=./report/allure/results.xml'])
        shutil.copy('./environment.xml', './report/allure/temp')
        os.system('allure generate ./report/allure/temp -o report/allure/html --clean')
        os.system('allure generate ./report/allure/temp -o report/allure --single-html')
        if not os.getenv('CI'):
            os.system('allure serve ./report/allure/temp')
    # （Test Management）
    elif REPORT_TYPE == 'tm':
        pytest.main(['-vs', '--pytest-tmreport-name=testReport.html', '--pytest-tmreport-path=./report/tmreport'])
        if not os.getenv('CI'):
            webbrowser.open_new_tab(os.getcwd() + '/report/tmreport/testReport.html')
