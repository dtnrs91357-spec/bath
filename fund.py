import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="root"
)

cur=conn.cursor()
cur.execute("create database if not exists bathDB")
cur.close()
conn.close()
print("接続完了")