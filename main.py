from app.inicial import app, session
from flask import request, jsonify, make_response
from app.models import User
import jwt
import datetime
from app.cliente.cliente_api import cliente_api
from app.empresa.empresa_api import empresa_api
from app.empresa.produto import produtos
from app.cliente.pedido import pedido

app.config['SECRET_KEY'] = 'secretachave'


app.register_blueprint(cliente_api)
app.register_blueprint(empresa_api)
app.register_blueprint(produtos)
app.register_blueprint(pedido)


@app.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    password = request.json['password']

    user = session.query(User).filter_by(email=email).first()

    try:
        if user:
            if user.verifica_password(password):
                token = jwt.encode({'id': user.id, 'email': user.email,  'exp': datetime.datetime.utcnow(
                ) + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'])
                user.status = True

                return jsonify({'token': token})

            return jsonify({'Message': " email ou senha incorretos"})
        return jsonify({'Message': " email ou senha incorretos"})

    except:
        return make_response('Nao pode verificar2', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


if __name__ == '__main__':
    app.run(debug=True)
