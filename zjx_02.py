# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 08:42:44 2017

@author: Administrator
"""

#赋值语句x,y,z=1,2,3会在x,y,z中分别赋什么值？
x,y,z=1,2,3
print('x=',x)
print('y=',y)
print('z=',z)

#执行z,x,y=y,z,x后，x,y,z中分别含什么值？
z,x,y=y,z,x
print('x=',x)
print('y=',y)
print('z=',z)