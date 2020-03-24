# -*- coding:utf-8 -*-
# @Time :2020-03-24 10:46
# @Email :876417305@qq.com
# @Author :yanxia
# @File :send_email.PY
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
from common.read_config import config
from common import file_adress
from common import logger
logger=logger.get_logger(__name__)#__name__意思是把我在logger里面设置的case名字给这个用例用
def send_email(report_file):
    msg = MIMEMultipart()  # 混合MIME格式
    # 添加html格式邮件正文（会丢失css格式)
    msg.attach(MIMEText(open(report_file,encoding='utf-8').read(),'html','utf-8'))
    now_time= time.strftime('%Y-%m-%d_%H_%M_%S')#获取时间戳
    msg['From']='yanxia_626@163.com'  # 发件人
    msg['To'] = 'yanxia_626@163.com'  # 收件人
    msg['Subject'] = Header(now_time+config.get('EMAIL','subject'), 'utf-8') # 中文邮件主题，指定utf-8编码

    att1 = MIMEText(open(report_file,'rb').read(),'base64','utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment;filename="test_report.html"'  # filename为邮件中附件显示的名字
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL('smtp.163.com')
        smtp.login('yanxia_626@163.com',"FSRTHIDKXBWEUZNC")  # 从配置文件中读取
        smtp.sendmail('yanxia_626@163.com','yanxia_626@163.com', msg.as_string())
        logger.info("邮件发送完成！")
        smtp.quit()
    except Exception as e:
        logger.error(str(e))

if __name__ == '__main__':
    send_email(file_adress.report_path)


