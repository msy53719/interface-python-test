# coding=utf-8
import pymysql.cursors


class mysqlHelper():
    def connection(self, ip, port, user, pwd, db, cls):
        # conect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='msy53719', db='python_test',
        #  cursorclass=pymysql.cursors.DictCursor)
        conect = pymysql.connect(host=ip, port=port, user=user, password=pwd, db=db,
                                 cursorclass=cls)
        return conect


p = mysqlHelper()
s = p.connection('127.0.0.1', 3306, 'root', 'msy53719', 'python_test', 'pymysql.cursors.DictCursor')
print(s)
