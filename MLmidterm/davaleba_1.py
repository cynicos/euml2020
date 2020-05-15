# -*- coding: utf-8 -*-
"""
Created on Fri May 15 11:14:34 2020

@author: cynicos
"""
arr = []
arr2 = []
for num in range(1,500):
  if num > 1:
    for i in range(2,num):
      if (num % i) == 0:
        break
    else:
      arr.append(num)
for i in arr:
	j = i * 7
	if j<3000:
		arr2.append(j)
print (arr2)

