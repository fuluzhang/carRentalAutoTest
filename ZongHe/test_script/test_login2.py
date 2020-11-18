'''
测试登录功能
'''
import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_data.yaml"))
def login_data(request):  # 固定写法
    return request.param

@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_setup.yaml"))
def setup_data(request):  # 固定写法
    return request.param

# 测试前置和后置
@pytest.fixture()
def register(setup_data,url,baserequests,db):
    # 注册
    phone = setup_data['casedata']['mobilephone']
    DbOp.deleteUser(db, phone)
    Member.register(url, baserequests, setup_data['casedata'])
    yield
    # 删除注册用户
    DbOp.deleteUser(db, phone)

def test_login(register,login_data,url,baserequests):
    # 登录
    # 检查登录的结果
    r = Member.login(url, baserequests, login_data['casedata'])
    assert r.json()['msg'] == login_data['expect']['msg']
    assert r.json()['status'] == login_data['expect']['status']
    assert r.json()['code'] == login_data['expect']['code']