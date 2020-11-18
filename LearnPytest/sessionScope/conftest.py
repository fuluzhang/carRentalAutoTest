'''
conftest.py session 级别的fixture放到这个文件当中，文件名字不能写错

第一次调用fixture执行前置，目录下所有文件执行完，再执行后置。
conftest.py 文件有作用域，对同级目录和子目录生效
一个工程中可以有多个conftest.py文件
'''

import pytest

@pytest.fixture(scope='session')
def login():
    print("系统登录")
    yield
    print("退出登录")