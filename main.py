from app.inicial import app, session
from flask import request, jsonify, make_response
from app.models import User, Empresa
import jwt
import datetime
from app.cliente.cliente_api import cliente_api
from app.empresa.empresa_api import empresa_api
from app.empresa.produto import produtos
from app.cliente.pedido import pedido
from app.empresa.att_pedido import pedido_att
from flask_cors import CORS

app.config['SECRET_KEY'] = 'secretachave'
CORS(app, resources={r"/login": {"origins": "http://localhost:3000"}})


app.register_blueprint(cliente_api)
app.register_blueprint(empresa_api)
app.register_blueprint(produtos)
app.register_blueprint(pedido)
app.register_blueprint(pedido_att)

@app.route('/login', methods=['POST'])
def login():

    """
    Login dos usuarios e empresas

    :return: Json
    """
    email = request.json['email']
    password = request.json['password']

    user = session.query(User).filter_by(email=email).first()
    is_admin = session.query(Empresa).filter_by(user_id=user.id).first()


    if is_admin:
        is_admin = is_admin.is_admin
    
    else:
        is_admin = False

    try:
        if user:
            if user.verifica_password(password):
                token = jwt.encode({'id': user.id, 'email': user.email, 'status_log': user.status_log, 'exp': datetime.datetime.utcnow(
                ) + datetime.timedelta(hours=1)}, app.config['SECRET_KEY'])

                
            
                data = [{'token': token},{'is_admin': is_admin}]

                return jsonify(data)
            return jsonify({'Message': " Senha incorreto"})
        
        return jsonify({'Message': " email  incorreto"})

    except:
        return make_response('Nao pode verificar2', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})


if __name__ == '__main__':
    app.run(debug=True)
