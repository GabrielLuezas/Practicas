from flask import Flask, jsonify, request
import pymongo
import json
cliente = pymongo.MongoClient('localhost',
                             port=27017,
                             username='user',
                             password='password')    
db = cliente.get_database('API')
coleccion = db['API']
app = Flask(__name__)
def convertir_a_json(documento):
    if '_id' in documento:
        documento['_id'] = str(documento['_id'])
    return json.dumps(documento)
@app.route('/usuarios')
def Usuarios():
    documentos = coleccion.find()
    lista_documentos = [convertir_a_json(doc) for doc in documentos]
    return jsonify({"Usuarios": lista_documentos})

@app.route('/usuarios/<string:nombre_usuario>')
def conseguirUsuarios(nombre_usuario):
    documentos = coleccion.find()
    lista_documentos = [convertir_a_json(doc) for doc in documentos]
    usuarios_encontrados = [doc for doc in lista_documentos if doc['nombre'] == nombre_usuario]
    if len(usuarios_encontrados) > 0:
        return jsonify({"usuarios": usuarios_encontrados})
    else:
        return jsonify({"message": "No se encontraron usuarios con el nombre especificado."})

@app.route('/usuarios/<string:nombre_usuario>/<string:id_usuario>')
def obtenerUsuario(nombre_usuario, id_usuario):
    documentos = coleccion.find()
    lista_documentos = [convertir_a_json(doc) for doc in documentos]
    usuarios_encontrados = [doc for doc in lista_documentos if doc['nombre'] == nombre_usuario and doc['id'] == id_usuario]
    if len(usuarios_encontrados) > 0:
        return jsonify({"usuario": usuarios_encontrados[0]})
    else:
        return jsonify({"message": "No se encontró el usuario con el nombre y ID especificados."})

@app.route('/usuarios', methods=['POST'])
def AñadirDatosAMongo():
    try:
        nuevo_usuario = {
            'nombre': request.json['nombre'],
            'apellido': request.json['apellido'],
            'edad': request.json['edad']
        } 
        coleccion.insert_one(nuevo_usuario)
        return jsonify({'message': 'Usuario añadido a Mongo'})
    except Exception as e1:
        return jsonify({'message': 'Algo no ha funcionado:  {}'.format(str(e1))})
@app.route('/usuarios/<string:nombre_usuario>', methods=['PUT'])
def actualizarUsuario(nombre_usuario):
    documentos = coleccion.find()
    lista_documentos = [convertir_a_json(doc) for doc in documentos]
    usuarios_encontrados = [doc for doc in lista_documentos if doc['nombre'] == nombre_usuario]
    try:
        if len(usuarios_encontrados) > 0:
            filtro = {'nombre': nombre_usuario}
            actualizacion = {
                '$set': {
                'nombre': request.json['nombre'],
                'apellido': request.json['apellido'],
                'edad': request.json['edad']
             }
            }
            coleccion.update_one(filtro, actualizacion)
            return jsonify({"message": "Documento actualizado correctamente"})
        else:
            return jsonify({"message": "No hay documentos con ese nombre"})
    except Exception as e1:
        return jsonify({'message': 'Algo no ha funcionado:  {}'.format(str(e1))})
@app.route('/usuarios/<string:nombre_usuario>', methods=['DELETE'])
def eliminarUsuario(nombre_usuario):
    filtro = {'nombre': nombre_usuario}
    resultado = coleccion.delete_one(filtro)
    if resultado.deleted_count > 0:
        return jsonify({'message': 'Usuario borrado con éxito'})
    else:
        return jsonify({'message': 'No hay documentos con ese nombre'})
if __name__ == '__main__':
    app.run(debug=True, port=4000) 