# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:18:28 2020

@author: cynicos
"""
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
import random
import string
from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="quiz"
)


#    დავალება N1 & N2

mycursor = mydb.cursor()
sql = "INSERT INTO students (personal_id, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

random_ids = []
rand_times =[]
spent_time_in_week = []
ids = []
i=0
while i < 100:
    rand_id = random_with_N_digits(9)
    if rand_id not in random_ids:
        random_ids.append(rand_id)
        ids.append(rand_id)
        for x in range(7):
            rand_t = round(random.uniform(0, 5), 2)
            random_ids.append(rand_t)
            rand_times.append(round(rand_t))
        i += 1
      

n = 8 
m = 7
  
# using list comprehension 
final = [random_ids[i * n:(i + 1) * n] for i in range((len(random_ids) + n - 1) // n )]  
final_t = [rand_times[i * m:(i + 1) * m] for i in range((len(rand_times) + m - 1) // m )] 

res = [tuple(i) for i in final]

#print(res)

print("####################################\n\n")

print(final_t)

print("####################################\n\n")

print(ids)

print("####################################\n\n")


# დავალება N3

spent_time_in_week=[sum(rand_times[x:x+7]) for x in range(0, len(rand_times), 7)]
print(spent_time_in_week)
print("\n\n####################################\n\n")

plt.scatter(ids, spent_time_in_week)
plt.show()


# დავალება N4

average_spent_time = np.mean(spent_time_in_week)
print("საშუალოდ კვირაში სტუდენტი ხარჯავს " + str(average_spent_time) + "-საათს")
standard_deviation = round(np.std(spent_time_in_week),2)
print("სტანდარტული გადახრა უდრის " + str(standard_deviation) + "-ს")

print("\n\n####################################\n\n")

#  დავალება N5

average_spent_time_in_day = [];

for i in range(100):
    average_spent_time_in_day.append(round(spent_time_in_week[i]/7))

x = np.percentile(average_spent_time_in_day, 70)

print(x)
print("\n\n####################################\n\n")

# =============================================================================
# val = res
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")
# =============================================================================



# =============================================================================
# mycursor.execute("SELECT * FROM students")
# myresult = mycursor.fetchall()
# for item in myresult:
#   print(item)
# =============================================================================

