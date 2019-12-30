import unittest
from common import logger
from common import mysql_util
from common import base_api
from common import login_common
import json


class TestAddBasicInfo(unittest.TestCase):
    log = logger.Log()

    def setUp(self):
        self.log.debug('*******初始化开始：-----  %s  ----**********' % __name__)
        self.op = mysql_util.OperationDbInterface()
        self.lc = login_common.LoginCommon()
        token = self.lc.login_common()
        print(token)
        self.testdata = self.op.select_one_sql('select * from api where function = \'addBasicInfo\'')['data']
        temp = json.loads(self.testdata['params'])
        temp['token'] = token
        self.testdata['params'] = temp
        print(self.testdata)
        self.log.debug('*******初始化成功！**********')

    def test_addbasicinfo(self):
        self.r = base_api.send_requests(self.testdata)

    def tearDown(self):
        self.op.close()


if __name__ == '__main__':
    unittest.main()
