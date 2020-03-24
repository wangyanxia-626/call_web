# -*- coding:utf-8 -*-
# @Time :2020-03-23 19:46
# @Email :876417305@qq.com
# @Author :yanxia
# @File :file_adress.PY
import os
#获取根目录
prj_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#获取执行那套环境的路径
global_file=os.path.join(prj_dir,'config','global.cfg')
#获取线上环境
online_file=os.path.join(prj_dir,'config','online.cfg')
#获取测试环境
test_file=os.path.join(prj_dir,'config','test.cfg')
#获取日志的路径
log_dir=os.path.join(prj_dir,'log')
#获取测试报告的路径
report_path=os.path.join(prj_dir,'reports','test_report.html')
#获取测试用例的路径
case_dir=os.path.join(prj_dir,'data')
print(case_dir)
print(r"G:\CALLWEB_API\testcases")
#获取测试数据data_case路径
data_path=os.path.join(prj_dir,'data_case','cases.xlsx')