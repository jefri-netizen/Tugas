# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 18:42:38 2019

@author: Faris Fatin 32
"""
i=0
npm = input("NPM: ")
while i<1:
    if len(npm)<7:
        print("npm kurang dari 7")
        npm = input("NPM: ")
    elif len(npm)>7:
        print("npm lebih dari 7")
        npm = input("NPM: ")
    else:
        i=1
        
a=npm[0]
b=npm[1]
c=npm[2]
d=npm[3]
e=npm[4]
f=npm[5]
g=npm[6]


for x in a,b,c,d,e,f,g:
    if int(x) > 1:
        for i in range(2,int(x)):
            if (int(x)) % i == 0:
                break
            else:
                print(int(x),end ="")