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


@pytest.fixture(scope='module')
def project_name():
    module_name = str(os.path.basename(__file__)).split('.')[0]
    return module_name[5:]


@allure.feature("护士队列测试模块")
class TestCase:
    @pytest.mark.dependency()
    @allure.story('护士队队列登录测试')
    def test_001(self, drivers, project_name):
        """护士队队列登录测试"""
        page = PageObject(drivers, project_name)
        page_url = ini.get_url(project_name)
        page.get_url(page_url)
        page.login(cm.USER, cm.PASSWORD)

        result = re.search(EXPECT_WORD, page.page_source)
        assert result

    @pytest.mark.dependency(depends=['test_001'], scope='class')
    @allure.story('护士资料点击测试')
    def test_002(self, drivers, project_name):
        """护士资料点击测试"""
        page = PageObject(drivers, project_name)

        page.click('护士资料')
        result = page.locate_expect_element()
        assert result




