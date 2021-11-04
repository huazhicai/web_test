# -*- coding:utf-8 -*-
import os
import re
import allure
import pytest

from common.readconfig import ini
from page_object.searchpage import PageObject


SEARCH_KEY = '慢性肾脏病发病率预测'  # 应用展示搜索
SEARCH_KEY2 = 'BMI 计算'           # 知识对象搜索
EXPECT_WORD = '目标与愿景'


@pytest.fixture(scope='module')
def project_name():
    module_name = str(os.path.basename(__file__)).split('.')[0]
    return module_name[5:]


@allure.feature("K-GRID测试模块")
class TestCase:
    # @pytest.fixture(scope='function', autouse=True)
    # def go_home_page(self, drivers, project_name):
    #     """huodaoshouye"""
    #     page = PageObject(drivers, project_name)
    #     page_url = ini.get_url(project_name)
    #     page.get_url(page_url)

    @allure.story('应用展示测试')
    def test_001(self, drivers, project_name):
        """应用展示搜索慢性肾脏病发病率预测"""
        page = PageObject(drivers, project_name)
        page_url = ini.get_url(project_name)
        page.get_url(page_url)

        page.click('应用展示')
        page.search(SEARCH_KEY)
        result = page.locate_expect_element()
        assert result

    @allure.story('知识对象测试')
    def test_002(self, drivers, project_name):
        """知识对象搜索BMI计算测试"""
        page = PageObject(drivers, project_name)
        page.click('知识对象')
        page.search(SEARCH_KEY2)
        page.click(SEARCH_KEY2)
        result = re.search(SEARCH_KEY2, page.page_source)
        assert result

    @allure.story('平台导引测试')
    def test_003(self, drivers, project_name):
        """平台引导&大事记&关于我们点击测试"""
        page = PageObject(drivers, project_name)
        page.switch_to_home()

        page.click('平台引导')
        page.click('大事记')
        page.click('关于我们')

        result = re.search(EXPECT_WORD, page.page_source)
        assert result
