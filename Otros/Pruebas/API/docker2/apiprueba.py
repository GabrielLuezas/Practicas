from flask import Flask, send_file

app = Flask(__name__)

@app.route('/prueba')
def prueba():
    return '''
    <h1>Esto es una ruta de prueba</h1>
    <img src="/imagen.png" alt="Imagen de prueba">
    '''

@app.route('/imagen.png')
def obtener_imagen():
    return send_file('imagen.png', mimetype='image/png')

if __name__ == '__main__':
    app.run()
    