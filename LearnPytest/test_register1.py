import pytest,requests

# @pytest.fixture(params=[
#     {"casedata":{"mobilephone":"1801234567","pwd":"123456","regname":"hello"},"expect":{"status":"0","code":"20109","data":None,"msg":"手机号码格式不正确"}},
#     {"casedata":{"mobilephone":"13712345678","pwd":"123","regname":"aaa"},"expect":{"status":"0","code":"20108","msg":"密码长度必须为6~18"}},
#     {"casedata":{"mobilephone":"13424455688","pwd":"123456","regname":"aaa"},"expect":{"status":"1","code":"10001","msg":"注册成功"}}])
@pytest.fixture(params=[{'casedata': {'mobilephone': '1801234567', 'pwd': '123456', 'regname': 'hello'}, 'except': {'status': '0', 'code': '20109', 'data': None, 'msg': '手机号码格式不正确'}}, {'casedata': {'mobilephone': '13712345678', 'pwd': '123', 'regname': 'aaa'}, 'except': {'status': '0', 'code': '20108', 'msg': '密码长度必须为6~18'}}, {'casedata': {'mobilephone': '13224495288', 'pwd': '123456', 'regname': 'aaa'}, 'except': {'status': '1', 'code': '10001', 'msg': '注册成功'}}])
def data(request):
    return request.param



def test_register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data['casedata'])
    print(r.json()['msg'])
    print(data['except']['msg'])
    assert r.json()['msg'] == data['except']['msg']
    assert r.json()['code'] == data['except']['code']