import pymysql

class MysqlConn:
    def conn(self):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='1234',
            db = 'clean_web_culture',
            charset = 'utf8'
        )

        return conn