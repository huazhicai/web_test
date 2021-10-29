# -*- coding:utf-8 -*-
import re
import os
import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.searchpage import SearchPage


SEARCH_KEY = '肺癌'


@pytest.fixture(scope='module')
def project_name():
    module_name = str(os.path.basename(__file__)).split('.')[0]
    return module_name[5:]


@allure.feature("测试多模态模块")
class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_page(self, drivers, project_name):
        """打开多模态网页"""
        search = SearchPage(drivers, project_name)
        search.get_url(ini.get_url(project_name))

    @allure.story("搜索肺癌结果用例")
    def test_001(self, drivers, project_name):
        """搜索肺癌结果用例"""
        search = SearchPage(drivers, project_name)
        search.input_search(SEARCH_KEY)
        search.click_search()
        result = re.search(SEARCH_KEY, search.page_source).group()
        log.info(result)
        assert result


if __name__ == '__main__':
    pytest.main(['test_search.py'])