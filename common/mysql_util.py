#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import pymysql
from public import config
import configparser

src_path = config.src_path.replace("\\", "/")
file_path = src_path + "/config/config.ini"
cf = configparser.ConfigParser()
cf.read(file_path)
host = cf.get("mysql", "host")
port = cf.get("mysql", "port")
username = cf.get("mysql", "username")
password = cf.get("mysql", "password")
dbname = cf.get("mysql", "dbname")


class OperationDbInterface(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(host=host, user=username, passwd=password, db=dbname, port=int(port),
                                        charset='utf8', cursorclass=pymysql.cursors.DictCursor)
            self.cur = self.conn.cursor()
        except pymysql.Error as e:
            print("Mysql Error %d:%s" % (e.args[0], e.args[1]))
            logging.basicConfig(filename=src_path + '/log/syserror.log', level=logging.DEBUG, format='%(asctime)s %('
                                                                                                     'filename)s[line:%('
                                                                                                     'lineno)d] %('
                                                                                                     'levelname)s %('
                                                                                                     'message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)

    '''
    删除、更新操作，可执行insert、update、delete单条数据操作
    '''

    def operate_sql(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            result = {'code': '200', 'message': '执行通用操作成功', 'data': []}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {'code': '400', 'message': '执行通用操作失败', 'data': []}
            print("Mysql Error %d:%s" % (e.args[0], e.args[1]))
            logging.basicConfig(filename=src_path + '/log/syserror.log', level=logging.DEBUG, format='%(asctime)s %('
                                                                                                     'filename)s[line:%('
                                                                                                     'lineno)d] %('
                                                                                                     'levelname)s %('
                                                                                                     'message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result

    '''
    查询单条数据
    '''

    def select_one_sql(self, sql):
        try:
            rows_affect = self.cur.execute(sql)
            if rows_affect > 0:
                results = self.cur.fetchone()
                result = {'code': '200', 'message': '执行单条查询成功', 'data': results}
            else:
                result = {'code': '200', 'message': '执行单条查询成功', 'data': []}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {'code': '400', 'message': '执行单条查询操作失败', 'data': []}
            print("Mysql Error %d:%s" % (e.args[0], e.args[1]))
            logging.basicConfig(filename=src_path + '/log/syserror.log', level=logging.DEBUG, format='%(asctime)s %('
                                                                                                     'filename)s[line:%('
                                                                                                     'lineno)d] %('
                                                                                                     'levelname)s %('
                                                                                                     'message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result

    '''
    查询多条数据
    '''

    def select_all_sql(self, sql):
        try:
            rows_affect = self.cur.execute(sql)
            if rows_affect > 0:
                self.cur.scroll(0, mode='absolute')  # 游标光标回到初始位置
                results = self.cur.fetchall()  # 返回游标中所有结果
                result = {'code': '200', 'message': '查询多条操作成功', 'data': results}
            else:
                result = {'code': '200', 'message': '执行多条查询成功', 'data': []}
        except pymysql.Error as e:
            self.conn.rollback()
            result = {'code': '400', 'message': '执行单条查询操作失败', 'data': []}
            print("Mysql Error %d:%s" % (e.args[0], e.args[1]))
            logging.basicConfig(filename=src_path + '/log/syserror.log', level=logging.DEBUG, format='%(asctime)s %('
                                                                                                     'filename)s[line:%('
                                                                                                     'lineno)d] %('
                                                                                                     'levelname)s %('
                                                                                                     'message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return result


if __name__ == "__main__":
    op = OperationDbInterface()
    print(op.select_one_sql('select * from api where function = \'login\'')['data'])
