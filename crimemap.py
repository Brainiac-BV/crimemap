from dbhelper import DBHelper
from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)
DB = DBHelper()


# main view function
@app.route('/')
def home():
    try:
        data = DB.get_all_inputs()
    except Exception as e:
        print e
        data = None
    return render_template("home.html", data=data)


# view function to add crimes to db
@app.route('/add', methods=['POST'])
def add():
    try:
        data = request.form.get('userinput')
        DB.add_input(data)
    except Exception as e:
        print e
    return home()


# view function to clear crime entries from db
@app.route('/clear')
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        print e
    return home()

if __name__ == '__main__':
    app.run(port=5001, debug=True)
