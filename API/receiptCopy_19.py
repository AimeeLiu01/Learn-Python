# !/usr/bin/python
# coding:utf-8
#通用票据识别
from aip import AipOcr
import json
import chardet


#定义常量
APP_ID = '15850686158'
API_KEY = '7209bfd2e0914fb5a3a6c7ca6573365a'
SECRET_KEY = '73d19039db7d46f18235475060f9d4ad'

#初始化AipOcr对象(AipOcr类提供给开发这一系列的图像识别方法)
aipOcr = AipOcr(APP_ID,API_KEY,SECRET_KEY)

#读取图片 使用with...as...能确保文件一定被关闭  read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有
def get_file_content(filePath):
    with open('C:\Users\I332487\Desktop\Train19.png', 'rb') as fp:
        return fp.read()

#定义参数变量
options = {

    #我们更改其默认的参数 查看其返回的参数
    'recognize_granularity':'small',
    'probability':'true',
    'accuracy':'normal',
}

#调用票据识别接口
result = aipOcr.receipt(get_file_content('C:\Users\I332487\Desktop\Train19.png'),options)

#将返回的json格式化输出
jsondata= json.dumps( result, ensure_ascii = False, indent = 4 ).encode('utf-8')

#打印出整个json结构
print jsondata

print '*******************************************************'
data = json.loads(jsondata)
#获取结果的行数
size = data['words_result_num']

#打印其中的words信息
for index in range(size):
   print index+1,' ',data['words_result'][index]['words']
