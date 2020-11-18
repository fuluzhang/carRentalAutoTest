'''
pytest命名规则：
1. 测试文件以test_开头或结尾
2.测试类以Test开头
3.测试方法/测试函数以test_开头
'''
import  requests

def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data)
    return r

# 手机号码格式不正确
def test_register_001():
    # 测试数据
    data = {"mobilephone":"1801234567","pwd":"123456","regname":"hello"}
    # 预期结果
    expect = {"status":"0","code":"20109","data":None,"msg":"手机号码格式不正确"}
    # 测试步骤
    real = register(data)
    # 检查结果

    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']
    pass

# 密码过短
def test_register_002():
    data = {"mobilephone":"13712345678","pwd":"123","regname":"aaa"}
    expect = {"status":"0","code":"20108","msg":"密码长度必须为6~18"}
    real = register(data)
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']
    pass

# 注册名过长
def test_register_003():
    data = {"mobilephone":"13742445679","pwd":"123456","regname":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}
    expect = {"status":"0","code":"20102","msg":"服务器异常"}
    real = register(data)
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']
    pass

# 注册成功
def test_register_004():
    data = {"mobilephone":"13414345688","pwd":"123456","regname":"aaa"}
    expect = {"status":"1","code":"10001","msg":"注册成功"}
    real = register(data)
    assert real.json()['msg'] == expect['msg']
    assert real.json()['code'] == expect['code']
    pass

