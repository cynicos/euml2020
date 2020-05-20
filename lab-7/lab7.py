# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:10:46 2020

@author: cynicos
"""


import pandas as pd
excel_file = 'file_example_XLS_10.xls'
people = pd.read_excel(excel_file)
print(people.head(10))
print("\n")

sorted_by_id = people.sort_values(['Id'], ascending=True)
print(sorted_by_id)
print("\n")


print("\n")

import matplotlib.pyplot as plt
#people["Age"].T.plot(kind='bar')
people["Age"].plot()

print("\n")

meanAge = people["Age"].mean()
print("საშუალო ასაკია ",meanAge)

modeAge = people["Age"].mode()
print("მოდა არის ",modeAge)

medianAge = people["Age"].median()
print("მედიანა არის ",medianAge)

maxAge = people["Age"].max()
print("მაქსიმალური ასაკია ",maxAge)

minAge = people["Age"].min()
print("მინიმალური ასაკია ",minAge)
