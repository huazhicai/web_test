# -*- coding:utf-8 -*-
import configparser
from config.conf import ConfigManager

HOST = 'host'


class ReadConfig(object):
    def __init__(self):
        self.cm = ConfigManager()
        self.config = configparser.RawConfigParser()  # 当有%的符号时请使用Raw读取
        self.config.read(self.cm.ini_file, encoding='utf-8')

    def _get(self, section, option):
        return self.config.get(section, option)

    def _set(self, section, option, value):
        self.config.set(section, option, value)
        with open(self.cm.ini_file, 'w') as f:
            self.config.write(f)

    @property
    def url(self):
        return self._get(HOST, HOST)


ini = ReadConfig()

if __name__ == '__main__':
    rc = ReadConfig()
    print(rc.url)