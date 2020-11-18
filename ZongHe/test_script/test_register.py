'''
注册的测试脚本（pytest)
'''
import pytest

from ZongHe.caw import DataRead
from ZongHe.baw import Member, DbOp
from ZongHe.caw.BaseRequests import BaseRequests
from ZongHe.caw.DataRead import readini

# 测试前置：获取测试数据，数据是列表，通过readyaml读取来的
from ZongHe.test_script.conftest import baserequests


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_fail.yaml"))
def fail_data(request):  # 固定写法
    return request.param

@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_success.yaml"))
def success_data(request):  # 固定写法
    return request.param

@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_repeat.yaml"))
def repeat_data(request):  # 固定写法
    return request.param

# 注册失败
def test_register_fail(fail_data,url,baserequests):
    print(f"测试数据为：{fail_data['casedata']}")
    print(f"预期结果为为：{fail_data['expect']}")
    # 发送请求
    r = Member.register(url,baserequests,data=fail_data['casedata'])
    # 检查结果
    assert r.json()['msg'] == fail_data['expect']['msg']
    assert r.json()['status'] == fail_data['expect']['status']
    assert r.json()['code'] == fail_data['expect']['code']

# 注册成功
def test_register_pass(success_data,url,db,baserequests):
    print(f"测试数据为：{success_data['casedata']}")
    print(f"预期结果为为：{success_data['expect']}")
    phone = success_data['casedata']['mobilephone']
    # 初始化环境
    DbOp.deleteUser(db, phone)
    # 发送请求
    r = Member.register(url, baserequests, data=success_data['casedata'])
    # 1.检查响应结果
    assert r.json()['msg'] == success_data['expect']['msg']
    assert r.json()['status'] == success_data['expect']['status']
    assert r.json()['code'] == success_data['expect']['code']
    # 2. 检查实际有没有注册成功（1.查数据库，2.获取用户列表 3.用注册的用户登录）
    r = Member.getList(url,baserequests)
    assert phone in r.text
    # 清理环境，根据手机号删除注册用户
    DbOp.deleteUser(db, phone)

# 重复注册
def test_register_repeat(repeat_data):
    print(repeat_data['casedata'])
    print(repeat_data['expect'])