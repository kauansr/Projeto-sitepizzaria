from flask import jsonify, Blueprint, request, abort
from app.models import Pedido, Produtos, Empresa
from app.middlewares import token_required
from app.inicial import session
import asyncio
import time
from flask_cors import CORS

pedido_att = Blueprint('pedido_att', __name__, template_folder='templates')

"""
API dos Pedidos para empresa CRUD (Create, Read, Update, Delete), CORS permite 
o front-end fazer requisicoes
"""

CORS(pedido_att, resources={r"/user/empresa/pedido/*": {"origins": "http://localhost:3000"}})

@pedido_att.route('/user/empresa/pedido', methods=['GET'])
@token_required
def Pedidos_todos(current_user):
    
    """
    Pega todos pedidos dos clientes

    :param User current_user: dados da empresa
    :return: Json
    """

    id_empresa = session.query(Empresa).filter_by(user_id=current_user.id).first()

    if not id_empresa:
        return abort(401)

    pedidos_info = session.query(Pedido).all()

    if not pedidos_info:
        return abort(404)

    output = []

    for user in pedidos_info:
        user_data = {}
        user_data['id'] = user.id
        user_data['nome'] = user.pedido_nome
        user_data['email'] = user.email
        user_data['data_pedido'] = user.data_pedido
        user_data['status'] = user.status
        user_data['frete'] = user.frete
        user_data['custo_total'] = user.custo_total
        output.append(user_data)

    return jsonify({'pedidos': output})

@pedido_att.route('/user/empresa/pedido/<int:id>', methods=['GET'])
@token_required
def pedidos(current_user, id):

    """
    Pega um pedido do cliente

    :param User current_user: dados do usuario(empresa)
    :param int id: dados da rota id
    :return: Json
    """

    id_pedido = session.query(Pedido).filter_by(id=id).first()

    if not id_pedido:
        jsonify({'message': 'nao foi possivel encontrar pedido'})

    pedido_item = {}
    pedido_item['email'] = id_pedido.email
    pedido_item['nome'] = id_pedido.pedido_nome
    pedido_item['data_pedido'] = id_pedido.data_pedido
    pedido_item['status'] = id_pedido.status
    pedido_item['frete'] = id_pedido.frete
    pedido_item['custo_total'] = id_pedido.custo_total

    return jsonify({'Pedido': pedido_item})


@pedido_att.route('/user/empresa/pedido/<int:id>', methods=['PUT'])
@token_required
def att_pedido(current_user, id):

    """
    Atualiza um pedido do cliente

    :param User current_user: dados do usuario(empresa)
    :param int id: dados da rota id
    :return Json
    """

    id_empresa = session.query(Empresa).filter_by(user_id=current_user.id).first()

    if not id_empresa:
        return abort(401)

    id_pedido = session.query(Pedido).filter_by(id=id).first()

    data_json = request.get_json()

    if not data_json:
        return jsonify({'message': 'Nenhum campo pode ficar vazio'})

    if not id_pedido:
        return abort(404)

    # status preparando...
    if not data_json['Preparando...'] or data_json['Preparando...'] == '':
        id_pedido.status = id_pedido.status

    else:
        id_pedido.status = data_json['Preparando...']

    # status enviado...
    if not data_json['Enviado'] or data_json['Enviado'] == '':
        id_pedido.status = id_pedido.status

    else:
        id_pedido.status = data_json['Enviado']

    # status entregue
    if not data_json['Entregue'] or data_json['Entregue'] == '':
        id_pedido.status = id_pedido.status

    else:
        id_pedido.status = data_json['Entregue']

    session.commit()

    return jsonify({'info_message': 'status trocado'})


@pedido_att.route('/user/empresa/pedido/<int:id>', methods=['DELETE'])
@token_required
def cancelar_pedidos(current_user, id):

    """
    Cancela o pedido do cliente

    :param User current_user: dados do usuario(empresa)
    :param int id: dados da rota id
    :return: Json
    """

    id_empresa = session.query(Empresa).filter_by(user_id=current_user.id).first()

    if not id_empresa:
        return abort(401)

    id_pedido = session.query(Pedido).filter_by(id=id).first()

    if not id_pedido:
        return abort(404)

    session.delete(id_pedido)
    session.commit()

    return jsonify({'message': 'Pedido deletado!'})


