# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:32:11 2020

@author: cynicos
"""

#task-1

import random



# =============================================================================
# def sumOfDigits(x) : 
#     sum = 0
#     while (x != 0) : 
#         sum = sum + x % 10
#         x   = x // 10
#       
#     return sum
# 
# dicts = {}
# keys = [random.randrange(1,100) for i in range(10)]
# for i in keys:
#         dicts[i] = sumOfDigits(i)
#         
# print(dicts)
# =============================================================================

#task-2

# =============================================================================
# lis = [random.randrange(5,15) for i in range(20)]
# print(lis)
# print("მოდა არის - ", max(set(lis), key=lis.count))
# unic=set(lis)
# print(unic)
# 
# repeated = {i:lis.count(i) for i in lis}
# for i in repeated:
#      print(i, "შეგვხვდა", repeated[i],"- ჯერ")
# =============================================================================


#task-3

chars="აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ"
lis= []
L={}
for i in range(20):
    lis.append(''.join(random.choices(chars, k=random.randrange(5,15)))) 

for x in lis:
  cnt=x.count('ა')+x.count('ე')+x.count('ი')+x.count('ო')+x.count('უ')
  if cnt not in L.keys():
    L[cnt]=[]
  L[cnt].append(x)
print("ყველაზე მეტ ხმოვანს შეიცავს - ",L[max(L.keys())])








