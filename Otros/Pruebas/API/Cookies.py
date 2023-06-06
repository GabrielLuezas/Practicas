from flask import Flask, jsonify, request, render_template, make_response, redirect, url_for
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, create_refresh_token, get_jwt_identity, verify_jwt_in_request
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

apppp = Flask(__name__)
apppp.config["JWT_SECRET_KEY"] = "Patata" 
jwt = JWTManager(apppp)

@apppp.route('/cookies')
def cookie():
    respuesta = make_response('Añadiendo la cookie')
    respuesta.set_cookie('Nombre', 'Mi cookie')
    return redirect(url_for('vercookie'))

@apppp.route('/cookies/vercookie')
def vercookie():
    Nombre = request.cookies.get('Nombre')
    if Nombre:
        return 'Este es el contenido de mi cookie: ' + Nombre
    else:
        respuesta = make_response('No se encontró la cookie')
        respuesta.delete_cookie('Nombre') 
        return respuesta



@apppp.route('/cookiesaceptar', methods=['GET', 'POST'])
def cookies():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'accept':
            global cookies_accepted
            cookies_accepted = True
            return redirect(url_for('protected_page'))
        elif action == 'reject':
            return redirect(url_for('cookies_rejected'))

    return render_template('cookies.html')

@apppp.route('/protected')
def protected_page():
    if 'cookies_accepted' in globals() and cookies_accepted:
        return "¡Bienvenido a la página donde necesitas las cookies!"
    else:
        return redirect(url_for('cookies_rejected'))

@apppp.route('/cookies_rejected')
def cookies_rejected():
    return "Debes activar las cookies para acceder a esta página."

if __name__ == "__main__":
    apppp.run(debug=True, port=4000)