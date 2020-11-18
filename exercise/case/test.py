import pytest,requests
from exercise.base.util import GetExcelData

@pytest.fixture(params=GetExcelData().load(r'D:\ApiAutoTest\exercise\data\data.xlsx','Sheet1'))
def data(request):
    return request.param



def test_register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data['casedata'])
    print(r.json()['msg'])
    print(data['except']['msg'])
    assert r.json()['msg'] == data['except']['msg']
    assert r.json()['code'] == data['except']['code']