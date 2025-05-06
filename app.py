from flask import Flask, redirect, render_template, request, session, url_for
from adminManagement import admin ,adminlogin

app = Flask(__name__)
app.secret_key = "mysecret_key"

# Register routes
admin(app)

def autheticate():
    if 'type' in session and 'id' in session:
        return True
    else:
        return False
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data['email']
        password = data['password']
        type = data['type']
        if type == 'admin':
            status,message,details =  adminlogin(email,password)
            if status:
                session['type'] = type
                session['id'] = details[0]
                session['email'] = email
                session['password'] = password
                session['first_name'] = details[1]
                session['second_name'] = details[2]
                session['last_name'] = details[3]
                session['phone_number'] = details[5]
                session['profile_picture'] = details[7]
                session['tsc_number'] = details[9]
                return redirect(url_for('admindashboard'))
            else:
                return render_template('login.html', message=message)
        elif type == 'teacher':
            return redirect(url_for('teachersManagement'))
        elif type == 'student':
            return redirect(url_for('studentsmanagement'))
        elif type == 'finance':
            return redirect(url_for('finances'))
        else:
            return render_template('login.html')
    if autheticate():
        return redirect(url_for('admindashboard'))
    else:
        return render_template('login.html')
@app.route('/logout')
def logout():
    pass

if __name__ == '__main__':
    app.run(debug=True)
