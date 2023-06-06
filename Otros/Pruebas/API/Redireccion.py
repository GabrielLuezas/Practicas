from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from flask_jwt_extended import JWTManager
import pymongo
from datetime import timedelta

cliente = pymongo.MongoClient('localhost',
                             port=27017,
                             username='user',
                             password='password') 

db = cliente.get_database('API')
coleccion = db['usuarios verificados']

def convertir_a_json(documento):
    if '_id' in documento:
        documento['_id'] = str(documento['_id'])
    return documento

app = Flask(__name__)

app.config["SECRET_KEY"] = "Patata" 
app.config["JWT_SECRET_KEY"] = "Patata" 
jwt = JWTManager(app)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)

@app.route("/login", methods=["POST"])
def login():
    documentos = coleccion.find()
    lista_usuarios = [convertir_a_json(doc) for doc in documentos]
    username = request.json['username']
    password = request.json['password']
    for verificacion in lista_usuarios:
        if verificacion["username"] == username and verificacion["password"] == password:
            session.permanent = True 
            session.modified = True
            session['login_user'] = True
            return redirect(url_for('protegida'))
    return jsonify({"msg": "El usuario o la contraseña son incorrectos"}), 401

@app.route("/protegida", methods=["GET", "POST"])
def protegida():
    if session.get('login_user'):
        return jsonify(logged_in_as=session), 200
    else:
        return "No tienes permisos para acceder a esta zona"

if __name__ == "__main__":
    app.run(debug=True, port=4000)