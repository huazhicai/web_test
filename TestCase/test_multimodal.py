# -*- coding:utf-8 -*-
import re
import os
import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.searchpage import PageObject


SEARCH_KEY = '肺癌'
EXPECT_WORD = '检索'
EXPECT_ELE = '数据检索结果'


@pytest.fixture(scope='module')
def project_name():
    module_name = str(os.path.basename(__file__)).split('.')[0]
    return module_name[5:]


@allure.feature("多模态测试模块")
class TestCase:
    @allure.story('打开多模态网页')
    def test_001(self, drivers, project_name):
        """搜索肺癌测试"""
        page = PageObject(drivers, project_name)
        page.get_url(ini.get_url(project_name))

        result = re.search(EXPECT_WORD, page.page_source)
        assert result

        page.search(SEARCH_KEY)
        result = page.locate_expect_element(EXPECT_ELE)
        assert result
