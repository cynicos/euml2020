# -*- coding: utf-8 -*-
"""
Created on Fri May 15 12:14:35 2020

@author: cynicos
"""

li2=[]
strs = ['ab','aba','aaaa','aaaaa']
for i in strs:
    li2.append(strs[i].join(sorted(strs[1], reverse = True)))


res = ''.join(sorted(strs[1], reverse = True)) 
print(strs)