# from flask import Flask,render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template("index.html")

# if __name__ == '__main__':
#     app.run(debug=True,port=700)



# from flask import Flask,request
# app=Flask(__name__)
# users=[]
# @app.route('/')
# def home():
#    return '''
# <form action="/save" method="post">
#   <label for="name">Name:</label><br>
#   <input type="text" id="name" name="name"><br><br>
#   <label for="password">Password:</label><br>
#   <input type="password" id="password" name="password"><br><br>
#   <input type="submit" value="save">
# </form>
# '''
# @app.route('/save', methods=['POST'])
# def save():
#     name = request.form['name']
#     password = request.form['password']
#     users.append({'name': name, 'password': password}) 
#     return f"user {name} saved! total login : {len(users)}"
# @app.route('/users')
# def show_users():
#     return str(users)

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from pymongo import MongoClient

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'naresh'
mysql = MySQL(app)

mongo_client=MongoClient('mongodb://localhost:27017/')
mongo_db=mongo_client['garage']
CAR=mongo_db['suv']
AUDI=mongo_db['audi']

@app.route('/', methods=['GET'])
def index():
    return render_template('acc.html')
@app.route('/car')
def car():
    return render_template('car.html')
@app.route('/dealers')
def dealers():
    return render_template('dealers.html')
@app.route('/def')
def defe():
    return render_template('defe.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/service')
def service():
    return render_template('service.html')
@app.route('/garage')
def garage():
    carr=list(CAR.find())
    audii=list(AUDI.find())
    return render_template('garage.html',carr=carr,audii=audii)
@app.route('/s1')
def s1():
    return render_template('s1.html')
@app.route('/audi')
def audi():
    return render_template('audi.html')
@app.route('/submit')
def submit():
    return render_template('submit.html')
@app.route('/save', methods=['POST'])
def save():
    name = request.form['name']
    password = request.form['password']
    confirmpwd = request.form['confirmpwd']
    address = request.form['address']
    phn = request.form['phn']
    carmodel = request.form['carmodel']
    purpose = request.form['purpose']
    cur = mysql.connection.cursor()
    cur.execute("""
            INSERT INTO login (name, password, confirmpwd, address, phn, carmodel, purpose)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (name, password, confirmpwd, address, phn, carmodel, purpose))
    mysql.connection.commit()
    cur.close()
    return render_template('car.html')

@app.route('/s1',methods=['POST'])
def ser():
    name = request.form['name']
    contactNumber = request.form['contactNumber']
    carModel = request.form['carModel']
    serviceType = request.form['serviceType']
    otherService = request.form['otherService']
    appointmentDate = request.form['appointmentDate']
    cur = mysql.connection.cursor()
    cur.execute("""
            INSERT INTO services (name, contactNumber, carModel, serviceType, otherService, appointmentDate)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, contactNumber, carModel, serviceType, otherService, appointmentDate))
    mysql.connection.commit()
    cur.close()
    return render_template('submit.html')

@app.route('/submit',methods=['GET'])
def ss():
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)