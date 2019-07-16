from flask import Flask, jsonify, request, json
from flask_mysqldb import MySQL
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token

app= Flask(__name__)
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'flask_Vue'
app.config['MYSQL_CURSORCLASS']= 'DictCursor'
app.config['JWT_SECRET_KEY']= 'secret'


mysql= MySQL(app)
bcrypt= Bcrypt(app)
jwt= JWTManager(app)
CORS(app)

@app.route('/users/register', methods=['POST'])
def register():
    cur= mysql.connection.cursor()
    first_name= request.get_json()['first_name']
    last_name= request.get_json()['last_name']
    email= request.get_json()['email']
    password= bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')
    created= datetime.utcnow()

    sql = "INSERT INTO users(first_name, last_name, email, password, created) VALUES (%s, %s, %s, %s, %s)"
    val = (str(first_name),str(last_name),str(email),str(password),str(created))
    cur.execute(sql,val)
    mysql.connection.commit()

    result= {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'created': created
    }

    return jsonify({'result': result})

@app.route('/users/login', methods=['POST'])
def login():
    cur= mysql.connection.cursor()
    email= request.get_json()['email']
    password= request.get_json()['password']

    result=""

    cur.execute("select * from users where email= '"+str(email)+"'")
    rv= cur.fetchone()

    if bcrypt.check_password_hash(rv['password'], password):
        access_token= create_access_token(identity={'first_name': rv['first_name'],'last_name': rv['last_name'],'email': rv['email']})
        result= access_token
    else:
        result= jsonify({"Error": "username or password error"})
    
    return result

if __name__=='__main__':
    app.run(debug=True)



