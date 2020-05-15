# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:14:35 2020

@author: cynicos
"""

str2=""
inp = str(input("შეიყვანეთ სიტყვები ;-ით გამოყოფილი: "))
strs = inp.split(";")
for i, s in enumerate(strs):
    strs[i]="".join(sorted(strs[i], reverse = True))
str2 =";".join(strs)
print(str2)


