# -*- coding:utf-8 -*-
# @Time :2020-03-24 9:38
# @Email :876417305@qq.com
# @Author :yanxia
# @File :run.PY
import unittest
import HTMLTestRunnerNew
from common import file_adress
from common.send_email import send_email
from common import logger
logger=logger.get_logger(__name__)#__name__意思是把我在logger里面设置的case名字给这个用例用

logger.info("=====================================开始测试=================================")
discover=unittest.defaultTestLoader.discover(file_adress.case_dir,'test_*.py')
with open(file_adress.report_path,'wb') as file:
    HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title="接口自动化测试报告",
                                            description="各位好，以下是本次接口自动化报告结果，请查看",
                                            tester="wangyanxia").run(discover)

send_email(file_adress.report_path)
logger.info("=====================================结束测试=================================")
