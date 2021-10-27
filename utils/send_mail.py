# -*- coding:utf-8 -*-
import zmail
from utils.logger import log
from config.conf import cm


def send_report():
    """发送报告"""
    with open(cm.REPORT_FILE, encoding='utf-8') as f:
        content_html = f.read()
    try:
        mail = {
            'from': cm.EMAIL_INFO['username'],
            'subject': '新测试报告',
            'content_html': content_html,
            'attachments': [cm.REPORT_FILE]
        }
        server = zmail.server(*cm.EMAIL_INFO.values())
        server.send_mail(cm.ADDRESSEE, mail)
        log.info('测试邮件发送成功！')
    except Exception as e:
        log.warning(f'邮件发送失败{e}')
