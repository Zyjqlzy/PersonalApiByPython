#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def send_requests(testdata):
    method = testdata['method']  # POST or GET or DELETE
    url = testdata['url']  # 接口
    params = testdata['params']  # 参数
    test_func = testdata['function']  # 功能
    print("*******正在执行用例：-----  %s  ----**********" % test_func)
    print("请求方式：%s, 请求url:%s" % (method, url))
    print("请求params：%s" % params)

    try:
        if method == "post":
            r = requests.post(url, params)
        else:
            r = requests.get(url, params)
        result = r.json()
    except Exception as e:
        print(e)

    return result
# if __name__ == "__main__":
