#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from public import config
import time

src_path = config.src_path.replace("\\", "/")
log_path = src_path + '/log/'
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))[:-4]  # 时间戳


class Log(object):
    def __init__(self):
        self.log_name = log_path + rq + '.log'
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s')

    def __consle(self, level, message):
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 创建一个FileHandle，往文件写入日志
        sh = logging.StreamHandler()  # 创建StreamHandler，用于输出控制台
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        sh.setLevel(logging.DEBUG)
        sh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(sh)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 下面两行为了防止重复输出日志
        self.logger.removeHandler(sh)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        self.__consle('debug', message)

    def info(self, message):
        self.__consle('info', message)

    def warning(self, message):
        self.__consle('warning', message)

    def error(self, message):
        self.__consle('error', message)


if __name__ == "__main__":
    log = Log()
    log.info('info测试')
    log.debug('debug测试')
