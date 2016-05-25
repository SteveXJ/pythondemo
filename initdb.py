# -*- coding: utf-8 -*-

import sqlite3
# import TS_Catalogue.test as test

#GLOBAR VAR
import setting

#init db
def init():
    # create one Cursor
    cursor = setting.DB_CONN.cursor()
    # create user table: Store your mail and password
    cursor.execute('create table user (id varchar(20) primary key, pw varchar(20))')
    cursor.execute('insert into user (id, pw) values (\'xxjxu@cn.ibm.com\', \'xxxx\')')
    # create cartdata table: The data of Catalogue Workflow
    cursor.execute('create table cartdata (id varchar(20) primary key, data varchar(20))')
    cursor.execute('insert into cartdata (id, data) values (\'1\',\'ifd_LicencetoRequest-13431\')')
    cursor.execute('insert into cartdata (id, data) values (\'2\',\'ifd_LicencetoRequest-13381\')')
    cursor.execute('insert into cartdata (id, data) values (\'3\',\'ifd_LicencetoRequest-13434\')')
    # create depdata table: The data of Deployment Workflow
    cursor.execute('create table depdata (id varchar(20) primary key, data varchar(20))')
    cursor.execute('insert into depdata (id, data) values (\'1\',\'ifd_LicencetoDeploy-13431\')')
    cursor.execute('insert into depdata (id, data) values (\'2\',\'ifd_LicencetoDeploy-13381\')')
    cursor.execute('insert into depdata (id, data) values (\'3\',\'ifd_LicencetoDeploy-13434\')')
    # create request table: Store the docid of the request
    cursor.execute('create table request (id varchar(20) primary key, requestid varchar(20))')
    cursor.execute('insert into request (id, requestid) values (\'1\', \'1\')')
    # create role table: Store the create role and used in TC_Creator_AskForAm_Amend_SubtoApp.py file
    cursor.execute('create table currentrole (id varchar(20) primary key, rolename varchar(20))')
    cursor.execute('insert into currentrole (id, rolename) values (\'1\',\'Cat\')')
    # create appneed table: Store the value of "Approver needed" about approver
    cursor.execute('create table appneed (id varchar(20) primary key, appneeded varchar(20))')
    cursor.execute('insert into appneed (id, appneeded) values (\'1\',\'Y\')')
    # close cursor
    cursor.close()
    # commit
    setting.DB_CONN.commit()

if __name__ == '__main__':
    setting.init()
    init()
