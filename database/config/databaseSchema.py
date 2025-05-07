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
                        gender  VARCHAR(100),
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
                print(f"✅ ready to admin admin table")
                cursor.execute(query)
                print(f"✅ table admin created successfully")
                connection.close()
            else:
                print(f"⚠ ⚠ not connected ")
        except Exception as e:
            print("❗❗ error occured while creating table admin", e)

    def teacherstable(self):
        query ='''
                    CREATE TABLE IF NOT EXISTS teachers(
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        first_name VARCHAR(100) NOT NULL,
                        second_name VARCHAR(100),
                        level VARCHAR(100),
                        gender  VARCHAR(100),
                        last_name VARCHAR(100) NOT NULL,
                        email VARCHAR(100) NOT NULL UNIQUE,
                        phone_number VARCHAR(100) NOT NULL,
                        password VARCHAR(100) NOT NULL,
                        profile_picture text,
                        date_registered TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        tsc_number VARCHAR(100),
                        id_number INT,
                        active_status VARCHAR(100),
                        last_login TIMESTAMP NULL DEFAULT NULL
                    );

                '''
        try:
            connection = self.connection()
            if connection.is_connected():
                cursor = connection.cursor()
                print(f"✅ ready to create  table teachers")
                cursor.execute(query)
                print(f"✅ table teachers created successfully")
                connection.close()
            else:
                print(f"⚠ ⚠ not connected ")
        except Exception as e:
            print("❗❗ error occured while creating table teachers", e)

    def studentstable(self):
        query ='''
                    CREATE TABLE IF NOT EXISTS students(
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        first_name VARCHAR(100) NOT NULL,
                        second_name VARCHAR(100),
                        grade VARCHAR(100),
                        last_name VARCHAR(100) NOT NULL,
                        gender  VARCHAR(100),
                        email VARCHAR(100) NOT NULL UNIQUE,
                        ups_number VARCHAR(100),
                        phone_number VARCHAR(100) NOT NULL,
                        password VARCHAR(100) NOT NULL,
                        profile_picture text,
                        date_registered TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        active_status VARCHAR(100),
                        last_login TIMESTAMP NULL DEFAULT NULL
                    );

                '''
        try:
            connection = self.connection()
            if connection.is_connected():
                cursor = connection.cursor()
                print(f"✅ ready to create  table students")
                cursor.execute(query)
                print(f"✅ table students created successfully")
                connection.close()
            else:
                print(f"⚠ ⚠ not connected ")
        except Exception as e:
            print("❗❗ error occured while creating table students", e)

    def historyactivityteachers(self):
        query='''
                    CREATE TABLE IF NOT EXISTS historyactivity(
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        activity_type VARCHAR(100) NOT NULL,
                        doneby INT,
                        description VARCHAR(100) NOT NULL, 
                        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (doneby) REFERENCES teachers(id) ON DELETE CASCADE ON UPDATE CASCADE 
                    );
                '''
        try:
            connection = self.connection()
            if connection.is_connected():
                cursor = connection.cursor()
                print(f"✅ ready to create  table teachers history")
                cursor.execute(query)
                print(f"✅ table teachershistory created successfully")
                connection.close()
            else:
                print(f"⚠ ⚠ not connected ")
        except Exception as e:
            print("❗❗ error occured while creating table students", e)
        
        
    def historyactivityadmin(self):
        query='''
                    CREATE TABLE IF NOT EXISTS historyactivityadmins(
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        activity_type VARCHAR(100) NOT NULL,
                        doneby INT,
                        description VARCHAR(100) NOT NULL, 
                        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (doneby) REFERENCES admin(id) ON DELETE CASCADE ON UPDATE CASCADE
                    );
                '''
        try:
            connection = self.connection()
            if connection.is_connected():
                cursor = connection.cursor()
                print(f"✅ ready to create  table admin history")
                cursor.execute(query)
                print(f"✅ table admins history created successfully")
                connection.close()
            else:
                print(f"⚠ ⚠ not connected ")
        except Exception as e:
            print("❗❗ error occured while creating table students", e)



create = config()
create.connect()
create.tableAdmin()
create.teacherstable()
create.studentstable()
create.historyactivityadmin()
create.historyactivityteachers()