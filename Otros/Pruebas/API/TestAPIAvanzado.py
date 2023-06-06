import pytest 
from Cookies import apppp

@pytest.fixture
def cliente3():
    apppp.config['TESTING'] = True
    with apppp.test_client() as cliente3:
        yield cliente3


def test_cookie(cliente3):
    respuesta = cliente3.get('/cookies')
    assert respuesta.status_code == 302

def test_vercookie(cliente3):
    respuesta = cliente3.get('/cookies/vercookie')
    assert respuesta.status_code == 200
    assert f'No se encontró la cookie' in respuesta.data

    respuesta = cliente3.get('/cookies')
    assert respuesta.status_code == 302

    respuesta = cliente3.get('/cookies/vercookie')
    assert respuesta.status_code == 200
    assert f'Este es el contenido de mi cookie: Mi cookie' in respuesta.data

def test_cookies(cliente3):
    respuesta = cliente3.get('/cookiesaceptar')
    assert respuesta.status_code == 200

    respuesta = cliente3.post('/cookiesaceptar', data={'action': 'accept'})
    assert respuesta.status_code == 302
    assert respuesta.headers['Location'] == 'http://localhost/protected'

    respuesta = cliente3.get('/protected')
    assert respuesta.status_code == 200
    assert f'¡Bienvenido a la página donde necesitas las cookies!' in respuesta.data

    respuesta = cliente3.post('/cookiesaceptar', data={'action': 'reject'})
    assert respuesta.status_code == 302
    assert respuesta.headers['Location'] == 'http://localhost/cookies_rejected'

    respuesta = cliente3.get('/protected')
    assert respuesta.status_code == 302
    assert respuesta.headers['Location'] == 'http://localhost/cookies_rejected'

def test_protected_page(cliente3):
    respuesta = cliente3.get('/protected')
    assert respuesta.status_code == 302
    assert respuesta.headers['Location'] == 'http://localhost/cookies_rejected'

    cliente3.post('/cookiesaceptar', data={'action': 'accept'})
    respuesta = cliente3.get('/protected')
    assert respuesta.status_code == 200
    assert f'¡Bienvenido a la página donde necesitas las cookies!' in respuesta.data

def test_cookies_rejected(cliente3):
    respuesta = cliente3.get('/cookies_rejected')
    assert respuesta.status_code == 200
    assert f'Debes activar las cookies para acceder a esta página.' in respuesta.data