# 开始联系request
import requests

headers = {
'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

}
url = 'https://www.douban.com'
response = requests.get(url,headers=headers)
print(response.status_code)
print(response.text)