#!/usr/bin/env python
# -*- coding: utf-8 -*-
file = input('Название файла:\n')
print('\nНазвание введенного вами файла: ')
print(file)
one = open(file, 'r', encoding='utf-8')
print('\nТекст, находящийся в файле:\n ')
print(one.read())
one.close()
two = open(file, 'r', encoding='utf-8')
string = ""
while 1:
    line = two.readline()
    if not line: break
    string += line
two.close()
print('\nДеление текста на предложения и подсчет слов в каждом из них:\n ')
import re
pattern = re.compile(r'([А-ЯA-Z]((т.п.|т.д.|пр.|г.)|[^!.\(]|\([^\)]*\))*[.!])')
a = 0
sum=[]
for i, sent in enumerate(pattern.findall(string)):
    print('[{}]{}'.format(i + 1, sent[0]))
    a = a + 1
    s=re.sub(r'[^\w\s]','',sent[0])
    res=len(s.split())
    sum+=[res]
    print('В предложении '+ str(res) + ' слов(а).\n')
print('Количество предложений в тексте: ' + str(a))
print('\nКоличество слов в каждом предложении:\n')
from itertools import groupby
c=[]
for j in range(len(sum)):
   c+=[{' количество': sum[j]}]
r=groupby(sorted(c,key=lambda x: x[' количество']),lambda x: x[' количество'])
for k,g in r:
    print(str(k) + ' слов(a) в ' + str(len(list(g))) + ' предложении(ях).')



