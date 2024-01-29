# -- coding: utf-8 --
# @Time    : 2024/1/28 11:35
# @Author  : TangKai
# @Team    : ZheChengData


class Test(object):
    def __init__(self, name: str = '2'):
        self.name = name

    def run(self):
        print(rf'hello {self.name}! Actions Test!')
