from database.config.connect import connection
class updateUsers:
    def __init__(self):
        pass
    class adminuser:
        def __init__(self):
            self.connection = connection()
            self.conn = self.connection.getconnection()
            self.cursor = self.conn.cursor()
        
        def lastseenupdate(self,id):
            query = ''' 
                        update admin set last_login = CURRENT_TIMESTAMP where id = %s
                    '''
            values = (id,)
            try:
                self.cursor.execute(query,values)
                self.conn.commit()
                print(f'✅ last seen updated successfully')
                return True, '✅ last seen updated successfully'
            except Exception as e:
                print(f'❌❌ error {e}')
                return False, f'❌❌ error {e}'
            
        def adduser(self,first_name,second_name,last_name,email,phone_number,password,profile_picture,ts_number,id_number,active_status="active"):
            try:
                query = '''
                        INSERT INTO admin(first_name,second_name,last_name,email,phone_number,password,profile_picture,tsc_number,id_number,active_status)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        '''
                values = (first_name,second_name,last_name,email,phone_number,password,profile_picture,ts_number,id_number,active_status)
                self.cursor.execute(query,values)
                self.conn.commit()
                print(f'✅ user inserted successfully')
                return True, '✅ user inserted successfully'
            except Exception as e:
                print(f'❌❌ error {e}')  
                return False, f'❌❌ error {e}'

        def deletadmin(self,id):
            query = ''' 
                        DELETE FROM admin WHERE id = %s
                    '''
            values = (id,)
            try:
                self.cursor.execute(query,values)
                self.conn.commit()
                print(f'✅ user deleted successfully')
                return True, '✅ user deleted successfully'
            except Exception as e:
                print(f'❌❌ error {e}')
                return False, f'❌❌ error {e}'
        def updatedetails(self,id,first_name,second_name,last_name,email,phone_number,profile_picture,ts_number,id_number,active_status="active"):
            query = '''
                        UPDATE admin SET first_name = %s, second_name = %s, last_name = %s, email = %s, phone_number = %s, profile_picture = %s, tsc_number = %s, id_number = %s, active_status = %s WHERE id = %s
                    '''
            values = (first_name,second_name,last_name,email,phone_number,profile_picture,ts_number,id_number,active_status,id)
            try:
                self.cursor.execute(query,values)
                self.conn.commit()
                print(f'✅ user updated successfully')
                return True, '✅ user updated successfully'
            except Exception as e:
                print(f'❌❌ error {e}')
                return False, f'❌❌ error {e}'
        def updatedateleft(self,id):
            query = ''' 
                        update admin set date_left = CURRENT_TIMESTAMP where id = %s
                    '''
            values = (id,)
            try:
                self.cursor.execute(query,values)
                self.conn.commit()
                print(f'✅ date left updated successfully')
                return True, '✅ date left updated successfully'
            except Exception as e:
                print(f'❌❌ error {e}')
                return False, f'❌❌ error {e}'
    def teachers(self):
        pass
    def finance(self):
        pass
    def students(self):
        pass