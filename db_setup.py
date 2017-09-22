import pymsysql
import dbconfig
connection = pymsql.connect(host='localhost', user=dbconfig.db_user, passwd=dbconfig.password)

try:
    with connection.cursor() as cursor:
        sql = "CREATE DATABASE IF NOT EXISTS crimemap"
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes(
id int NOT NULL AUTO_INCREMENT,
latitude FLOAT(10,6),
longitude FLOAT(10,6),
date DATETIME,
category VARCHAR(50),
description VARCHAR(255),
updated_at TIMESTAMP,
PRIMARY KEY (id)
)"""
         cursor.execute(sql)
     connection.commit()
     connection.close()
