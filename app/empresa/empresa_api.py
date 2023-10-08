from flask import Blueprint, jsonify, request, abort
from app.middlewares import token_required
from app.models import User, Empresa
from app.inicial import session
from werkzeug.security import generate_password_hash
from flask_cors import CORS

empresa_api = Blueprint('empresa_api', __name__, template_folder='templates')

"""
API da empresa CRUD(Create, Read, Update, Delete), CORS permite requisicoes do
front-end
"""

CORS(empresa_api, resources={r"/user/empresa/*": {"origins": "http://localhost:3000"}})

@empresa_api.route('/user/empresa', methods=['GET'])
@token_required
def todos_empresa(current_user):

    """
    Pega a empresa do usuario logado

    :param User current_user: dados do usuario(empresa)
    :return: Json
    """


    user = session.query(Empresa).filter_by(user_id=current_user.id).first()
    

    if not user:
        return abort(404)

    output = []

    
    user_data = {}
    user_data['id'] = user.id
    user_data['empresa'] = user.empresa
    user_data['user_id'] = user.user_id
    user_data['is_admin'] = user.is_admin
    user_data['cnpj'] = user.cnpj
    output.append(user_data)

    return jsonify({'users': output})


@empresa_api.route('/user/empresa/<id>', methods=['GET'])
@token_required
def um_empresa(current_user, id):

    """
    Pega uma empresa

    :param User current_user: dados do usuario(empresa)
    :param int id: dados da rota id
    :return: Json
    """

    user = session.query(Empresa).filter_by(id=id).first()

    if not user:
        return jsonify({'message': 'User not found!'})

    user_data = {}
    user_data['id'] = user.id
    user_data['empresa'] = user.empresa
    user_data['is_admin'] = user.is_admin
    user_data['user_id'] = user.user_id

    return jsonify({'user': user_data})


@empresa_api.route('/user/empresa', methods=['POST'])
def criar_empresa():

    """
    Cria uma empresa
    """


    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    user_email = session.query(User).filter_by(email=data['email']).first()

    if user_email:
        return jsonify({'message': 'Email ja existente'})

    new_user = User(name=data['name'], email=data['email'],
                    age=data['age'], password=hashed_password)
    session.add(new_user)
    session.commit()
    new_user_empresa = Empresa(
        empresa=data['empresa'], cnpj=data['cnpj'], is_admin=True, user_id=new_user.id)

    session.add(new_user_empresa)
    session.commit()
    return jsonify({'info empresa':  'empresa criada'})


@empresa_api.route('/user/empresa/<id>', methods=['PUT'])
@token_required
def atualizar_empresa(current_user, id):

    """
    Atualiza uma empresa

    :param User current_user: dados do usuario(empresa)
    :param int id: dados da rota id
    :return: Json
    """

    id_empresa = session.query(Empresa).filter_by(user_id=current_user.id).first()

    if not id_empresa:
        return abort(401)
    
    data_json = request.get_json()

    id_pedido = session.query(Empresa).filter_by(id=id).first()

    if not data_json:
        return jsonify({'message': 'Nenhum campo pode ficar vazio'})

    if not id_pedido:
        return jsonify({'message': 'Não encontrado empresa'})

    # status preparando...
    if not data_json['cnpj'] or data_json['cnpj'] == '':
        id_pedido.cnpj = id_pedido.cnpj

    else:
        id_pedido.cnpj = data_json['cnpj']

    if not data_json['empresa'] or data_json['empresa'] == '':
        id_pedido.empresa = id_pedido.empresa

    else:
        id_pedido.empresa = data_json['empresa']

    session.commit()

    return jsonify({'info_mudanca_empresa': 'Empresa mudada com sucesso'})


@empresa_api.route('/user/empresa/<id>', methods=['DELETE'])
@token_required
def deletar_empresa(current_user, id):

    """
    Deleta uma empresa

    :param User current_user: dados do usuario(empresa)
    :param int id: dados da rota id
    :return: Json
    """

    id_empresa = session.query(Empresa).filter_by(user_id=current_user.id).first()

    if not id_empresa:
        return abort(401)

    user_empresa = session.query(Empresa).filter_by(id=id).first()

    if not user_empresa:
        return jsonify({'message': 'Nao foi encontrado empresa'})
    session.delete(user_empresa)

    session.commit()

    return jsonify({'info empresa deletada': 'Empresa  deletada'})
