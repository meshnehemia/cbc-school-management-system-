from flask import jsonify, request, session, render_template, redirect, url_for
from database.databaseinsert.userinsertion import updateUsers
from werkzeug.utils import secure_filename
import uuid, os
from database.databaseretrivals.getuser import selectusers
from database.databaseretrivals.getactivities import Activities
from database.databaseretrivals.getteachers import teachers
from database.databaseretrivals.getstudent import students
def admin(app):
    @app.route('/admin')
    def admindashboard():
        if session.get('type') == 'admin':
            updateUsers().adminuser().lastseenupdate(session['id'])
            details = {
                'first_name': session.get('first_name'),
                'second_name': session.get('second_name'),
                'last_name': session.get('last_name'),
                'email': session.get('email'),
                'phone_number': session.get('phone_number'),
                'profile_picture': session.get('profile_picture'),
                'tsc_number': session.get('tsc_number')
            }
            history = []
            teachers_number = 0
            students_number = 0
            
            adminstatus, adminmessage, adminshistory = Activities().getAdminHistory()
            otherstatus, othermessage, othershistory = Activities().teachersHistory()
            if adminstatus:
                history = adminshistory
                
            if otherstatus:
                history.append(othershistory)
            print(history)
            teachersstates , teachersmessage , teachersnum = teachers().teachersCount()
            if teachersstates:
                teachers_number = teachersnum
            print(teachers_number)
            studentStatus, studentmessage,studentsnumber = students().studentsCount()
            if studentStatus:
                students_number = studentsnumber
            print(students_number)
            
            
            return render_template('index.html' , details=details, history= history , students_number=students_number, teachers_number=teachers_number)
        return redirect(url_for('login'))
    @app.route('/studentsmanagement')
    def studentsmanagement():
        if session.get('type') == 'admin':
            updateUsers().adminuser().lastseenupdate(session['id'])
            allstudents = []
            status, message, getstudents = students().allStudents()
            if status:
                allstudents = getstudents
            else:
                allstudents = "no student"
            print(allstudents)
            return render_template("studentsadmin.html", allstudents = allstudents)
        return redirect(url_for('login'))

    @app.route('/perfomance')
    def studentperfomancemanagement():
        if session.get('type') == 'admin':
            updateUsers().adminuser().lastseenupdate(session['id'])
            return render_template('studentperfomanceadmin.html')
        return redirect(url_for('login'))

    @app.route('/teachersManagement')
    def teachersManagement():
        if session.get('type') == 'admin':
            updateUsers().adminuser().lastseenupdate(session['id'])
            teachersavailable = []
            tstatus, tmessage, tavailable = teachers().allTeachers()
            if tstatus:
                teachersavailable = tavailable
            else:
                teachersavailable = "no teachers registed"
            print(teachersavailable)
            active_teachers = [teacher for teacher in teachersavailable if teacher[13] == 'active']
            onleave_teachers = [teacher for teacher in teachersavailable if teacher[13] == 'onleave']
            notactive_teachers = [teacher for teacher in teachersavailable if teacher[13] != 'active' and teacher[13] != 'onleave']
            return render_template('teachersavailable.html', 
                                   allteachers=teachersavailable,
                                   active_teachers = active_teachers,
                                   onleave_teachers = onleave_teachers,
                                    notactive_teachers = notactive_teachers
                                    )
        return redirect(url_for('login'))

    @app.route('/studentsattendance')
    def studentsattendance():
        if session.get('type') == 'admin':
            updateUsers().adminuser().lastseenupdate(session['id'])
            return render_template('attendancemarking.html')
        return redirect(url_for('login'))

    @app.route('/curriculum')
    def admincurriculum():
        if session.get('type') == 'admin':
            updateUsers().adminuser().lastseenupdate(session['id'])
            return render_template("admincurriculum.html")
        return redirect(url_for('login'))

    @app.route('/reports')
    def adminreports():
        if session.get('type') == 'admin':
            updateUsers().adminuser().lastseenupdate(session['id'])
            return render_template('adminreports.html')
        return redirect(url_for('login'))

    @app.route('/assessments')
    def assessment():
        if session.get('type') == 'admin':
            updateUsers().adminuser().lastseenupdate(session['id'])
            return render_template('assessments.html')
        return redirect(url_for('login'))

    @app.route('/finances')
    def finances():
        if session.get('type') == 'admin':
            updateUsers().adminuser().lastseenupdate(session['id'])
            return render_template('finances.html')
        return redirect(url_for('login'))
    
    @app.route('/addstudent', methods=['GET', 'POST'])
    def addstudent():
        if session.get('type') == 'admin':
            updateUsers().adminuser().lastseenupdate(session['id'])
            if request.method == 'POST':
                data = request.form
                first_name = data["first_name"]
                second_name = data["second_name"]
                grade = data["grade"]
                last_name = data["last_name"]
                gender = data["gender"]
                email = data["email"]
                ups_number = data["upa"]
                phone_number = data["phone_number"]
                password = data["password"]
                active_status = data["active_status"]

                # Handle image upload
                profile_picture = request.files.get('profile_picture')
                image_name = ''
                if profile_picture and profile_picture.filename != '':
                    ext = profile_picture.filename.rsplit('.', 1)[-1].lower()
                    image_name = f"{uuid.uuid4().hex}.{ext}"
                    image_path = os.path.join('static/images/profile_images', image_name)
                    os.makedirs(os.path.dirname(image_path), exist_ok=True)
                    profile_picture.save(image_path)
                else:
                    image_name ="default.png"
                # Save to DB with image_name
                adminus = updateUsers()
                addnewstudent = adminus.adminuser()
                status, message = addnewstudent.addstudent(
                    first_name, second_name, last_name, gender,
                    grade, email, phone_number, ups_number,
                    password, image_name, active_status
                )

                if status:
                    updateUsers().adminuser().updateadminHistory(
                        "newstudent", session['id'],
                        f"student {first_name} {last_name} has been registered"
                    )
                    return {'status': True, 'message': 'Student added'}
                else:
                    return {'status': False, 'message': message}

            return render_template('addstudent.html')
        return redirect(url_for('login'))

    @app.route('/addteacher', methods=['GET', 'POST'])
    def addteacher():
        if session.get('type') == 'admin':
            updateUsers().adminuser().lastseenupdate(session['id'])

            if request.method == 'POST':
                data = request.form

                # Get form data
                first_name = data["first_name"]
                second_name = data["second_name"]
                last_name = data["last_name"]
                level = data["level"]
                gender = data["gender"]
                email = data["email"]
                phone_number = data["phone_number"]
                password = data["password"]
                tsc_number = data["tsc_number"]
                id_number = data["id_number"]
                active_status = data["active_status"]

                # ✅ Handle profile picture
                profile_picture = request.files.get("profile_picture")
                filename = "default.png"
                if profile_picture and profile_picture.filename != "":
                    filename = secure_filename(profile_picture.filename)
                    upload_folder = os.path.join('static', 'images', 'profile_images')
                    os.makedirs(upload_folder, exist_ok=True)
                    filepath = os.path.join(upload_folder, filename)
                    profile_picture.save(filepath)

                # Save to DB
                adminuser = updateUsers().adminuser()
                status, addt = adminuser.addteacher(
                    first_name, second_name, last_name, gender, level,
                    email, phone_number, password, filename,  # only filename, path handled in template
                    tsc_number, id_number, active_status
                )

                if status:
                    updateUsers().adminuser().updateadminHistory(
                        "newteacher", session['id'],
                        f"Teacher {first_name} {last_name} has been registered"
                    )
                    return jsonify({"status": True, "message": "Successfully added new teacher", "data": addt})
                else:
                    return jsonify({"status": False, "message": "Failed to add new teacher", "data": addt})

            return render_template('addteacher.html')
        return redirect(url_for('login'))
    
    @app.route('/getstudentsbyfilter', methods=['POST'])
    def studentfilter():
        data = request.form
        grade = data['grade']
        gender = data['gender']
        status = data['status']
        status, message, values = students().filterstudent(grade,gender,status)
        if status:
            student = values
        else:
            student= "no student available"
        return jsonify(student)
    @app.route('/getstudentbyups', methods=['POST'])
    def getstudentbyid():
        data = request.form
        ups = data['ups']
        status, message, values =students().filterups(ups)
        if status:
            student = values
        else:
            student= "no student available"
        return jsonify(student)
    @app.route('/getsteachersbyfilter', methods=['POST'])
    def getteacherfilter():
        data = request.form
        grade = data['grade']
        status = data['status']
        status, message, values = teachers().filter(grade,status)
        if status:
            teachersf = values
        else:
            teachersf= "no student available"
        return jsonify(teachersf)
        
    @app.route('/getteachersbyts', methods = ['POST'])
    def getteacherbyts():
        data = request.form
        ts = data['ts']
        status, message, values = teachers().searchtsnumber(ts)
        if status:
            teachersf = values
        else:
            teachersf= "no student available"
        return jsonify(teachersf)

    # @app.route('/insertadmin')
    # def insertadmin():
    #     newadmin = updateUsers()
    #     addnewadmin = newadmin.adminuser()
    #     adduser = addnewadmin.addadmin('joshua','james','micky',"male'josh@gmail.com','+254757316903',1234,'133878734424447098.jpg','ts12743','12436493')
    #     return jsonify(adduser)
    
def adminlogin(email,password):
        databaseretrival = selectusers()
        adminuser = databaseretrival.adminuser()
        login , message , user = adminuser.login(email,password)
        return login, message, user