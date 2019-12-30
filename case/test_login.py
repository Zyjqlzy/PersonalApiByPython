#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import ddt
import unittest
from common import mysql_util
from common import base_api
from common import logger
from public import config
import logging
import time

src_path = config.src_path.replace("\\", "/")
file_path = src_path + "/config/config.ini"
log_path = src_path + '/log/'
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))[:-4]  # 时间戳


class TestLogin(unittest.TestCase):
    log = logger.Log()

    def setUp(self):
        self.log.debug('*******初始化开始：-----  %s  ----**********' % __name__)
        self.op = mysql_util.OperationDbInterface()
        self.testdata = self.op.select_one_sql('select * from api where function = \'login\'')['data']
        self.log.debug('*******初始化成功！**********')

    def test_login(self):
        self.r = base_api.send_requests(self.testdata)

    def tearDown(self):
        self.op.close()


if __name__ == "__main__":
    unittest.main()
