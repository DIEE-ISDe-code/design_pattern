# -*- coding: utf-8 -*-
"""

"""

def f0():
    print('not found')

def f1():
    print('f1')


def f2():
    print('f2')

def f3():
    print('f3')

actions={1:f1, 2:f2, 3:f3}

v=int(input('insert a value:\n'))

f=actions.get(v,f0)
f()
