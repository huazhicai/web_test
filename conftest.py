# -*- coding:utf-8 -*-
import base64
import pytest
import allure
from py.xml import html
from selenium import webdriver

from config.conf import cm
from common.readconfig import ini
from utils.times import timestamp
from utils.send_mail import send_report
from utils.logger import log

driver = None


@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    # if driver is None:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
    options.add_experimental_option("prefs", prefs)
    options.add_argument('--headless')
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })
    # driver.maximize_window()

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    当测试失败的时候，自动截图，展示到html报告中
    :param item: 测试用例
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    report.description = str(item.function.__doc__)
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            screen_img = _capture_screenshot()
            if screen_img:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例描述'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)


def pytest_html_results_table_row(report, cells):
    cells.insert(1, html.td(report.description))
    cells.insert(2, html.td(report.nodeid))
    cells.pop(2)


def pytest_html_results_table_html(report, data):
    if report.passed:
        del data[:]
        data.append(html.div('No log output captured.', class_='empty log'))


def pytest_html_report_title(report):
    report.title = "外网项目测试报告"


def pytest_configure(config):
    config._metadata.clear()
    config._metadata['测试项目'] = "外网项目"
    # config._metadata['测试地址'] = ini.url


def pytest_html_results_summary(prefix, summary, postfix):
    # prefix.clear()  # 清空summary中的内容
    prefix.extend([html.p("测试部门：重大疾病实验室")])
    prefix.extend([html.p("测试执行人: Seven")])


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """收集测试结果"""
    result = {
        "total": terminalreporter._numcollected,
        'passed': len(terminalreporter.stats.get('passed', [])),
        'failed': len(terminalreporter.stats.get('failed', [])),
        'error': len(terminalreporter.stats.get('error', [])),
        'skipped': len(terminalreporter.stats.get('skipped', [])),
        # terminalreporter._sessionstarttime 会话开始时间
        'total times': timestamp() - terminalreporter._sessionstarttime
    }
    print(result)
    # if result['failed'] or result['error']:
    #     send_report()


def _capture_screenshot():
    """截图保存为base64"""
    now_time, screen_file = cm.screen_file
    driver.save_screenshot(screen_file)
    allure.attach.file(screen_file, "测试失败截图...{}".format(
        now_time), allure.attachment_type.PNG)
    with open(screen_file, 'rb') as f:
        imagebase64 = base64.b64encode(f.read())
    return imagebase64.decode()
