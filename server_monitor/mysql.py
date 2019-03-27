#!/usr/bin/python
#coding: UTF-8
import MySQLdb


db_config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'passwd': 'Cao8992908@xing',
        'db': 'RUNOOB',
        'use_unicode': 0, 
        'charset': 'utf8'
    }
db = MySQLdb.connect(**db_config)
cursor = db.cursor()
cursor.execute("select * from runoob_tbl")
data = cursor.fetchone()
print db.character_set_name()
res = []
for i in range (0,len(data)):
 print data[i]
 res.append(str(data[i]))
print res
result = (",".join(res))
print result
db.close
