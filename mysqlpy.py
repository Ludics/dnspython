#!/usr/bin/env python
# coding=utf-8

import pymysql

db = pymysql.connect(host="127.0.0.1", user="root", passwd="ludics", db="dnsdata")
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

# sql = "INSERT INTO query(domainName, resolverAddr, aNum) \
#         VALUES ('%s', '%s', '%d')" % ('tikishi.cn', '9.9.9.9', 1)

# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()

sql = "UPDATE query SET aaaaNum = '%d' WHERE queryID = '%d'" % (1,1)

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

# new_id = cursor.lastrowid

# sql = "INSERT INTO a_record (queryID, domainName, \
#         resolverAddr, ttl, addr)  VALUES \
#         ('%d', '%s', '%s', '%d', '%s')" % \
#         (new_id, 'tikishi.cn', '9.9.9.9', 600, '211.159.174.23')

# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()      
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print("Database version: %s" % data)

# cursor.execute("select * from query")
# row_1 = cursor.fetchone()
# print(row_1['domainName'])

db.commit()
cursor.close()
db.close()
