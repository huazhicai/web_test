import os
import re
import allure
import pytest

from config.conf import cm
from utils.logger import log
from common.readconfig import ini
from page_object.searchpage import PageObject


EXPECT_WORD = '内容'


@pytest.fixture(scope='module')
def project_name():
    module_name = str(os.path.basename(__file__)).split('.')[0]
    return module_name[5:]


@allure.feature("测试卫健委模块")
class TestSearch:
    @allure.story('卫健委登录测试')
    def test_001(self, drivers, project_name):
        """卫健委登录测试"""
        page = PageObject(drivers, project_name)
        page_url = ini.get_url(project_name)
        page.get_url(page_url)
        page.input('user', cm.USER)
        page.input('password', cm.PASSWORD2)
        page.click()

        result = re.search(EXPECT_WORD, page.page_source)
        log.info(result)
        assert result


