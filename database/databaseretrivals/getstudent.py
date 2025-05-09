from flask import json
from database.config.connect import connection
class students:
    def __init__(self):
        self.connection = connection()
        self.conn = self.connection.getconnection()
        self.cursor = self.conn.cursor()
   
    def studentsCount(self):
        query = ''' 
                SELECT Count(*) from students;
                '''
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            if result:
                print(f'✅ NUMBER OF STUDENTS RETRIVED successfully')
                return True, '✅ NUMBER OF STUDENTS retrived successfully', result
            else:
                print(f' no record found')
                return False, '❌❌ no record found',"NO RECORDS"
        except Exception as e:
            print(f'❌❌ error {e}')
            return False, f'❌❌ error {e}',"NO RECORDS"
    def allStudents(self):
        query = ''' 
                SELECT * FROM students;
                '''
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            if result:
                print(f'✅ all  students retrieved successfully')
                return True, '✅ all students retrieved successfully', result
            else:
                print(f'❌❌ no record found')
                return False, '❌❌ no record found' , 'NO RECORDS'
        except Exception as e:
            print(f'❌❌ error {e}')
            return False, f'❌❌ error {e}','error'
        
    def filterstudent(self, grade, gender, status):
        query = ''' 
                SELECT * FROM students WHERE active_status = %s AND grade = %s AND gender = %s;
                '''
        try:
            values = (status, grade, gender)
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            if result:
                print(f'✅ All students retrieved successfully')
                return True, '✅ All students retrieved successfully', result
            else:
                print(f'❌❌ No record found')
                return False, '❌❌ No record found', 'NO RECORDS'
        except Exception as e:
            print(f'❌❌ Error: {e}')
            return False, f'❌❌ Error: {e}'


    def filterups(self, ups):
        query = ''' 
                SELECT * FROM students WHERE ups_number LIKE %s;
                '''  # Use LIKE if you're searching for a partial match
        try:
            values = (ups + '%',)  # Add '%' to ups for partial match (starts with)
            self.cursor.execute(query, values)
            result = self.cursor.fetchall()
            if result:
                print(f'✅ UPS records retrieved successfully')
                return True, '✅ UPS records retrieved successfully', result
            else:
                print(f'❌❌ No record found')
                return False, '❌❌ No record found', 'NO RECORDS'
        except Exception as e:
            print(f'❌❌ Error: {e}')
            return False, f'❌❌ Error: {e}'
