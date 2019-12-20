#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import unittest
from common import mysql_util
from common import base_api

op = mysql_util.OperationDbInterface()
testdata = op.select_one_sql('select * from api where function = \'login\'')[0]['data']
print(testdata)
class TestLogin(unittest.TestCase):
    def SetUp(self):
        print(testdata)

    def test_login(self,testdata):
        r = base_api.send_requests(testdata)


if __name__ == "__main__":
    unittest.main()
