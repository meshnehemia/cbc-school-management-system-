from flask import session, render_template, redirect, url_for

def admin(app):
    @app.route('/admin')
    def admindashboard():
        if session.get('type') == 'admin':
            return render_template('index.html')
        return redirect(url_for('index'))
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
