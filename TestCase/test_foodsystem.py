# -*- coding:utf-8 -*-
import os
import re
import allure
import pytest

from utils.logger import log
from common.readconfig import ini
from page_object.searchpage import PageObject

EXPECT_WORD = '食物系统大数据综合平台'


@pytest.fixture(scope='module')
def project_name():
    module_name = str(os.path.basename(__file__)).split('.')[0]
    return module_name[5:]


@allure.feature("食物系统网站测试模块")
class TestSearch:
    @allure.story('打开食物系统网站')
    def test_001(self, drivers, project_name):
        """打开食物系统网站"""
        page = PageObject(drivers, project_name)
        page_url = ini.get_url(project_name)
        page.get_url(page_url)

        result = re.search(EXPECT_WORD, page.page_source)
        assert result
