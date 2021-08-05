import pymysql;


import os, json
from django.core.exceptions import ImproperlyConfigured

from config.settings import get_secret

config = {
    'database': 'shopdb',
    'user': 'shop_user',
    'password': get_secret("DB_PW"),
    'host':'127.0.0.1',
    'port': 3306,
    'charset':'utf8',
    'use_unicode':True
}
class Db:
    def getConnection(self):
        conn = pymysql.connect(**config);
        return conn;

    def close(self, conn, cursor):
        if cursor != None:
            cursor.close();
        if conn != None:
            conn.close();