# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element


class PageObject(WebPage):
    """页面基本操作类"""

    def __init__(self, driver, project_name):
        super().__init__(driver)
        self.element = Element(project_name)

    def search(self, content, input_name='search_box', click_name='button'):
        """
        内容搜索
        :param content: 搜索内容
        :param input_name: 搜索框名   user: 'xpath==//*[@id="uid"]'
        :param click_name: 点击键名
        """
        self.input(input_name, content)
        self.click(click_name)

    def login(self, user, password, u_input_name='user', p_input_name='password', click_name='button'):
        """登录"""
        self.input(u_input_name, user)
        self.input(p_input_name, password)
        self.click(click_name)

    def input(self, input_name='input', content=None):
        """输入框"""
        assert content
        self.input_text(self.element[input_name], txt=content)
        sleep()

    def find_expect_texts(self, expect_ele_name='expect'):
        """搜索要匹配的结果"""
        return [x.text for x in self.find_elements(self.element[expect_ele_name])]

    def locate_expect_element(self, expect_ele_name='expect'):
        """定位到期望的元素"""
        return self.find_element(self.element[expect_ele_name])

    def click(self, click_name='button'):
        """点击搜索"""
        self.is_click(self.element[click_name])
        sleep()
