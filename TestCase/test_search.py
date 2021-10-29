# # -*- coding:utf-8 -*-
# import re
# import pytest
# import allure
# from utils.logger import log
# from common.readconfig import ini
# from page_object.searchpage import SearchPage
#
#
# @allure.feature("测试ckd模块")
# class TestSearch:
#     @pytest.fixture(scope='function', autouse=True)
#     def open_baidu(self, drivers):
#         """打开ckd"""
#         search = SearchPage(drivers)
#         search.get_url(ini.url)
#
#     @allure.story("搜索肺癌结果用例")
#     def test_001(self, drivers):
#         """搜索"""
#         search = SearchPage(drivers)
#         search.input_search("肺癌")
#         search.click_search()
#         result = re.search(r'肺癌', search.page_source)
#         log.info(result)
#         assert result
#
#     # @allure.story("测试搜索候选用例")
#     # def test_002(self, drivers):
#     #     """测试搜索候选"""
#     #     search = SearchPage(drivers)
#     #     search.input_search("selenium")
#     #     log.info(list(search.imagine))
#     #     assert all(["selenium" in i for i in search.imagine])
#
#
# if __name__ == '__main__':
#     pytest.main(['test_search.py'])
#
