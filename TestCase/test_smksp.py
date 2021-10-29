# -*- coding:utf-8 -*-
import re
import os
import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.searchpage import SearchPage


SEARCH_KEY = 'Virus'


@pytest.fixture(scope='module')
def project_name():
    module_name = str(os.path.basename(__file__)).split('.')[0]
    return module_name[5:]


@allure.feature("测试结构化医疗搜索模块")
class TestSearch:
    @pytest.fixture(scope='function', autouse=True)
    def open_page(self, drivers, project_name):
        """打开结构化医疗网页测试"""
        search = SearchPage(drivers, project_name)
        page_url = ini.get_url(project_name)
        search.get_url(page_url)

    @allure.story(f"搜索{SEARCH_KEY}结果")
    def test_002(self, drivers, project_name):
        """搜索Virus结果测试"""
        search = SearchPage(drivers, project_name)
        search.input_search(SEARCH_KEY)
        search.click_search()
        # result = re.search(SEARCH_KEY, search.page_source)
        # log.info(list(search.imagine))
        assert any([SEARCH_KEY in i for i in search.imagine])


if __name__ == '__main__':
    pytest.main([str(os.path.basename(__file__))[0]])