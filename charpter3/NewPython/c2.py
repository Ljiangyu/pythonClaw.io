import requests
url = 'http://httpbin.org/post'
data={
    'wd':'python'
}
response = requests.post(url,data=data)
response.encoding='utf-8'
print(response.text)