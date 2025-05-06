import mysql.connector
class connection:
    def __init__(self):
        self.databasehost='127.0.0.1'
        self.databaseuser = 'root'
        self.databasepassword=''
        self.databasename='cbcmanagement'
        print(f"✅ configurations initialized call connection functions to connect")
    def getconnection(self):
        try:
            connection = mysql.connector.connect(
                host=self.databasehost,
                user = self.databaseuser,
                password=self.databasepassword,
                database = self.databasename
            )
            if connection.is_connected():
                print(f"✅ ready to execute")
                return connection
        except Exception as e:
            print("❗❗ error occured", e)