# -*- coding:utf-8 -*-
# @Time :2020-03-24 12:52
# @Email :876417305@qq.com
# @Author :yanxia
# @File :test_login.PY
import unittest
from common.http_request import HttpRequest
from ddt import ddt,data
from common import do_excel
from common import file_adress
from common import logger
logger=logger.get_logger(__name__)#__name__意思是把我在logger里面设置的case名字给这个用例用

@ddt
class LoginTest(unittest.TestCase):
    excel=do_excel.DoExcel(file_adress.data_path,'login')
    cases=excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.http_request=HttpRequest()

    @data(*cases)
    def test_login(self,case):
        logger.info("测试的title{}".format(case.title))
        res=self.http_request.request(case.method,case.url,case.data)
        try:
            self.assertEqual(case.expected,res.json()['code'])
            self.excel.write_result(case.case_id+1,res.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,res.text,'Fail')
            logger.error("测试报错了{}",format(e))
            raise e
    @classmethod
    def tearDown(cls):
        cls.http_request.close()
if __name__ == '__main__':
    unittest.main()