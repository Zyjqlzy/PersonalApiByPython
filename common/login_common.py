#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from common import mysql_util
from common import base_api
from common import logger
from public import config

"""
登录操作封装，返回token
"""
class LoginCommon(object):

    def login_common(self):
        op = mysql_util.OperationDbInterface()
        testdata = op.select_one_sql('select * from api where function = \'login\'')['data']
        testdata['params'] = json.loads(testdata['params'])
        r = base_api.send_requests(testdata)
        return r['data']['token']


if __name__ == "__main__":
    lc = LoginCommon()
    print(lc.login_common())
