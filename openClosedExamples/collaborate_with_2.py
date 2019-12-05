#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class A:
    def collaborate_with(self,v):
        v.collaborate_with_A(self)
        
    def collaborate_with_A(self,v):
        print ('class A with class A')

    def collaborate_with_B(self,v):
        print ('class B with class A')

         

class B:
    def collaborate_with(self,v):
        v.collaborate_with_B(self)

    def collaborate_with_A(self,v):
        print ('class A with class B')

    def collaborate_with_B(self,v):
        print ('class B with class B')


a1=A()
a2=A()
b1=B()
b2=B()

a1.collaborate_with(a2)
a1.collaborate_with(b1)
b1.collaborate_with(a2)
b1.collaborate_with(b2)