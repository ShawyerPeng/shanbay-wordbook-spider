import requests
import re
from lxml import html
 
file = open("/Users/shawyerpeng/Downloads/猴哥SAT词频8000.txt", "w", encoding="utf-8")

def spider(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    wordlist = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div/table/tbody/tr/td[1]/strong/text()')
    for word in wordlist:
        # print(word)
        file.writelines((word, "\n"))

url_list = []

domain = 'https://www.shanbay.com'
# 只需要修改这个URL
mainUrl = "https://www.shanbay.com/wordbook/97333"
mainPage = requests.get(mainUrl)
mainPageTree = html.fromstring(mainPage.content)

ele = mainPageTree.xpath('//*[@id="wordbook-wordlist-tmpl"]')
for e in ele:
    e.getparent().remove(e)

wordlist = mainPageTree.xpath('//*[@class="wordbook-wordlist-name"]/a/@href')
for wl in wordlist:
    url_list.append(domain + wl.strip(''))

# wordlist = re.findall(r'<td class="wordbook-wordlist-name">\s*<a href="(.*?)">(.*?)</a>\s*</td>', mainPage.text)
# for wl in wordlist:
#     url_list.append(domain + wl[0].strip(''))

# print(url_list)

for url in url_list:
    # print(url)
    everyPage = requests.get(url)
    everyPageTree = html.fromstring(everyPage.content)
    allCount = everyPageTree.xpath('//*[@id="wordlist-num-vocab"]/text()')
    # lxml 中的 xpath 方法，对于 xpath 表达式应该返回元素，总是返回一个数组，即使只有一个元素
    for count in allCount:
        # 该单元总单词数
        allCount = int(count)
        print(allCount)
        # 扇贝默认每页显示20个单词
        pageCount = int(allCount / 20) + 1
    for i in range(1, pageCount + 1):
        aurl = url + '?page=' + str(i)
        spider(aurl)

file.close()

def removedBooks(first_id, page_count):
    