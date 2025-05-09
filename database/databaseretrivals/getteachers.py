from flask import json
from database.config.connect import connection
class teachers:
    def __init__(self):
        self.connection = connection()
        self.conn = self.connection.getconnection()
        self.cursor = self.conn.cursor()
   
    def teachersCount(self):
        query = ''' 
                SELECT Count(*) from teachers;
                '''
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            if result:
                print(f'✅ NUMBER OF TEACHERS RETRIVED successfully')
                return True, '✅ NUMBER OF TEACHERS retrived successfully', result
            else:
                print(f' no record found')
                return False, '❌❌ no record found',"NO RECORDS"
        except Exception as e:
            print(f'❌❌ error {e}')
            return False, f'❌❌ error {e}',"NO RECORDS"
    def allTeachers(self):
        query = ''' 
                SELECT * FROM teachers;
                '''
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            if result:
                print(f'✅ all  teachers retrieved successfully')
                return True, '✅ all teachers retrieved successfully', result
            else:
                print(f'❌❌ no record found')
                return False, '❌❌ no record found' , 'NO RECORDS'
        except Exception as e:
            print(f'❌❌ error {e}')
            return False, f'❌❌ error {e}'
    def filter(self, grade, status):
        query = ''' 
                SELECT * FROM teachers WHERE status = %s AND grade = %s;
                '''
        try:
            values = (grade, status)
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            if result:
                print(f'✅ All teachers retrieved successfully')
                return True, '✅ All teachers retrieved successfully', result
            else:
                print(f'❌❌ No record found')
                return False, '❌❌ No record found', 'NO RECORDS'
        except Exception as e:
            print(f'❌❌ Error: {e}')
            return False, f'❌❌ Error: {e}'

    def searchtsnumber(self, tsnumber):
        query = ''' 
                SELECT * FROM teachers WHERE ts_number LIKE %s;
                '''  # Use LIKE if you're searching for a partial match
        try:
            values = (tsnumber + '%',)  # Add '%' for partial match (e.g., starts with)
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            if result:
                print(f'✅ Teachers retrieved successfully')
                return True, '✅ Teachers retrieved successfully', result
            else:
                print(f'❌❌ No record found')
                return False, '❌❌ No record found', 'NO RECORDS'
        except Exception as e:
            print(f'❌❌ Error: {e}')
            return False, f'❌❌ Error: {e}'
