import requests
import re
from lxml import html
 
file = open("/Users/shawyerpeng/Downloads/纽约时报一万常用高频词.txt", "w", encoding="utf-8")

def spider(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    wordlist = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div/table/tbody/tr/td[1]/strong/text()')
    for word in wordlist:
        # print(word)
        file.writelines((word, "\n"))

domain = 'https://www.shanbay.com'
# 只需要修改这个URL
bookName = "纽约时报一万常用高频词"
bookId = 171586
firstId = 460096
pages = 46
mainUrl = "https://www.shanbay.com/wordlist/" + str(bookId) + "/"

url_list = []

index = firstId
while index <= firstId + (pages - 1) * 3:
    url = mainUrl + str(index)
    index += 3
    print(url)
    everyPage = requests.get(url)
    everyPageTree = html.fromstring(everyPage.content)

    is404 = everyPageTree.xpath('/html/body/div[3]/div[1]/div/h1/text()')
    if (len(is404) != 0):
        break

    wordbook_contains_this_wordlist = everyPageTree.xpath('/html/body/div[3]/div/div[1]/div[1]/div/div/div[3]/p/a[1]')
    if len(wordbook_contains_this_wordlist) == 0:
        pages += 1
        continue
    else:
        # if wordbook_contains_this_wordlist
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
    