import bs4
import requests
from bs4 import  BeautifulSoup
import lxml
import warnings
warnings.filterwarnings("ignore")
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" id = "p" value="p标签"s><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, 'lxml')  #声明BeautifulSoup对象
# print(soup)
print("------------------------")
find = soup.find('p')
print(type(find))
print(find)
print(find)
print(find.name)#标签对象名字
print(find['value'])#用于获取标签内属性值
print(find.string) #标签内的html.Text()文本内容
print(soup.find_all('a'))#获得所有a标签
print(soup.find(id = "1"))#查找id为xx的标签
print(soup.get_text())#从文档中获取所有文字内容:
print("------------------------------------")

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup2 = BeautifulSoup(markup)
comment = soup2.b.string
if type(comment) == bs4.element.Comment:#比较对象
    print("这是注释")
else:
    print("不是注释")

print("-------------------------------------------")
#对标签子节点循环
head_tag = soup.head
print(head_tag.children)

for child in soup.body.children:
    print(child)




