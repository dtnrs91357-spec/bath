import mysql.connector

print("aaa")

def db_create():
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
    return print("接続完了")
db_create()

def db_connect():
    con=mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="root",
        database="bathDB"
    )
    cur=con.cursor()
    return con,cur

def table_create():
    con,cur=db_connect()
    sql_account="""
        create table if not exists account(
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        familypass VARCHAR(255) NOT NULL
        )
    """
    cur.execute(sql_account)
    print("アカウントテーブル完了")

    sql_bath_status="""
        create table if not exists bath_status(
        familypass VARCHAR(255) PRIMARY KEY,
        status VARCHAR(10) NOT NULL,
        username VARCHAR(50) NOT NULL
        )
    """
    cur.execute(sql_bath_status)
    print("お風呂状態完了")

    sql_bath_log="""
        create table if not exists bath_log(
        familypass VARCHAR(255) PRIMARY KEY,
        status VARCHAR(10) NOT NULL,
        username VARCHAR(50) NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    cur.execute(sql_bath_log)
    print("お風呂ログ完了")

    con.commit()
    print("テーブル完了")
    cur.close()
    con.close()
table_create()