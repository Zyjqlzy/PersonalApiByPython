#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import ddt
import unittest
from common import mysql_util
from common import base_api


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.op = mysql_util.OperationDbInterface()
        self.testdata = self.op.select_one_sql('select * from api where function = \'login\'')['data']
        print(self.testdata)

    def test_login(self):
        r = base_api.send_requests(self.testdata)
        return r['data']


if __name__ == "__main__":
    unittest.main()
