from flask import Flask, jsonify, request
import pymongo

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
    return documento

@app.route('/usuarios', methods=['DELETE'])
def eliminarUsuario():
    usuario = {
        'nombre': request.json['nombre'],
        'apellido': request.json['apellido'],
        'edad': request.json['edad']
    }
    documentos = coleccion.find()
    lista_documentos = [convertir_a_json(doc) for doc in documentos]
    if usuario in lista_documentos:
        coleccion.delete_one(usuario)
        return jsonify({'message': 'Usuario borrado con exito'})
    else:
        return jsonify({'message': 'No hay ningun documento con esos datos'})

@app.route('/usuarios', methods=['DELETE'])
def eliminarUsuario():
    usuario = {
        'nombre': request.json['nombre'],
        'apellido': request.json['apellido'],
        'edad': request.json['edad']
    }
    coleccion.delete_one(usuario)
    return jsonify({'message': 'Usuario borrado con exito'})



if __name__ == '__main__':
    app.run(debug=True, port=4000)
