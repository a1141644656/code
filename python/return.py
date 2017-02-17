import math
from collections import Iterable

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

def quadratic(a, b, c):
    if (b ** 2 - 4 * a * c) >= 0:
        s1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        s2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return s1, s2
    else:
        return None

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

def calc(*numbers):     # 可变参数
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, **kw):    #关键字参数
    print('name:', name, 'age:', age, 'other:', kw)
def person(name, age, *, city, job):
    print(name, age, city, job)


'''
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
'''

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)



# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n-1, a, c, b)
    print('move', a, '-->', c)
    move(n-1, b, a, c)


list(x for x in range(1, 100, 2) if x < 50)
list(range(1, 100, 2))


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


















