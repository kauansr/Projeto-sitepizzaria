from flask import jsonify, Blueprint, request
from app.models import Pedido, Produtos, User
from app.middlewares import token_required
from app.inicial import session
import socketio
import asyncio
import time

pedido = Blueprint('pedido', __name__, template_folder='templates')

# criar a lista pedido e deletar com


@pedido.route('/user/pedido/<int:id>', methods=['GET'])
@token_required
def pedidos(current_user, id):

    pedido_id = session.query(Pedido).filter_by(id=id).first()

    if not pedido_id:
        jsonify({'message': 'nao foi possivel encontrar pedido'})

    pedido_item = {}
    pedido_item['email'] = pedido_id.email
    pedido_item['data_pedido'] = pedido_id.data_pedido
    pedido_item['quantidade'] = pedido_id.quantidade
    pedido_item['status'] = pedido_id.status
    pedido_item['frete'] = pedido_id.frete
    pedido_item['custo_total'] = pedido_id.custo_total

    return jsonify({'Pedido': pedido_item})


@pedido.route('/user/pedido/', methods=['POST'])
@token_required
def criar_pedidos(current_user):

    data_pedido = request.get_json()

    if not data_pedido:
        return jsonify({'message': 'Nenhum campo pode ficar vazio'})

    email_user = session.query(User).filter_by(id=data_pedido['id']).first()

    if not email_user:
        return jsonify({'Message': 'nao foi possivel concluir seu pedido'})

    pedido_lista = Pedido(email=email_user.email,  quantidade=data_pedido['quantidade'],
                          status='preparando...', frete=data_pedido['frete'], custo_total=data_pedido['custo_total'])

    session.add(pedido_lista)
    session.commit()
    return jsonify({'Message': 'pedido criado'})


@pedido.route('/user/pedido/<int:id>', methods=['DELETE'])
@token_required
def cancelar_pedido(current_user, id):

    id_pedido = session.query(Pedido).filter_by(id=id).first()

    if not id_pedido:
        return jsonify({'message': 'nao foi possivel achar pedido'})

    session.delete(id_pedido)
    session.commit()

    return jsonify({'message': 'Pedido deletado!'})
