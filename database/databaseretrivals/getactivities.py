from flask import json
from database.config.connect import connection
class Activities:
    def __init__(self):
        self.connection = connection()
        self.conn = self.connection.getconnection()
        self.cursor = self.conn.cursor()
   
    def getAdminHistory(self):
        query = ''' 
                SELECT h.activity_type, h.description, h.time ,
                a.first_name, a.second_name FROM historyactivityadmins AS h 
                INNER JOIN admin as a  where h.doneby = a.id  LIMIT 20;
                '''
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            if result:
                print(f'✅ ADMIN HISTORY RETRIEVED  successfully')
                return True, '✅ admin history has been retrived successfully', result
            else:
                print(f' no record found')
                return False, '❌❌ no record found',"NO RECORDS"
        except Exception as e:
            print(f'❌❌ error {e}')
            return False, f'❌❌ error {e}',"NO RECORDS"
    def teachersHistory(self):
        query = ''' 
                SELECT h.activity_type, h.description, h.time ,
                a.first_name, a.second_name FROM historyactivity AS h 
                INNER JOIN teachers as a  where h.doneby = a.id  LIMIT 20;
                '''
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            if result:
                print(f'✅ all  other history retrieved successfully')
                return True, '✅ all other history retrieved successfully', result
            else:
                print(f'❌❌ no record found')
                return False, '❌❌ no record found' , 'NO RECORDS'
        except Exception as e:
            print(f'❌❌ error {e}')
            return False, f'❌❌ error {e}'