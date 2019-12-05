#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class A:
    def collaborate_with(self,v):
        if type(v)==A:
            print ('class A with class A')
        if type(v)==B:
            print ('class A with class B')
        


class B:
    def collaborate_with(self,v):
        if type(v)==A:
            print ('class B with class A')
        if type(v)==B:
            print ('class B with class B')
        

a1=A()
a2=A()
b1=B()
b2=B()

a1.collaborate_with(a2)
a1.collaborate_with(b1)
b1.collaborate_with(a2)
b1.collaborate_with(b2)