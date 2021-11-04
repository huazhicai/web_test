# -*- coding:utf-8 -*-
import re
import os
import pytest
import allure
from utils.logger import log
from common.readconfig import ini
from page_object.searchpage import PageObject


SEARCH_KEY = 'Virus'


@pytest.fixture(scope='module')
def project_name():
    module_name = str(os.path.basename(__file__)).split('.')[0]
    return module_name[5:]


@allure.feature("测试结构化医疗搜索模块")
class TestSearch:
    @pytest.fixture(scope='class', autouse=True)
    def open_page(self, drivers, project_name):
        """打开结构化医疗网页测试"""
        page = PageObject(drivers, project_name)
        page_url = ini.get_url(project_name)
        page.get_url(page_url)

    @allure.story(f"医疗结构知识测试用例")
    def test_002(self, drivers, project_name):
        """搜索Virus测试"""
        page = PageObject(drivers, project_name)
        page.search(SEARCH_KEY)
        assert any([SEARCH_KEY in i for i in page.find_expect_texts()])


if __name__ == '__main__':
    pytest.main([str(os.path.basename(__file__))[0]])