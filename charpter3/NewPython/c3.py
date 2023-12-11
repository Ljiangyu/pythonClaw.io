import requests
url = 'https://item.jd.com/100075799817.html?bbtf=1#comment'
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
response = requests.get(url,headers=header)
print(response.text.json())