from flask import Blueprint, jsonify, request, abort
from app.middlewares import token_required
from app.models import User
from app.inicial import session
from werkzeug.security import generate_password_hash
from flask_cors import CORS

cliente_api = Blueprint('cliente_api', __name__, template_folder='templates')


"""
Esta e a api do cliente, as funcoes de crud (create, read, update, delete), 
O CORS funciona para permitir o front-end react.js consiga fazer a requisicao via Axios para nossa api.
"""

CORS(cliente_api, resources={r"/user/*": {"origins": "http://localhost:3000"}})


@cliente_api.route('/user/<int:id>', methods=['GET'])
@token_required
def um_cli(current_user, id):
    """
    Pega um cliente no banco de dados

    :param User current_user: dados do usuario decodificado
    :param int id: Retorna o id colocado na rota
    :return: json
    """
    user = session.query(User).filter_by(id=id).first()

    if not user:
        return jsonify({'message': 'User not found!'})

    user_data = {}
    user_data['id'] = user.id
    user_data['name'] = user.name
    user_data['age'] = user.age
    user_data['email'] = user.email

    return jsonify({'user': user_data})


@cliente_api.route('/user/<int:id>', methods=['PUT'])
@token_required
def att_cli(current_user, id):

    """
    Atualiza dados do cliente no banco de dados

    :param User current_user: dados do usuario decodificado
    :param int id: Retorna o id colocado na rota
    :return: json
    """


    user = session.query(User).filter_by(email=current_user.email).first()
    if not user:
        return abort(404)

    id_pedido = session.query(User).filter_by(id=id).first()

    data_json = request.get_json()
    
    if not data_json:
        return jsonify({'message': 'Nenhum campo pode ficar vazio'})

    if not id_pedido:
        return jsonify({'message': 'Não encontrado usuario'})

    # status preparando...
    if not data_json['email'] or data_json['email'] == '':
        id_pedido.email = id_pedido.email

    else:
        id_pedido.email = data_json['email']

    # status enviado...
    if not data_json['name']:
        id_pedido.name = id_pedido.name

    else:
        id_pedido.name = data_json['name']

    # status entregue
    if not data_json['age'] or data_json['age'] == '':
        id_pedido.age = id_pedido.age

    else:
        id_pedido.age = data_json['age']

    

    session.commit()

    return jsonify({'usuario': 'usuario atualizado'})


@cliente_api.route('/user/<int:id>', methods=['DELETE'])
@token_required
def deletar_cli(current_user, id):

    """
    Deleta a conta de um cliente do banco de dados

    :param User current_user: dados do usuario decodificado
    :param int id: Retorna o id colocado na rota
    :return: json
    """

    user = session.query(User).filter_by(email=current_user.email).first()
    if not user:
        return abort(404)

    id_cli = session.query(User).filter_by(id=id).first()

    if not id_cli:
        return jsonify({'message': 'usuario nao encontrado'})

    session.delete(id_cli)
    session.commit()
    return jsonify({'info_message': 'Usuario deletado'})


@cliente_api.route('/user', methods=['GET'])
@token_required
def todos_cli(current_user):

    """
    Pega  dados do cliente logado

    :param User current_user: Dados do usuario decodificado
    :return: json
    """

    user = session.query(User).filter_by(email=current_user.email).first()
    if not user:
        return abort(404)

    output = []

    
    user_data = {}
    user_data['id'] = user.id
    user_data['name'] = user.name
    user_data['age'] = user.age
    user_data['email'] = user.email
    output.append(user_data)

    return jsonify({'users': output})


@cliente_api.route('/user', methods=['POST'])
def criar_cli():

    """
    Cria uma conta pro cliente.

    :return: json
    """


    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    user_email = session.query(User).filter_by(email=data['email']).first()

    if not data:
        return jsonify({'message': 'nenhum campo pode ficar vazio'})

    if user_email:
        return jsonify({'message': 'Email ja existente'})

    new_user = User(name=data['name'], email=data['email'], age=data['age'],
                    password=hashed_password)

    session.add(new_user)
    session.commit()
    return jsonify({'info_message':  'cliente criado'})

