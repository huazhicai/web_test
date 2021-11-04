# -*- coding:utf-8 -*-
import yaml
from config.conf import cm


class Element(object):
    """获取元素"""

    def __init__(self, project_name):
        self.project = project_name

        with open(cm.element_file, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性"""
        data = self.data.get(self.project).get(item)
        if data:
            name, value = data.split('==')
            return name, value
        raise ArithmeticError("{}中不存在关键字：{}".format(cm.element_file, item))


if __name__ == '__main__':
    search = Element('k_grid')
    from pprint import pprint
    pprint(search.data)


