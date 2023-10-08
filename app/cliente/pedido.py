from flask import jsonify, Blueprint, request,abort
from app.models import Pedido, Produtos, User
from app.middlewares import token_required
from app.inicial import session
from flask_cors import CORS

pedido = Blueprint('pedido', __name__, template_folder='templates')

"""
API dos pedidos, Crud (Create, Read, Update, Delete), O CORS serve para permitir
o front-end react acesse as rotas
"""

CORS(pedido, resources={r"/pedidos/*": {"origins": "http://localhost:3000"}})

@pedido.route('/pedidos', methods=['GET'])
@token_required
def Pedidos_all(current_user):

    """
    Pega todos os pedidos do cliente logado

    :param User current_user: dados do usuario decodificado
    :return: Json
    """

    pedidos_info = session.query(Pedido).filter_by(email=current_user.email).all()

    if not current_user:
        return jsonify({'message': 'Nao existe token'})


    output = []

    for pedidos in pedidos_info:
        user_data = {}
        user_data['id'] = pedidos.id
        user_data['nome'] = pedidos.pedido_nome
        user_data['email'] = pedidos.email
        user_data['data_pedido'] = pedidos.data_pedido
        user_data['status'] = pedidos.status
        user_data['frete'] = pedidos.frete
        user_data['custo_total'] = pedidos.custo_total

        output.append(user_data)

    return jsonify({'pedidos': output})

@pedido.route('/pedidos/<int:id>', methods=['GET'])
@token_required
def pedidos(current_user, id):

    """
    Pega um pedido do usuario

    :param User current_user: dados do usuario decodificado
    :param int id: dados da rota id
    :return: Json
    """

    id_user = session.query(User).filter_by(id=current_user.id).first()

    if not id_user:
        return jsonify({'message': 'Nao existe token'})

    pedido_id = session.query(Pedido).filter_by(id=id).first()

    if not pedido_id:
        return abort(204)
    

    if not pedido_id:
        jsonify({'message': 'nao foi possivel encontrar pedido'})

    pedido_item = {}
    pedido_item['email'] = pedido_id.email
    pedido_item['data_pedido'] = pedido_id.data_pedido
    pedido_item['status'] = pedido_id.status
    pedido_item['frete'] = pedido_id.frete
    pedido_item['custo_total'] = pedido_id.custo_total

    return jsonify({'Pedido': pedido_item})


@pedido.route('/pedidos/<int:id>', methods=['POST'])
@token_required
def criar_pedidos(current_user, id):

    """
    Cria um pedido

    :param User current_user: dados do usuario decodificado
    :param int id: dados da rota id
    :return: Json
    """


    id_produtos = session.query(Produtos).filter_by(id=id).first()

    if not id_produtos:
        return jsonify({'message': 'Nao foi possivel criar seu pedido'})



    email_user = session.query(User).filter_by(id=current_user.id).first()

    if not email_user:
        return jsonify({'Message': 'nao foi possivel concluir seu pedido'})

    pedido_lista = Pedido(email=email_user.email, pedido_nome=id_produtos.produto_nome,
                          status='preparando...', frete=id_produtos.produto_preco, custo_total=id_produtos.produto_preco)

    session.add(pedido_lista)
    session.commit()
    return jsonify({'Message': 'pedido criado'})


@pedido.route('/pedidos/<int:id>', methods=['DELETE'])
@token_required
def cancelar_pedido(current_user, id):

    """
    Cancela um pedido do usuario

    :param User current_user: dados do usuario decodificado
    :param int id: dados da rota id
    :return: Json
    """


    user = session.query(User).filter_by(email=current_user.email).first()
    if not user:
        return abort(401)

    id_pedido = session.query(Pedido).filter_by(id=id).first()

    if not id_pedido:
        return jsonify({'message': 'nao foi possivel achar pedido'})

    session.delete(id_pedido)
    session.commit()

    return jsonify({'info_message': 'Pedido deletado!'})


