#-*-coding:utf-8-*-
import datetime
import MySQLdb
# from test_2 import mpz_

class job_db(object):
    def __init__(self):
        self.db = MySQLdb.connect('localhost','root','040810','mpz',charset="utf8")
        self.cursor = self.db.cursor()

    def isnull(self):
        sql = "select count(*) from job;"
        self.cursor.execute(sql)
        count = self.cursor.fetchone()[0]
        if count == 0:
            return True
        else:
            return False

    def insert(self,list_):
        for item in list_:

            sql = "insert into job values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\');"\
                    %(item[0],item[1],item[2],item[3],item[4])
            try:
                self.cursor.execute(sql)
            except:
                continue
        self.db.commit()

    def update(self):
        today = str(datetime.date.today())[:10]
        sql = "delete from job WHERE date_=\'%s\'" %today
        self.cursor.execute(sql)
        self.db.commit()

    def read(self,date):
        sql = "select * from job where date_=\'%s\'" %date
        self.cursor.execute(sql)
        list_ = self.cursor.fetchall()
        return list_

    def get_user(self):
        sql = "select * from user"
        self.cursor.execute(sql)
        list_ = self.cursor.fetchall()
        return list_  

    def judge(self,date):
        sql ="select company from job where date_=\'%s\'" %date
        self.cursor.execute(sql)
        list_ = self.cursor.fetchone()
        if len(list_)>0:
            return True
        else:
            return False  

db = job_db()
