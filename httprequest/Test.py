# coding=utf-8
import time
from Common.LogConfig import *
#sum = 0
#for x in range(101):
#    sum = x + sum
#    print sum
#print abs(-100)
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print b
        a,b=b,a+b
        n=n+1
    return 'done'

print(fib(5))

def ftb(max):
    n,a,b=0,0,1
    while n<max:
        print b
        t=(b,a+b)
        a=t[0]
        b=t[1]
        n=n+1
    return 'done'

print(ftb(5))

def fpb(max):
    n,a,b=0,0,1
    while n<max:
        print b
        a=1
        b=a+b
        n=n+1
    return 'done'

print(fpb(5))

print(time.time())
print(time.localtime(time.time()))
print time.strftime("%Y%m%d%H%M%S_", time.localtime())
logging.debug('你好')