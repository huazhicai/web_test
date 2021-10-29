# -*- coding:utf-8 -*-
import os
import re
import allure
import pytest

from pytest import assume

from config.conf import cm
from utils.logger import log
from common.readconfig import ini
from page_object.searchpage import PageObject


LOGOUT = '退出登录'
EXPECT_WORD = '社会统计学'
# EXPECT_WORD = '社会统计学'
EXPECT_ELE = '文本输入框'


@pytest.fixture(scope='module')
def project_name():
    module_name = str(os.path.basename(__file__)).split('.')[0]
    return module_name[5:]


@allure.feature("测试ckd模块")
class TestSearch:
    @allure.story('ckd登录测试')
    def test_001(self, drivers, project_name):
        """ckd登录测试"""
        page = PageObject(drivers, project_name)
        page_url = ini.get_url(project_name)
        page.get_url(page_url)
        page.input('user', cm.USER)
        page.input('password', cm.PASSWORD)
        page.click()

        result = re.search(LOGOUT, page.page_source)
        log.info(result)
        assert result

    @allure.story('预约管理&统计分析点击测试')
    def test_002(self, drivers, project_name):
        """点击测试预约管理&统计分析模块"""
        page = PageObject(drivers, project_name)
        page.click('预约管理')

        result = page.locate_expect_element(EXPECT_ELE)
        log.info(result)
        with assume: assert result

        page.click('统计分析')
        result = re.search(EXPECT_WORD, page.page_source)
        log.info(result)
        assert result



