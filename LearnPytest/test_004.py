'''
fixture作用域：
默认是function级别的。有function，module，class，session级别
'''
import pytest

@pytest.fixture(scope='class') # 每个类调用一次，在类中首次调用这个fixture的时候，执行前置，类里方法执行完执行后置
def login():
    print("登录系统") # 前置
    yield
    print("退出登录") # 后置

@pytest.fixture()  # 默认是function级别的，调用它的方法执行前执行前置，这个方法执行完执行后置
def login1():
    print("系统登录")
    yield
    print("退出登录")

@pytest.fixture(scope='module')  #首次调用这个fixture的地方执行前置，全部用例(当前.py文件中的所有用例)执行完执行后置
def login2():
    print("系统登录")
    yield
    print("退出登录")

class TestQuery():
    def test_case1(self):
        print("测试查询1")
    def test_case2(self,login): # 执行前置
        print("测试查询2")
    def test_case3(self):  #3执行完 执行后置
        print("测试查询3")

class TestDelete():
    def test_case1(self,login): # 执行前置
        print("测试删除1")
    def test_case2(self):
        print("测试删除2")
    def test_case3(self):  #3执行完 执行后置
        print("测试删除3")
