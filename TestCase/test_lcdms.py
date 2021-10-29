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


EXPECT_WORD = '首页'
EXPECT_ELE = '文本输入框'   # 病人资料 的定位元素
EXPECT_WORD1 = '开始检索'   # 智能检索 出现的字
EXPECT_WORD2 = '分析模块'   # 数据分析 出现的字


@pytest.fixture(scope='module')
def project_name():
    module_name = str(os.path.basename(__file__)).split('.')[0]
    return module_name[5:]


@allure.feature("测试多中心模块")
class TestSearch:
    @allure.story('多中心登录测试')
    def test_001(self, drivers, project_name):
        """多中心登录测试"""
        page = PageObject(drivers, project_name)
        page_url = ini.get_url(project_name)
        page.get_url(page_url)
        page.input('user', cm.USER)
        page.input('password', cm.PASSWORD)
        page.click()

        result = re.search(EXPECT_WORD, page.page_source)
        log.info(result)
        assert result

    @allure.story('病人资料&数据分析&交流窗口点击测试')
    def test_002(self, drivers, project_name):
        """病人资料&数据分析&交流窗口点击测试"""
        page = PageObject(drivers, project_name)

        page.click('病人资料')
        result = page.locate_expect_element(EXPECT_ELE)
        log.info(result)
        with assume: assert result

        page.click('智能检索')
        result = re.search(EXPECT_WORD1, page.page_source)
        log.info(result)
        with assume: assert result

        page.click('数据分析')
        result = re.search(EXPECT_WORD2, page.page_source)
        log.info(result)
        assert result



