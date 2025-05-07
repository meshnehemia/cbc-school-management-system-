from database.config.connect import connection
class updateUsers:
    def __init__(self):
        pass
    class adminuser:
        def __init__(self):
            self.connection = connection()
            self.conn = self.connection.getconnection()
            self.cursor = self.conn.cursor()
        
        def updateadminHistory(self,activitytype,doneby,description):
            query= '''
                INSERT INTO historyactivityadmins(activity_type,doneby,description) 
                VALUES (%s,%s,%s)
            '''
            values = (activitytype,doneby,description)
            try:
                self.cursor.execute(query,values)
                self.conn.commit()
                print(f'✅ activity {description} updated successfully')
                return True, f'✅ {description} updated successfully'
            except Exception as e:
                print(f'❌❌ error {e}')
                return False, f'❌❌ error {e}'

        
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
            
        def addadmin(self,first_name,second_name,last_name,gender,email,phone_number,password,profile_picture,ts_number,id_number,active_status="active"):
            try:
                query = '''
                        INSERT INTO admin(first_name,second_name,last_name,gender,email,phone_number,password,profile_picture,tsc_number,id_number,active_status)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        '''
                values = (first_name,second_name,last_name,gender,email,phone_number,password,profile_picture,ts_number,id_number,active_status)
                self.cursor.execute(query,values)
                self.conn.commit()
                print(f'✅ admin inserted successfully')
                return True, '✅ admin inserted successfully'
            except Exception as e:
                print(f'❌❌ error {e}')  
                return False, f'❌❌ error {e}'
            
        def addteacher(self,first_name,second_name,last_name,gender,level,email,phone_number,password,profile_picture,ts_number,id_number,active_status="active"):
            try:
                query = '''
                        INSERT INTO teachers(first_name,second_name,last_name,gender,level,email,phone_number,password,profile_picture,tsc_number,id_number,active_status)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        '''
                values = (first_name,second_name,last_name,gender,level,email,phone_number,password,profile_picture,ts_number,id_number,active_status)
                self.cursor.execute(query,values)
                self.conn.commit()
                print(f'✅ teacher inserted successfully')
                return True, '✅ teacher inserted successfully'
            except Exception as e:
                print(f'❌❌ error {e}')  
                return False, f'❌❌ error {e}'
        def addstudent(self,first_name,second_name,last_name,gender,grade,email,phone_number,ups_number,password,profile_picture,active_status="active"):
            try:
                query = '''
                        INSERT INTO students(first_name,second_name,last_name,gender,grade,email,phone_number,password,profile_picture,ups_number,active_status)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        '''
                values = (first_name,second_name,last_name,gender,grade,email,phone_number,password,profile_picture,ups_number,active_status)
                self.cursor.execute(query,values)
                self.conn.commit()
                print(f'✅ student inserted successfully')
                return True, '✅ student inserted successfully'
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