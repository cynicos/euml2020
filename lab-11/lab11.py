# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:09:03 2020

@author: cynicos
"""


import mysql.connector
# =============================================================================
# import random
# from random import randint
# import string
# 
# =============================================================================

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE numbers (number VARCHAR(255))")

sql = "INSERT INTO cars (car_num,) VALUES (%s)"

# =============================================================================
# randnum = [];
# for x in range(100):
#     ran=str(randint(100, 999));
#     randch1=str(''.join(random.choices(string.ascii_uppercase, k=3)))
#     randch2=str(''.join(random.choices(string.ascii_uppercase, k=3)))
#     rand=randch1+"-"+ran+"-"+randch2
#     randnum.append(rand)
#     
# print(randnum)
# print('xxxxxxxxxxxxxxxxxxxxxxxxx')
# res = [tuple(str(s) for s in i.split(',')) for i in randnum]
# print(res) 
# =============================================================================

val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")



