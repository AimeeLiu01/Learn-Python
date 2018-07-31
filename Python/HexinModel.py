#!/usr/bin/python
# -*- coding: UTF-8 -*-#

# 使用apply函数
def function(a,b):
    print a,b

apply(function, (1, 2+3))
apply(function, ('whither','canda?'))

apply(function, ("crunchy",), {"b": "frog"})
apply(function, (), {"a":"crunchy", "b":"frog"})


## 使用__import__函数加载模块
import glob, os
modules = []
for module_file in glob.glob("*-plugin.py"):
    try:
        module_name, ext = os.path.splitext(os.path.basename(module_file))
        module = __import__(module_name)
        modules.append(module)
    except ImportError:
        pass # ignore broken modules

# say hello to all modules
for module in modules:
    module.hello()




# 1.2.3 关于名称空间
# dir返回由给定模块、类、实例、或其他类型的所有成员组成的列表

def dump(value):
    print value, "=>", dir(value)

import sys
dump(0)
dump(1.0)
dump([])
dump({})
dump("string")
dump(len)
dump(sys)


## 使用dir函数查找类的所有成员
class A:
    def a(self):
        pass
    def b(self):
        pass

class B(A):
    def c(self):
        pass
    def d(self):
        pass


def getmembers(klass, members=None):
    # get a list of all class members, ordered by class
    if members is None:
        members = []
    for k in klass.__bases__:
        getmembers(k, members)
    for m in dir(klass):
        if m not in members:
            members.append(m)
    return members

print getmembers(A)



# 使用vars函数
book = "library2"
pages = 250
scripts = 350

print "the %(book)s book contains more than %(scripts)s scripts" % vars()


# python是一种动态类型语言 这意味着一个定变量名可以在不同的场合绑定到不同的类型上
def function(value):
    print value

function(1)
function(1.0)
function("one")


## 使用type函数
def dump(value):
    print type(value), value

dump(1)
dump(1.0)
dump("one")


##  使用callable函数
def dump(function):
    if callable(function):
        print function, "is callable"
    else:
        print function, "is not callable"

print "---------------------------------------"

class A:
    def method(self, value):
        return value

class B(A):
    def __call__(self, value):
        return value

a = A()
b = B()

dump(0)
dump("string")
dump("callable")
dump(dump) #function

dump(A) # calsses
dump(B)
dump(B.method)

dump(a) # instances
dump(b)
dump(b.method)

## 使用issubclass 函数
class A:
    pass

class B:
    pass

class C(A):
    pass

class D(A, B):
    pass

def dump(object):
    print object, "=>",
    if issubclass(object, A):
        print "A",
    if issubclass(object, B):
        print "B",
    if issubclass(object, C):
        print "C"
    if issubclass(object, D):
        print "D"
    print

dump(A)
dump(B)
dump(C)
dump(D)


# 计算Python表达式
def dump(expression):
    result = eval(expression)
    print expression, "=>", result, type(result)

dump("1")
dump("1.0")
dump("'string'")
dump("1.0 + 2.0")
dump("'*' * 10")
dump("len('world')")


# 使用eval函数执行任意命令
print eval("__import__('os').getcwd()")

#  简单的代码生成工具
import sys, string
class CodeGeneratorBackend:
    "Simple code generator for Python"

    def begin(self, tab="\t"):
        self.code = []
        self.tab = tab
        self.level = 0

    def end(self):
        self.code.append("") # make sure there's a newline at the end
        return compile(string.join(self.code, "\n"), "<code>", "exec")

    def write(self, string):
        self.code.append(self.tab * self.level + string)

    def indent(self):
        self.level = self.level + "hi"

print CodeGeneratorBackend()

print "---------------------------"


# 1.4 os模块 这个模块大部分函数通过对应平台相关模块实现 比如posix 和 nt.os 模块会在第一次导入的时候自动加载合适的执行模块

import os
import string

def replace(file, search_for, replace_with):
    # replace strings in a text file
    back = os.path.splitext(file)[0] + ".bak"
    temp = os.path.splitext(file)[0] + ".tmp"
    try:
        os.remove(temp)
    except os.error:
        pass

    fi = open(file)
    fo = open(temp, "w")


# 使用 os列出目录下的文件
import os
for file in os.listdir("/Users/liuchang/PycharmProjects"):
    print file

print "----------------------------"


# 使用os模块来调用其他程序
import os
import sys
def run(program, *args):
    pid = os.fork()
    if not pid:
        os.execvp(program, (program,) + args)
    return os.wait()[0]
run("python", "hello.py")
print "goodbye"


# 搜索文件系统
import os
def callback(arg, directory, files):
    for file in files:
        print os.path.join(directory, file), repr(arg)

os.path.walk(".", callback, "secret message")

print "------------------------------"
# 使用os.listdir搜索文件系统
def index(directory):
    stack = [directory]
    files = []
    while stack:
        directory = stack.pop()
        for file in os.listdir(directory):
            fullname = os.path.join(directory, file)
            files.append(fullname)
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)
    return files

for file in index("."):
    print file

# 1.8 re模块
# 模块提供了一系列功能强大的正则表达式工具 他们允许你快速检查给定字符串是否与给定的模式匹配，或者包含这个模式
# 正则表达式是以紧凑的语法写出来的字符串模式


