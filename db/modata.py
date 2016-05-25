# -*- coding: utf-8 -*-
import sqlite3
# connect to SQLite database, and the database file name is xjdata.db
# if not existed, will auto create one under current directory
conn = sqlite3.connect('testCase.db')
# create one Cursor
cursor = conn.cursor()

#删除表
# cursor.execute('drop table request')

# curroles = "ssssssss"
# cursor.execute("update role set rolename = ? where id =1", (curroles,))
# cursor.execute('select rolename from role')
# values = cursor.fetchall()
# print values
# cursor.execute('select * from user where name=? and pwd=?', ('abc', '123456'))

# cursor.execute('select data from depdata')
# values = cursor.fetchall()
# data1 = values[0]
# data2 = values[1]
# data3 = values[2]
# print data1, data2, data3
# print '############################'
# cursor.execute("select data from cartdata")
# values = cursor.fetchall()
# data1 = values[0][0]
# data2 = values[1][0]
# data3 = values[2][0]
# # print type(data)
# print data1,data2,data3

cursor.execute('create table appneed (id varchar(20) primary key, appneeded varchar(20))')
cursor.execute('insert into appneed (id, appneeded) values (\'1\',\'Y\')')
# ,data2, data3
# # 查看当前所有表
# cursor.execute('select name from sqlite_master where type="table"')
# values = cursor.fetchall()
# print values

cursor.close()
# commit 
conn.commit()
# close conn
conn.close()
