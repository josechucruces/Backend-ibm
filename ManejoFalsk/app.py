from flask import Flask, render_template, request
from cliente_dao import ClienteDao
from wtforms import Form, StringField, TextAreaField, validators

app = Flask(__name__)

titulo_app = 'Zona Fit (GYM)'

@app.route('/')
@app.route('/index.html')
def inicio():
    app.logger.debug('Entramos al path de inicio')
    clientes = ClienteDao.listar_clientes()
    return render_template('index.html', titulo=titulo_app, clientes=clientes)

if __name__ == '__main__':
    app.run(debug=True)
