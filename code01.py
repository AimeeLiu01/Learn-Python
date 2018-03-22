#!/usr/bin/python
# coding:utf8

a = 1.5 + 0.5j
print a.imag
print a.real

print 'C:\some\name'
print r'C:\some\name'

print 3 * 'un' + 'ium'

print 'Py' 'thon'
s = 'supercalifragilisticexpialidocious'
print len(s)


x = int(raw_input("Please enter an integer:"))
if x < 0:
    x = 0
    print 'Negative changed to zero'
elif x == 1:
    print 'Single'
elif x == 0:
    print 'Zero'
else:
    print 'More'


words = ['cats', 'window', 'defenestrate']
for w in words:
    print w, len(w)


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n/x
    else:
        print n, 'is a prime number'


def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print a
        a, b = b, a + b

fib(2000)



#------------------------------------------------#

a = [66.25, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.25), a.count('x')

print a.insert(2,-1)
a.append(333)
print a

print a.index(333)
print a.remove(333)
print a.reverse()
print a.sort()
print a.pop()
print a

