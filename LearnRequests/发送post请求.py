'''
发送post请求
1. 使用data传表单格式的参数
2. 使用json传json格式的参数
3. 带请求头使用headers
'''
import requests

# 发送post请求，带参数时，可以用data或json来传参，具体使用哪个要系统怎么实现
# 注册成功手机号，登录 post
url = "http://jy001:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone": "15678945411", "pwd": "123456"}
canshu1 = [("mobilephone","15678945412"),("pwd","123456")]
r = requests.post(url, json=canshu)  # json 金融系统不支持json方式传参
print(r.text)

r = requests.post(url, data=canshu)  # 表单
r1 = requests.post(url, data=canshu1)
print(r.text)
print(r1.text)

# 发送请求到httpbin，观察区别
r = requests.post("http://httpbin.org/post",data=canshu) #"Content-Type": "application/x-www-form-urlencoded",
print(r.text)
r = requests.post("http://httpbin.org/post",json=canshu) #"Content-Type": "application/json",
print(r.text)
