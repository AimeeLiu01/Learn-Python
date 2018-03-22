#!/usr/bin/python
# -*- coding: UTF-8 -*-#

import this
import keyword
print keyword.kwlist
import csv

path_read = '.csv'
path_write = '.csv'

# 从文件中抽取数据
f = open(path_read, 'r')
reader = csv.reader(f)
content = []
for con in reader:
    content.append(con)
f.close()

# 对Legendary变量下的每个数值进行判断
content_new = [content[0]]

for con in content[1:]:
    if con[-1] == str('True'):
        content_new.append(con)

print content_new[0]
print content_new[1]


# -----------------------------------------------------
#  读取文件中的数据
path = 'Pokemon.txt'
f = open(path, 'r')
content = f.readlines()
f.close()
print content[0]
print content[1]

content_new = []
for con in content:
    tmp = con.strip() # 去除换行符
    tmp = tmp.split('\t') # 以'\t'的方式对字符串进行分隔、并返回一个列表
    content_new.append(tmp)
print content_new[0]
print content_new[1]

## 将数据写入文件
path = 'Pokemon_write.txt'
#写入Pokemon的前两行数据
content = [['#','Name','Type 1', 'Type 2'],
           ['1','Bulbasuea','Grass','Poison']]

# 循环content中的内容
for con in content:
    con = '\t'.join(con) # 是用.join（）将列表中的每个数值用'\t'联合组成一个字符串
    con = con + '\r\n' # 每行后添加换行符、如果是Linux系统 则换成'\n'
    f.write(con)
f.close()

print '-------------------------------------'

# 读取 引入CSV模块
import csv
path = 'Pokemon.csv'
f = open(path, 'r')
reader = csv.reader(f) # 用csv.reader()方法生成reader对象
content = [] # 用于数据存储

for con in reader:
    content.append(con)
f.close()

print content[0]
print content[1]


print '-------------------------------------'

# 写入 引入CSV模块
import csv
path = 'Pokemon_write.csv'

# 写入Pokemon前两行数据
content = [['#','Name','Type 1', 'Type 2'],
           ['1','Bulbasuea','Grass','Poison']]

f = open(path, 'w')
writer = csv.writer(f) # 生成writer对象对存储
# for循环、逐个对内容写入文件中
for con in content:
    writer.writerow(con)

f.close()

