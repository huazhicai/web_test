# -*- coding:utf-8 -*-
from lxml import etree
from urllib.parse import urlparse


class Parser(object):
    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return
        doc_tree = etree.HTML(html_content)
        new_urls = self._get_new_urls(page_url, doc_tree)
        return new_urls

    def _get_new_urls(self, page_url, doc_tree):
        new_urls = set()
        netloc = urlparse(page_url).netloc
        links = doc_tree.xpath('//a/@href')
        for link in links:
            if netloc not in link:
                continue
            new_urls.add(link)
        return new_urls
