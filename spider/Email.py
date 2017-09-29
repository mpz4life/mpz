#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import datetime
from db_operate import db

class Email(object):
	def __init__(self):
		self.from_addr = "574259162@qq.com"
		self.smtp = smtplib.SMTP_SSL("smtp.qq.com",465)
		self.smtp.ehlo("smtp.qq.com")
		self.smtp.login(self.from_addr,"usahyflyuabobfej")

	def get_html(self):
		html_body = "<table border='1'>" \
            "<tr><th>公司名</th><th>地点</th><th>时间</th><th>详情</th></tr>"
		date = str(datetime.date.today()+datetime.timedelta(days=1))[0:10]
		list_ = db.read(date)
		for item in list_:
			html_body += "<tr><td>%s</td><td>%s</td><td>%s</td><td><a href=\'%s\'>详情</a></td></tr>" %(item[0],item[2],item[3],item[1])
		html_body = html_body+"</table>"
		return html_body




	def send(self,addr_list,content):
		for item in addr_list:
			html_titile="<p>亲爱的%s童鞋:<p><br><p>这是明天的宣讲会信息哦！<strong>请查收</strong></p>" %item[0]
			html = html_titile+content
			msg = MIMEText(html,'html','utf-8')
			msg["Subject"] =Header("宣讲会信息","utf-8")
			msg["From"] = "mpz<574259162@qq.com>"
			msg["To"] = item[1]
			self.smtp.sendmail(self.from_addr,item[1],msg.as_string())
		self.smtp.quit()
	
Email=Email()
