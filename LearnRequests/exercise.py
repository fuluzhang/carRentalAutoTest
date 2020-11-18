import requests
url = "http://jy001:8081/futureloan/mvc/api/member/login"
canshu = {"mobilephone":"18066668888888","pwd":"abcd_123"}
r = requests.post(url, data=canshu)  # json 金融系统不支持json方式传参
print(r.text)