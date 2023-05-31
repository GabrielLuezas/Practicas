from flask import Flask, jsonify, request, render_template
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager, verify_jwt_in_request
import pymongo

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
app.config["JWT_SECRET_KEY"] = "Patata" 
jwt = JWTManager(app)

@app.route("/navegador", methods=["GET", "POST"])
def login2():
    documentos = coleccion.find()
    lista_usuarios = [convertir_a_json(doc) for doc in documentos]
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        for verificacion in lista_usuarios:
            if verificacion["username"] == username and verificacion["password"] == password:
                access_token = create_access_token(identity=username)
                return jsonify({"Tu token de acceso": access_token})
        return jsonify({"msg": "El usuario o la contraseña son incorrectos"}), 401
    return render_template('login.html')

@app.route("/login", methods=["POST"])
def login():
    documentos = coleccion.find()
    lista_usuarios = [convertir_a_json(doc) for doc in documentos]
    username = request.json['username']
    password = request.json['password']
    for verificacion in lista_usuarios:
        if verificacion["username"] == username and verificacion["password"] == password:
            access_token = create_access_token(identity=username)
            return jsonify({"msg": access_token})
    return jsonify({"msg": "El usuario o la contraseña son incorrectos"}), 401

@app.route("/protegida", methods=["GET", "POST"])
@jwt_required()
def protegida():
    verify_jwt_in_request()
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == "__main__":
    app.run(debug=True, port=4000) 