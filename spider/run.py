#-*-coding:utf-8-*-
import datetime
import spider
from Email import Email
from db_operate import db

date = str(datetime.date.today()+datetime.timedelta(days=1))[:10]

if db.isnull():
	list_=spider.spider()
	db.insert(list_)

user_list = db.get_user()

if db.judge(date):
    html_body = Email.get_html()
    Email.send(user_list,html_body)

db.update()
