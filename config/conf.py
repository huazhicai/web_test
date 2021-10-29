# -*- coding:utf-8 -*-
import os
from selenium.webdriver.common.by import By
from utils.times import dt_strftime


def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@singleton
class ConfigManager(object):
    # 项目目录
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 页面元素目录
    ELEMENT_PATH = os.path.join(ROOT_DIR, 'page_element')

    # 报告文件
    REPORT_FILE = os.path.join(ROOT_DIR, 'report.html')

    # 元素定位的类型
    LOCATE_MODE = {
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH,
        'name': By.NAME,
        'id': By.ID,
        'class': By.CLASS_NAME
    }

    # 邮件信息
    EMAIL_INFO = {
        'username': '936844218@qq.com',
        'password': 'QQ邮箱授权码',
        'smtp_host': 'smtp.qq.com',
        'smtp_port': 465
    }

    # 收件人
    ADDRESSEE = [
        'django3997@dingtalk.com',
    ]

    # project name
    PROJECT_2_URL = {
        'k_grid': 'https://www.kgrid-china.net/layout/Home',
        'ck_net': 'https://www.chinakidney.net/',
        'multimodal': 'http://47.98.134.243:8390/multimodal-web/index',  # 多模态
        'foodsystem': 'http://foodsystem.wit-health.net:8190/foodsystem-web/Front_2/Template_C_1',
        'nursequeue': 'https://nursecohort.kgrid-china.net/rmyy-nursequeue-web/login',
        'cstride': 'https://cstride.bjmu.edu.cn/login',  # 多中心
        'ckd': 'https://chinackd.bjmu.edu.cn/followup-web/module/login.html#/',
        'nhc': 'https://nhc.chinakidney.net/login',  # 卫健委
        'lcdms': 'https://lcdms.bjmu.edu.cn/hydrocephaly-web/login',  # 脑积水
        'smksp': 'http://202.112.180.134/smksp-web/search',  # 结构化医疗搜索
    }

    USER_PSW = [('test2', 'ZHYL2021'), ('test2', '123456')]  # 卫健委第二个

    HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
    EXCLUDE_URLS = []

    @property
    def screen_path(self):
        """截图目录"""
        screenshot_dir = os.path.join(self.ROOT_DIR, 'screen_capture')
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        now_time = dt_strftime("%Y%m%d%H%M%S")
        screen_file = os.path.join(screenshot_dir, "{}.png".format(now_time))
        return now_time, screen_file

    @property
    def log_file(self):
        """日志目录"""
        log_dir = os.path.join(self.ROOT_DIR, 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        return os.path.join(log_dir, '{}.log'.format(dt_strftime()))

    @property
    def ini_file(self):
        """配置文件"""
        ini_file = os.path.join(self.ROOT_DIR, 'config', 'config.ini')
        if not os.path.exists(ini_file):
            raise FileNotFoundError("配置文件%s不存在！" % ini_file)
        return ini_file


cm = ConfigManager()

if __name__ == '__main__':
    print(cm.ROOT_DIR)
