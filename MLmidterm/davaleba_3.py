# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:29:41 2020

@author: cynicos
"""


import random
M=int(input("შეიყვანეთ M: "))
N=int(input("შეიყვანეთ N: "))

Matrix = [[0 for x in range(M)] for y in range(N)] 

for i in range(len(Matrix)) :  
    for j in range(len(Matrix[i])) : 
        if(i==0):
            Matrix[i][j]=random.randrange(1, 10)
        else:
            Matrix[i][j]=Matrix[i-1][j]*2
        print(Matrix[i][j], end=" ") 
    print()  