'''
上传文件 ，一般都是post接口 ,files参数上传文件
'''
import requests

url = "http://www.httpbin.org/post"
'''
files参数，字典的格式，'name':file-tuple
file-tuple可以是2-tuple('filename', fileobj),3-tuple('filename', fileobj, 'content_type'),4-tuple('filename', fileobj, 'content_type', custom_headers)
'''
with open("d:/test.txt", encoding='utf-8') as f:
    # "text/plain" 如果上传时一个文本文件，可以去掉content_type,默认文件时文本文件。
    file = {"file1": ("test.txt", f, "text/plain")}  # MIME类型 text/plain，image/png,image/gif,application/json
    r = requests.post(url, files=file)
    print(r.text)
    # \u53ef\u601c\u65e0 Unicode编码的，网上有Unicode转中文，中文转Unicode的小工具，可以在线转

# 上传一个图片文件，10k以内
with open("D:/test.PNG", mode='rb') as p:
    file = {"file2": ("test.PNG", p, "image/png")}
    r = requests.post(url, files=file)
    print(r.text)

# 可以一次上传多个文件
with open("d:/test.txt", encoding='utf-8') as f:
    with open("D:/test.PNG", mode='rb') as p:
        file = {"file1": ("test.txt", f, "text/plain"), "file2": ("test.PNG", p, "image/png")}
        r = requests.post(url, files=file)
        print(r.text)
