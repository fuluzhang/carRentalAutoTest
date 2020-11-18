'''
mark标记
1.skip：这个版本有缺陷，导致某个用例的执行不通过，可以跳过这个用例的执行，等缺陷修复后，再开放执行
2.自定义标记，
  随着代码规模增加，功能测试，接口测试，性能测试，冒烟测试，只想执行接口测试的用例，怎么挑选用例？
'''
import pytest

def test_case1():
    print("测试用例1")

@pytest.mark.skip(reason="有缺陷，缺陷号为232323，待缺陷解决后再执行")
def test_case2():
    print("测试用例2")

# 放到类上面，对类里的每个方法生效
@pytest.mark.maoyan
def test_case3():
    print("测试用例3")

@pytest.mark.api
class TestUserMark:

    @pytest.mark.maoyan
    def test_case4(self):
        print("测试用例4")
    def test_case5(self):
        print("测试用例5")
    def test_case6(self):
        print("测试用例6")