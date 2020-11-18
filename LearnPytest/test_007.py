'''
1.接口测试场景比较难模拟，需要大量的工作才能完成
2.需要第三方的接口，但是第三方的接口没有开发完成
测试环境不充分的情况下，怎么去做接口测试？使用Mock来模拟。
'''
import requests
import mock

class Alipay:
    def zhifu(data):
        # 接口功能尚未开发完成
        # 接口地址，ger/post,入参，返回值已经定义好，有对应的文档接口
        # 接口参数："OrderId":"1231345646","Amount":128.5,"Type":"支付宝"
        # 接口返回值："code":200,"msg":"支付成功" 201 支付失败 202 支付超时
        r = requests.post("http://zhifubao.com/pay",data=data).json()
        return r

class Jinrong:
    def chongzhi(self,data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/recharge",data=data).json()
        return r
    def quxian(self,data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/withdraw",data=data).json()
        return r

class TestMock:
    def test_alipay(self):
        # 对要模拟的类创建一个对象
        aliPay = Alipay()
        # 模拟zhifu的返回值为{"code":200,"msg":"支付成功"}
        aliPay.zhifu = mock.Mock(return_value={"code":200,"msg":"支付成功"})
        # 调用zhfu接口
        data = {"OrderId":"1231345646","Amount":128.5,"Type":"支付宝"}
        r = aliPay.zhifu(data)
        print(r)

class TestjinRong:
    def test_quxian(self):
        jinrong = Jinrong()
        c = {"mobilephone":13712345678,"amount":1000}
        r = jinrong.chongzhi(c)
        assert r['msg'] == "充值成功"
        assert r['status'] == 1
        assert r['code'] == '10001'


        jinrong.quxian = mock.Mock(return_value={"status":"1","code":"10001","msg":"取现成功"})
        data = {"mobilephone":"13712345678","amount":500}
        r = jinrong.quxian(data)
        assert r['msg'] == "取现成功"
        assert r['status'] == "1"
        assert r['code'] == '10001'
