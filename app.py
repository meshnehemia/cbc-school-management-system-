from flask import Flask, render_template, session
from adminManagement import admin

app = Flask(__name__)
app.secret_key = "mysecret_key"

# Register routes
admin(app)

@app.route('/')
def index():
    session['type'] = "admin"  # Simulate login as admin
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
