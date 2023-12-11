from urllib import request,error
try:
    reponse = request.urlopen('http://cuiqingcai.com/t1.txt')
except error.URLError as e:
    print(e.reason)