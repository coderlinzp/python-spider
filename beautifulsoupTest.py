import requests
from bs4 import BeautifulSoup
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/54.0.2840.99 Safari/537.36'}  #给请求指定一个请求头来模拟chrome浏览器
web_url = 'https://unsplash.com/photos/cm0eSVxdLDg'
r = requests.get(web_url,  headers=headers)
all_img = BeautifulSoup(r.text, 'lxml').find_all('img', class_= '_2zEKz')
floder_path = 'D:\BeautifulPicture'
path = 'E:/python/img.jpg'
for img in all_img:
    print('图片url:', img['src'])
    source = requests.request('get', img['src'])
    with open(path,'wb') as f: #wb二进制写操作权限
        f.write(source.content)
    f.close()



# def mkdir(self, path):
#     path = path.strip()
#     isExists = os.path.exists(path)
#     if not isExists:
#         print('创建名字叫做', path, '的文件夹')
#         os.makedirs(path)
#         print('创建成功！')
#     else:
#         print(path, '文件夹已经存在了，不再创建')
#
# def save_img(self, url, name):
#     print('开始保存图片...')
#     img = self.request(url)
#     file_name = name + '.jpg'
#     print('开始保存文件')
#     f = open(file_name, 'ab')
#     f.write(img.content)
#     print(file_name, '文件保存成功！')
#     f.close()