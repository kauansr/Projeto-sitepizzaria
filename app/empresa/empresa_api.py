from flask import Blueprint, jsonify, request
from app.middlewares import token_required
from app.models import User, Empresa
from app.inicial import session
from werkzeug.security import generate_password_hash

empresa_api = Blueprint('empresa_api', __name__, template_folder='templates')


@empresa_api.route('/user/empresa', methods=['GET'])
@token_required
def todos_empresa(current_user):

    users = session.query(Empresa).all()

    output = []

    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['empresa'] = user.empresa
        user_data['user_id'] = user.user_id
        output.append(user_data)

    return jsonify({'users': output})


@empresa_api.route('/user/empresa/<id>', methods=['GET'])
@token_required
def um_empresa(current_user, id):

    user = session.query(Empresa).filter_by(id=id).first()

    if not user:
        return jsonify({'message': 'User not found!'})

    user_data = {}
    user_data['id'] = user.id
    user_data['empresa'] = user.empresa
    user_data['user_id'] = user.user_id

    return jsonify({'user': user_data})


@empresa_api.route('/user/empresa', methods=['POST'])
def criar_empresa():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    user_email = session.query(User).filter_by(email=data['email']).first()

    if user_email:
        return jsonify({'message': 'Email ja existente'})

    new_user = User(name=data['name'], email=data['email'],
                    endereco=data['endereco'], age=data['age'], password=hashed_password)
    session.add(new_user)
    session.commit()
    new_user_empresa = Empresa(
        empresa=data['empresa'], cnpj=data['cnpj'], user_id=new_user.id)

    session.add(new_user_empresa)
    session.commit()
    return jsonify({'info empresa':  'empresa criada'})


@empresa_api.route('/user/empresa/<id>', methods=['PUT'])
@token_required
def atualizar_empresa(current_user, id):

    user_empresa = session.query(Empresa).filter_by(id=id).first()

    if not user_empresa:
        return jsonify({'message': 'Empresa nao encontrada.'})
    user_empresa.cnpj = request.json['cnpj']
    user_empresa.empresa = request.json['empresa']

    session.commit()

    return jsonify({'info mudanca empresa': 'Empresa mudada com sucesso'})


@empresa_api.route('/user/empresa/<id>', methods=['DELETE'])
@token_required
def deletar_empresa(current_user, id):

    user_empresa = session.query(Empresa).filter_by(id=id).first()

    if not user_empresa:
        return jsonify({'message': 'Nao foi encontrado empresa'})
    session.delete(user_empresa)

    session.commit()

    return jsonify({'info empresa deletada': 'Empresa  deletada'})
