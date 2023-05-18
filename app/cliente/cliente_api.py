from flask import Blueprint, jsonify, request, render_template, redirect
from app.middlewares import token_required
from app.models import User
from app.inicial import session
from werkzeug.security import generate_password_hash


cliente_api = Blueprint('cliente_api', __name__, template_folder='templates')

# Aqui sera a api do cliente


@cliente_api.route('/user/<int:id>', methods=['GET'])
@token_required
def um_cli(current_user, id):
    user = session.query(User).filter_by(id=id).first()

    if not user:
        return jsonify({'message': 'User not found!'})

    user_data = {}
    user_data['id'] = user.id
    user_data['name'] = user.name
    user_data['endereco'] = user.endereco
    user_data['age'] = user.age
    user_data['email'] = user.email

    return jsonify({'user': user_data})


@cliente_api.route('/user/<int:id>', methods=['PUT'])
@token_required
def att_cli(current_user, id):
    user_usuario = session.query(User).filter_by(id=id).first()

    if not user_usuario:
        return jsonify({'message': 'Usuario nao encontrado'})

    user_usuario.email = request.json['email']
    user_usuario.name = request.json['name']
    user_usuario.endereco = request.json['endereco']
    user_usuario.age = request.json['age']

    session.commit()

    return jsonify({'usuario': 'usuario atualizado'})


@cliente_api.route('/user/<int:id>', methods=['DELETE'])
@token_required
def deletar_cli(current_user, id):
    id_cli = session.query(User).filter_by(id=id).first()

    if not id_cli:
        return jsonify({'message': 'usuario nao encontrado'})

    session.delete(id_cli)
    session.commit()
    return jsonify({'message': 'Usuario deletado'})


@cliente_api.route('/user', methods=['GET'])
@token_required
def todos_cli(current_user):
    clientes = session.query(User).all()
    if not clientes:
        return jsonify({'message': 'no users'})

    output = []

    for user in clientes:
        user_data = {}
        user_data['id'] = user.id
        user_data['name'] = user.name
        user_data['age'] = user.age
        user_data['endereco'] = user.endereco
        user_data['email'] = user.email
        output.append(user_data)

    return jsonify({'users': output})


@cliente_api.route('/user', methods=['POST'])
def criar_cli():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')

    user_email = session.query(User).filter_by(email=data['email']).first()

    if not data:
        return jsonify({'message': 'nenhum campo pode ficar vazio'})

    if user_email:
        return jsonify({'message': 'Email ja existente'})

    new_user = User(name=data['name'], email=data['email'], age=data['age'],
                    endereco=data['endereco'], password=hashed_password)

    session.add(new_user)
    session.commit()
    return jsonify({'message':  'cliente criado'})
