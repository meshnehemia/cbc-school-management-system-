from flask import json
from database.config.connect import connection
class selectusers:
    def __init__(self):
        pass
    class adminuser:
        def __init__(self):
            self.connection = connection()
            self.conn = self.connection.getconnection()
            self.cursor = self.conn.cursor()
        def login(self,email,password):
            query = ''' 
                        SELECT * FROM admin WHERE email = %s AND password = %s
                    '''
            values = (email,password)
            try:
                self.cursor.execute(query,values)
                result = self.cursor.fetchone()
                if result:
                    print(f'✅ login successful')
                    return True,'✅ login successful',list(result)
                else:
                    print(f'❌❌ invalid credentials')
                    return False, '❌❌ invalid credentials',{'email':email,'password':password}
            except Exception as e:
                print(f'❌❌ error {e}')
                return False, f'❌❌ error {e}'
        def lastseen(self, id):
            query = ''' 
                        SELECT last_login FROM admin WHERE id = %s
                    '''
            values = (id,)
            try:
                self.cursor.execute(query,values)
                result = self.cursor.fetchone()
                if result:
                    print(f'✅ last seen retrieved successfully')
                    return True, '✅ last seen retrieved successfully', result
                else:
                    print(f'❌❌ no record found')
                    return False, '❌❌ no record found'
            except Exception as e:
                print(f'❌❌ error {e}')
                return False, f'❌❌ error {e}'
        def details(self,id):
            query = ''' 
                        SELECT * FROM admin WHERE id = %s
                    '''
            values = (id,)
            try:
                self.cursor.execute(query,values)
                result = self.cursor.fetchone()
                if result:
                    print(f'✅ details retrieved successfully')
                    return True, '✅ details retrieved successfully', result
                else:
                    print(f'❌❌ no record found')
                    return False, '❌❌ no record found'
            except Exception as e:
                print(f'❌❌ error {e}')
                return False, f'❌❌ error {e}'
        def alladmins(self):
            query = ''' 
                        SELECT * FROM admin
                    '''
            try:
                self.cursor.execute(query)
                result = self.cursor.fetchall()
                if result:
                    print(f'✅ all admins retrieved successfully')
                    return True, '✅ all admins retrieved successfully', result
                else:
                    print(f'❌❌ no record found')
                    return False, '❌❌ no record found'
            except Exception as e:
                print(f'❌❌ error {e}')
                return False, f'❌❌ error {e}'