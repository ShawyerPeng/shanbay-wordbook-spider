import re
from collections import Counter

from nltk import FreqDist
from nltk.corpus import brown
from nltk import word_tokenize

word_data = ""
with open('/Users/shawyerpeng/Downloads/2333.txt', 'r') as fin:
    word_data += fin.read() + " "

# 保留顺序
nltk_tokens = word_tokenize(word_data)
ordered_tokens = set()
result = []
for word in nltk_tokens:
    if word not in ordered_tokens:
        ordered_tokens.add(word)
        result.append(word)
f2 = open("/Users/shawyerpeng/Downloads/final.txt", "w", encoding="utf-8")
for w in result:
    f2.writelines((w, "\n"))
f2.close

# 不保留顺序
# f2 = open("/Users/shawyerpeng/Downloads/1.txt", "w", encoding="utf-8")
# for word in S2:
#     f2.writelines((word, "\n"))
# f2.close

# https://www.yiibai.com/python_text_processing/python_filter_duplicate_words.html