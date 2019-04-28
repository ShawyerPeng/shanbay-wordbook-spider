import csv

l = []
with open("/Users/shawyerpeng/Downloads/Longman Communication 9000 from LDOCE6.txt", "rt") as f:
    # for line in csv.reader(f, dialect="excel-tab"): #You can also use delimiter="\t" rather than giving a dialect.
    for line in csv.reader(f, delimiter=' '):
        # csv内容读入列表l，每行为其一个元素，元素也为list
        l.append(line)

with open('/Users/shawyerpeng/Downloads/2333.txt', "w", encoding="utf-8") as f2:
    cw = csv.writer(f2)
    #采用writerow()方法
    for item in l:
       # 将列表的第一个元素写到txt文件的一行
        cw.writerow([item[0]])
        print(item[0])
   #或采用writerows()方法
   #cw.writerows(l) #将嵌套列表内容写入txt文件，每个外层元素为一行，每个内层元素为一个数据

# lol = list(csv.reader(open('/Users/shawyerpeng/Downloads/coca20000_collins.txt', 'rb'), delimiter='t'))
# d = dict()
# key = lol[6][0] # cell A7
# value = lol[6][3] # cell D7
# d[key] = value # add the entry to the dictionary


# https://cloud.tencent.com/developer/ask/32704