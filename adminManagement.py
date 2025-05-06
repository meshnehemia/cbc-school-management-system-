from flask import jsonify, session, render_template, redirect, url_for
from database.databaseinsert.userinsertion import updateUsers
from database.databaseretrivals.getuser import selectusers
def admin(app):
    @app.route('/admin')
    def admindashboard():
        if session.get('type') == 'admin':
            details = {
                'first_name': session.get('first_name'),
                'second_name': session.get('second_name'),
                'last_name': session.get('last_name'),
                'email': session.get('email'),
                'phone_number': session.get('phone_number'),
                'profile_picture': session.get('profile_picture'),
                'tsc_number': session.get('tsc_number')
            }
            return render_template('index.html' , details=details)
        return redirect(url_for('login'))
    @app.route('/studentsmanagement')
    def studentsmanagement():
        if session.get('type') == 'admin':
            return render_template("studentsadmin.html")
        return redirect(url_for('index'))

    @app.route('/perfomance')
    def studentperfomancemanagement():
        if session.get('type') == 'admin':
            return render_template('studentperfomanceadmin.html')
        return redirect(url_for('index'))

    @app.route('/teachersManagement')
    def teachersManagement():
        if session.get('type') == 'admin':
            return render_template('teachersavailable.html')
        return redirect(url_for('index'))

    @app.route('/studentsattendance')
    def studentsattendance():
        if session.get('type') == 'admin':
            return render_template('attendancemarking.html')
        return redirect(url_for('index'))

    @app.route('/curriculum')
    def admincurriculum():
        if session.get('type') == 'admin':
            return render_template("admincurriculum.html")
        return redirect(url_for('index'))

    @app.route('/reports')
    def adminreports():
        if session.get('type') == 'admin':
            return render_template('adminreports.html')
        return redirect(url_for('index'))

    @app.route('/assessments')
    def assessment():
        if session.get('type') == 'admin':
            return render_template('assessments.html')
        return redirect(url_for('index'))

    @app.route('/finances')
    def finances():
        if session.get('type') == 'admin':
            return render_template('finances.html')
        return redirect(url_for('index'))

    @app.route('/insertadmin')
    def insertadmin():
        newadmin = updateUsers()
        addnewadmin = newadmin.adminuser()
        adduser = addnewadmin.adduser('joshua','james','micky','josh@gmail.com','+254757316903',1234,'133878734424447098.jpg','ts12743','12436493')
        return jsonify(adduser)
    
def adminlogin(email,password):
        databaseretrival = selectusers()
        adminuser = databaseretrival.adminuser()
        login , message , user = adminuser.login(email,password)
        print(login, message, user)
        return login, message, user