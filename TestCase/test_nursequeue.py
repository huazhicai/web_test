# -*- coding:utf-8 -*-
import os
import re
import allure
import pytest

from config.conf import cm
from utils.logger import log
from common.readconfig import ini
from page_object.searchpage import PageObject


EXPECT_WORD = '首页'
EXPECT_ELE = '文本输入框'  # 护士资料 的定位元素


@pytest.fixture(scope='module')
def project_name():
    module_name = str(os.path.basename(__file__)).split('.')[0]
    return module_name[5:]


@allure.feature("测试护士队列模块")
class TestSearch:
    @allure.story('护士队登录测试')
    def test_001(self, drivers, project_name):
        """护士队登录测试"""
        page = PageObject(drivers, project_name)
        page_url = ini.get_url(project_name)
        page.get_url(page_url)
        page.input('user', cm.USER)
        page.input('password', cm.PASSWORD)
        page.click()

        result = re.search(EXPECT_WORD, page.page_source)
        log.info(result)
        assert result

    @allure.story('护士资料')
    def test_002(self, drivers, project_name):
        """护士资料点击测试"""
        page = PageObject(drivers, project_name)

        page.click('护士资料')
        result = page.locate_expect_element(EXPECT_ELE)
        log.info(result)
        assert result




