import mysql.connector
class config:
    def __init__(self):
        self.databasehost='127.0.0.1'
        self.databaseuser = 'root'
        self.databasepassword=''
        self.databasename='cbcmanagement'
        print(f"✅ configurations initialized call connect functions to connect")
    def connect(self):
        try:
            connection = mysql.connector.connect(
                host=self.databasehost,
                user = self.databaseuser,
                password=self.databasepassword
            )
            if connection.is_connected():
               cursor = connection.cursor()
               cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.databasename}")
               print("✅ database created successfully")
               cursor.execute(f"USE {self.databasename}")
               print(f"✅ using {self.databasename}")
            else:
               print("❌❌ not connected")
        except Exception as e:
            print("❗❗ error occured", e)
    def connection(self):
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
    def tableAdmin(self):
        query= '''
                    CREATE TABLE IF NOT EXISTS admin(
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        first_name VARCHAR(100) NOT NULL,
                        second_name VARCHAR(100),
                        last_name VARCHAR(100) NOT NULL,
                        email VARCHAR(100) NOT NULL UNIQUE,
                        phone_number VARCHAR(100) NOT NULL,
                        password VARCHAR(100) NOT NULL,
                        profile_picture text,
                        date_registered TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        tsc_number VARCHAR(100),
                        id_number INT,
                        active_status VARCHAR(100),
                        last_login TIMESTAMP NULL DEFAULT NULL,
                        date_left TIMESTAMP NULL DEFAULT NULL
                    );
                '''
        try:
            connection = self.connection()
            if connection.is_connected():
                cursor = connection.cursor()
                print(f"✅ ready to insert admin table")
                cursor.execute(query)
                print(f"✅ table admin created successfully")
                connection.close()
            else:
                print(f"⚠ ⚠ not connected ")
        except Exception as e:
            print("❗❗ error occured", e)



create = config()
create.connect()
create.tableAdmin()