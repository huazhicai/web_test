# -*- coding:utf-8 -*-
# import allure
# import pytest
# import os
#
# from common.readconfig import ini
# from monitor_url.monitor import Monitor
#
# import urllib3
#
# urllib3.disable_warnings()
#
#
# @pytest.fixture(scope='module')
# def project_name():
#     module_name = str(os.path.basename(__file__)).split('.')[0]
#     return module_name[5:]
#
#
# @allure.feature("测试模块")
# class TestSearch:
#     @allure.story('测试cknet所有内网链接')
#     def test_001(self, project_name):
#         print(project_name)
#         page_url = ini.get_url(project_name)
#         failed_url = Monitor(page_url).run()
#         assert not failed_url, '测试请求失败的链接{}'.format(str(failed_url))
#
#
# if __name__ == '__main__':
#     pytest.main(['test_search.py'])