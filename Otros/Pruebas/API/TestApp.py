import pytest 
from flask import Flask
from Autenticacion import app   
from apinueva import appp
from Cookies import apppp

@pytest.fixture
def cliente():
    app.config['TESTING'] = True
    with app.test_client() as cliente:
        yield cliente

@pytest.fixture
def cliente2():
    appp.config['TESTING'] = True
    with appp.test_client() as cliente2:
        yield cliente2

def test_logear_correcto(cliente):
    response = cliente.post('/login', json={"username": "gabriel", "password": "213"})
    assert response.status_code == 200
    assert 'msg' in response.json
    msg = response.json['msg']
    assert msg.startswith('eyJ')
    print("Access token:", msg)

def test_obtener_usuarios(cliente2):
    response = cliente2.get('/usuarios')
    assert response.status_code == 200
    assert 'Usuarios' in response.json

def test_info_por_usuario(cliente2):
    nombre_usuario = 'Alfonso'
    response = cliente2.get(f'/usuarios/{nombre_usuario}')
    assert response.status_code == 200
    assert 'usuarios' in response.json

def test_info_por_usuario_y_id(cliente2):
    nombre_usuario = 'Gabriel'
    id_usuario = '3'
    response = cliente2.get(f'/usuarios/{nombre_usuario}/{id_usuario}')
    assert response.status_code == 200
    assert 'usuario' in response.json

def test_anadir_usuario(cliente2):
    nuevo_usuario = {
        'id': '2',
        'nombre': 'nuevo',
        'apellido': 'usuario',
        'edad': 25
    }
    response = cliente2.post('/usuarios', json=nuevo_usuario)
    assert response.status_code == 200
    assert 'message' in response.json

def test_actualizar_usuario_existente(cliente2):
    nombre_usuario = 'Gabriel'
    id_usuario = '3'
    datos_usuario = {
        'nombre': 'Gabriel',
        'apellido': 'González',
        'edad': 25
    }
    response = cliente2.put(f'/usuarios/{nombre_usuario}/{id_usuario}', json=datos_usuario)
    assert response.status_code == 200
    assert 'message' in response.json
    assert response.json['message'] == 'Documento actualizado correctamente'

def test_eliminar_usuario_existente(cliente2):
    nombre_usuario = 'gabriel'
    id_usuario = '1'
    response = cliente2.delete(f'/usuarios/{nombre_usuario}/{id_usuario}')
    assert response.status_code == 200
    assert 'message' in response.json






if __name__ == '__main__':
    pytest.main([__file__])
 