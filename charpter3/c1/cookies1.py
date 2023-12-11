# cookie:爬虫维持登陆状态的机制
import http.cookiejar,urllib.request
# cookie = http.cookiejar.CookieJar() # 声明cookiejar的对象,存放cookie的容器
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.zhihu.com')
# for item in cookie:
#     print(item.name + '=' + item.value)
#******************************************************8
# filename = 'cookies.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# 生成LWPcookiejar类型的文件
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.zhihu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)
# 将文件写入cookies.txt文件中
# import os
#
# filename = 'cookies.txt'
# path = os.path.abspath(filename)
# print(path)
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookies.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.zhihu.com')
print(response.read().decode('utf-8'))