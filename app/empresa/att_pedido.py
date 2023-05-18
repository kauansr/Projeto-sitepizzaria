from flask import jsonify, Blueprint, request
from app.models import Pedido, Produtos
from app.middlewares import token_required
from app.inicial import session
import socketio
import asyncio
import time

pedido_att = Blueprint('pedido_att', __name__, template_folder='templates')

# criar a lista pedido e deletar com


@pedido_att.route('/user/pedido/<int:id>', methods=['GET'])
@token_required
def pedidos(current_user, id):

    id_pedido = session.query(Pedido).filter_by(id=id).first()

    if not id_pedido:
        jsonify({'message': 'nao foi possivel encontrar pedido'})

    pedido_item = {}
    pedido_item['email'] = id_pedido.email
    pedido_item['num_pedido'] = id_pedido.num_pedido
    pedido_item['data_pedido'] = id_pedido.data_pedido
    pedido_item['quantidade'] = id_pedido.quantidade
    pedido_item['status'] = id_pedido.status
    pedido_item['frete'] = id_pedido.frete
    pedido_item['custo_total'] = id_pedido.custo_total

    return jsonify({'Pedido': pedido_item})


@pedido_att.route('/user/pedido/<int:id>', methods=['PUT'])
@token_required
def att_pedido(current_user, id):

    id_pedido = session.query(Pedido).filter_by(id=id).first()

    data_json = request.get_json()

    if not data_json:
        return jsonify({'message': 'Nenhum campo pode ficar vazio'})

    if not id_pedido:
        return jsonify({'message': 'Não encontrado pedido id'})

    # status preparando...
    if not data_json['Preparando...']:
        id_pedido.status = id_pedido.status

    else:
        id_pedido.status = data_json['Preparando...']

    # status enviado...
    if not data_json['Enviado']:
        id_pedido.status = id_pedido.status

    else:
        id_pedido.status = data_json['Enviado']

    # status entregue
    if not data_json['Entregue']:
        id_pedido.status = id_pedido.status

    else:
        id_pedido.status = data_json['Entregue']

    session.commit()
