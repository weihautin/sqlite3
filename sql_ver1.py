#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


con = lite.connect('test.db')
import time



'''# 顯示sqlite的版本
with con:
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data  
'''


    
""" # 印出cars內容    
with con:    
        
    cur = con.cursor()    
    cur.execute("SELECT * FROM Cars")

    rows = cur.fetchall()

    for row in rows:
        print row
"""

""" # 建立Table,並且加入資料
with con:
    
    cur = con.cursor()    
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
    cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
    cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
    cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
    cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
    cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
    cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
    cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
"""
        
""" # 刪除原本car Table,並且重新建立           
cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)


con = lite.connect('test.db')

with con:
   
    cur = con.cursor()    
    
    cur.execute("DROP TABLE IF EXISTS Cars")
    cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)        
"""  
  
''' # 利用executescript來操作sqlite3資料庫    
try:
    con = lite.connect('test.db')

    cur = con.cursor()  

    cur.executescript("""
        DROP TABLE IF EXISTS Cars;
        CREATE TABLE Cars(Id INT, Name TEXT, Price INT);
        INSERT INTO Cars VALUES(1,'Audi',52642);
        INSERT INTO Cars VALUES(2,'Mercedes',57127);
        INSERT INTO Cars VALUES(3,'Skoda',9000);
        INSERT INTO Cars VALUES(4,'Volvo',29000);
        INSERT INTO Cars VALUES(5,'Bentley',350000);
        INSERT INTO Cars VALUES(6,'Citroen',21000);
        INSERT INTO Cars VALUES(7,'Hummer',41400);
        INSERT INTO Cars VALUES(8,'Volkswagen',21600);
        """)

    con.commit()
    
except lite.Error, e:
    
    if con:
        con.rollback()
        
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()
'''

'''
# 插入多個變數內容進入Table方法
con = lite.connect('test.db')
a = u"我聽你你你你"
b= 23
NULL='NULL'

#usr =('we4',123)
usr =(a, b)

with con:
    
    cur = con.cursor()    
    #    cur.execute("INSERT INTO qoo3(price) VALUES (?);",[b])
#    cur.execute("INSERT INTO qoo3(price) VALUES (%d);"% (b) )  
    #cur.execute("INSERT INTO qoo3(name,price) VALUES (%s,%d);"% (a,b) )  
    
    cur.execute("INSERT INTO qoo3(name, price) VALUES (?,?) ", usr )  
    
        #cur.execute("INSERT  INTO qoo3(price) VALUES (?);",[b])
    
    #cur.executemany("INSERT INTO qoo3(id,name,price) VALUES (NULL, ?, ?);",NULL,[a],[b])
    
    #cur.execute("INSERT INTO qoo3(id, name, price) VALUES (?,?,?);",[a],[b])
    #cur.execute("insert ignore into qoo3(id, name, price);",?[a],[b])
 

    lid = cur.lastrowid
    print "The last Id of the inserted row is %d" % lid
'''

'''
# 利用 fetchone()來擷取tables內的資料
con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM Cars")

    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break
            
        print row[0], row[1], row[2]
'''

'''
#使用 dictionary字典來擷取tables
con = lite.connect('test.db')    

with con:
    
    con.row_factory = lite.Row
       
    cur = con.cursor() 
    cur.execute("SELECT * FROM Cars")

    rows = cur.fetchall()

    for row in rows:
        print "%s %s %s" % (row["Id"], row["Name"], row["Price"])
'''






# 插入多個變數包含時間內容進入Table方法
con = lite.connect('test.db')
a = u"我聽你你你你"
b = 9999

with con:
    #CREATE TABLE qoo3(Id INTEGER PRIMARY KEY, Time TEXT ,Name TEXT, Price REAL, Volume REAL);
    
    cur = con.cursor() 
    
    timenow = datetime.datetime.now()
    
    year = str(timenow.year)
    month = str(timenow.month)
    day = str(timenow.day)
    hour = str(timenow.hour)
    minute = str(timenow.minute)

    now = year+'-'+month+'-'+day+' '+hour+':'+minute

    
#    cur.execute("SELECT strftime('%Y-%m-%d %H:%M','localtime')") #自訂時間格式
    
    
   

    usr = (now, a, b)

    cur.execute("INSERT INTO qoo3(Time, Name, price) VALUES (?,?,?) ", usr )  

    lid = cur.lastrowid
    print "The last Id of the inserted row is %d" % lid


    
    


    
    