# -*- coding:utf-8 -*-
"""
此模块遍历访问所有网站内链接
"""
import time
import urllib3

from config.conf import cm
from monitor_url import url_manager, html_parser
from monitor_url.downloader import get_request


urllib3.disable_warnings()


class Monitor(object):
    def __init__(self, url):
        self.root_url = url
        self.urls = url_manager.UrlManager()
        self.parser = html_parser.Parser()
        self.exception_links = set()

    def vist_web_page(self):
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                response = get_request(new_url)
                if response:
                    self.urls.old_urls.add(new_url)
                    new_urls = self.parser.parse(new_url, response.text)
                    self.urls.add_new_urls(new_urls)
                else:
                    self.urls.failed_urls.add(new_url)
                time.sleep(1)
            except Exception as e:
                print(str(e))

    def run(self, interval=300):
        self.urls.add_new_url(self.root_url)
        self.vist_web_page()

        failed_urls = [url for url in self.urls.failed_urls if url not in cm.EXCLUDE_URLS]
        if failed_urls:  # 第二次访问异常的url请求
            # time.sleep(interval)
            self.urls.add_new_urls(self.urls.failed_urls)
            self.urls.failed_urls.clear()
            self.vist_web_page()

        return self.urls.failed_urls



