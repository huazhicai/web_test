# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element

SEARCH_BOX = '搜索框'
SEARCH_BUTTON = '搜索按钮'


class SearchPage(WebPage):
    """搜索类"""

    def __init__(self, driver, project_name):
        super().__init__(driver)
        self.search = Element(project_name)

    def input_search(self, content):
        """输入搜索"""
        self.input_text(self.search[SEARCH_BOX], txt=content)
        sleep()

    @property
    def imagine(self):
        """搜索联想"""
        return [x.text for x in self.find_elements(self.search['候选'])]

    def click_search(self):
        """点击搜索"""
        self.is_click(self.search[SEARCH_BUTTON])


class PageObject(WebPage):
    """页面基本操作类"""

    def __init__(self, driver, project_name):
        super().__init__(driver)
        self.search = Element(project_name)

    def input(self, input_name, content):
        """输入框"""
        self.input_text(self.search[input_name], txt=content)
        sleep()

    def find_expect_texts(self, expect='expect'):
        """搜索要匹配的结果"""
        return [x.text for x in self.find_elements(self.search[expect])]

    def locate_expect_element(self, expect='expect'):
        """定位到期望的元素"""
        return self.find_element(self.search[expect])

    def click(self, click_name='button'):
        """点击搜索"""
        self.is_click(self.search[click_name])
        sleep()
