import pymysql
from scrapy.utils.project import get_project_settings


class DBHelper():
    def __init__(self):
        settings = get_project_settings()
        host = settings['MYSQL_HOST']
        port = settings['MYSQL_PORT']
        db = settings['MYSQL_DBNAME']
        user = settings['MYSQL_USER']
        passwd = settings['MYSQL_PASSWORD']

        self.db_conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()

    # 关闭数据库
    def close(self):
        self.db_conn.commit()
        self.db_conn.close()

    # 插入数据
    def insert_to_db(self, item):
        values = (item['name'], item['score'], item['time'], item['comment'])
        sql = 'INSERT INTO movie_comments(name,score,time,comment) VALUES(%s,%s,%s,%s)'
        self.db_cur.execute(sql, values)