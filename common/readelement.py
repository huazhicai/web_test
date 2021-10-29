# -*- coding:utf-8 -*-
import os
import yaml
from config.conf import cm


file_name = 'search.yaml'


class Element(object):
    """获取元素"""

    def __init__(self, project_name):
        self.project = project_name
        # self.file_name = '%s.yaml' % name
        self.element_path = os.path.join(cm.ELEMENT_PATH, file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性"""
        data = self.data.get(self.project).get(item)
        if data:
            name, value = data.split('==')
            return name, value
        raise ArithmeticError("{}中不存在关键字：{}".format(file_name, item))


if __name__ == '__main__':
    search = Element('smksp')
    print(search['搜索框'])


