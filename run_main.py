#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from public import config
import os
from common import logger
import HTMLTestRunner_2

log = logger.Log()
report_path = os.path.join(config.src_path, "report")
if not os.path.exists(report_path):
    os.mkdir(report_path)


def add_test(caseName="case", rule="test*.py"):
    case_path = os.path.join(config.src_path, caseName)
    log.debug('用例路径：%s' % case_path)
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule)
    return discover


def run_case(all_case, reportpath=report_path):
    htmlreport = reportpath + r'\report.html'
    log.debug('测试报告：%s' % htmlreport)
    fp = open(htmlreport, 'wb')
    runner = HTMLTestRunner_2.HTMLTestRunner(stream=fp, verbosity=2, title='测试报告', description='用例执行情况')
    runner.run(all_case)
    fp.close()


if __name__ == "__main__":
    cases = add_test()
    run_case(cases)
