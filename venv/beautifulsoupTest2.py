import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/54.0.2840.99 Safari/537.36'}  #给请求指定一个请求头来模拟chrome浏览器
web_url = 'http://v.baidu.com/channel/short/tiyu'
r = requests.get(web_url, headers=headers)
soup = BeautifulSoup(r.text,'html')
print(soup)

# all_vedio = BeautifulSoup(r.text, 'lxml').find_all('object')
# for vedio in all_vedio:
#     print(vedio)