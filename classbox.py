from mysql.connector import pooling

class DatabaseManager:
    pool = pooling.MySQLConnectionPool(
        pool_name = "mypool",
        pool_size = 5,
        host = "localhost",
        port = "3306",
        user = "root",
        password = "root",
        database = "bathdb"
        )
    
    def __init__(self):
        self.con = DatabaseManager.pool.get_connection()
        self.cursor = self.con.cursor()

    def sql_account(self,username):
        sql = """
            select password
            from account
            where username = %s
        """
        self.cursor.execute(sql,(username,))
        result = self.cursor.fetchall()

        if len(result) == 0:
           return None
        
        return result[0][0]
    
    def sql_new_account(self,username,pswd):
        sql = """
            insert into account values(%s,%s)
        """
        self.cursor.execute(sql,(username,pswd))
        self.cursor.commit()
    
    def close(self):
        self.cursor.close()
        self.con.close()


class Login:
    def __init__(self,username,pswd):
        self.username = username
        self.pswd = pswd

    def login(self):
        db = DatabaseManager()
        corerect_pswd = db.sql_account(self.username)
        db.close()

        if corerect_pswd is None:
            return False
        return self.pswd == corerect_pswd


# 新規登録の時にファミリーIDを自動生成・誰かのファミリーIDに加入→updata
    def login_new(self):
        db = DatabaseManager()
        same_pswd = db.sql_account(self.username)
        db.close()

        if self.pswd != same_pswd:
            db.sql_new_account(self.username,self.pswd)
            db.close()
            answer = True
        else:
            answer = False

        return answer
