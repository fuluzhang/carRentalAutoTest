'''
登录的测试脚本
'''
import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_fail.yaml"))
def login_fail_data(request):  # 固定写法
    return request.param

@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_success.yaml"))
def login_success_data(request):  # 固定写法
    return request.param

# 登录失败前注册
@pytest.fixture()
def test_register_forloginfail(login_fail_data,url,db,baserequests):
    print(f"测试数据为：{login_fail_data['casedata']}")
    print(f"预期结果为为：{login_fail_data['expect']}")
    phone = login_fail_data['casedata']['mobilephone']
    # 初始化环境
    DbOp.deleteUser(db, phone)
    # 发送请求
    r = Member.register(url, baserequests, data=login_fail_data['casedata'])
    if r.json()['status'] == login_fail_data['expect']['status']:
        DbOp.deleteUser(db, phone)
        data = {"mobilephone":f"{phone}","pwd":"ceshizhuanyong001"}
        baserequests.post(url, data=data)
    yield
    DbOp.deleteUser(db, phone)

# 登录成功前注册
@pytest.fixture()
def test_register_forloginpass(login_success_data,url,db,baserequests):
    print(f"测试数据为：{login_success_data['casedata']}")
    print(f"预期结果为为：{login_success_data['expect']}")
    phone = login_success_data['casedata']['mobilephone']
    # 初始化环境
    DbOp.deleteUser(db, phone)
    # 发送请求
    r = Member.register(url, baserequests, data=login_success_data['casedata'])
    # 1.检查响应结果
    # assert r.json()['msg'] == success_data['expect']['msg']
    assert r.json()['status'] == login_success_data['expect']['status']
    assert r.json()['code'] == login_success_data['expect']['code']
    # 2. 检查实际有没有注册成功（1.查数据库，2.获取用户列表 3.用注册的用户登录）
    r = Member.getList(url,baserequests)
    assert phone in r.text
    yield
    DbOp.deleteUser(db, phone)

# 登录失败
def test_login_fail(test_register_forloginfail,login_fail_data,url,baserequests):
    print(f"测试数据为：{login_fail_data['casedata']}")
    print(f"预期结果为为：{login_fail_data['expect']}")
    # 发送请求
    r = Member.login(url,baserequests,data=login_fail_data['casedata'])
    # 检查结果
    assert r.json()['msg'] == login_fail_data['expect']['msg']
    assert r.json()['status'] == login_fail_data['expect']['status']
    assert r.json()['code'] == login_fail_data['expect']['code']

# 登录成功
def test_login_pass(test_register_forloginpass,login_success_data,url,baserequests):
    print(f"测试数据为：{login_success_data['casedata']}")
    print(f"预期结果为为：{login_success_data['expect']}")
    # 发送请求
    r = Member.login(url,baserequests,data=login_success_data['casedata'])
    # 检查结果
    # assert r.json()['msg'] == success_data['expect']['msg']
    assert r.json()['status'] == login_success_data['expect']['status']
    assert r.json()['code'] == login_success_data['expect']['code']