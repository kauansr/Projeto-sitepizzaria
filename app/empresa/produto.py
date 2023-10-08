from flask import Blueprint, jsonify, request, abort
from app.middlewares import token_required
from app.models import Produtos, Pedido, Empresa
from app.inicial import session
import socket
from flask_cors import CORS


produtos = Blueprint('produto', __name__, template_folder='templates')

"""
API dos produtos
"""

CORS(produtos, resources={r"/user/empresa/produtos/*": {"origins": "http://localhost:3000"}})

@produtos.route('/user/empresa/produtos', methods=['GET'])
@token_required
def listar_produtos(current_user):

    """
    Pega todos produtos

    :param User current_user: dados dos usuarios
    :return: Json
    """


    produtos = session.query(Produtos).all()

    if not produtos:
        return abort(404)

    output = [] 

    for produto in produtos:
        produto_data = {}
        produto_data['id'] = produto.id
        produto_data['nome_produto'] = produto.produto_nome
        produto_data['produto_preco'] = produto.produto_preco
        output.append(produto_data)
    
    return jsonify({'Produto': output})

@produtos.route('/user/empresa/produtos/<int:id>', methods=['GET'])
@token_required
def ver_um_produtos(current_user,id):

    """
    Pega um produto

    :param User current_user: dados do usuario
    :param int id: dados da rota id
    :return: Json
    """



    produto = session.query(Produtos).filter_by(id=id).first()

    if not produto:
        return abort(404)

    produto_data = {}

    produto_data['id'] = produto.id
    produto_data['produto_nome'] = produto.produto_nome
    produto_data['produto_preco'] = produto.produto_preco
    

    return jsonify({'produto': produto_data})


@produtos.route('/user/empresa/produtos', methods=['POST'])
@token_required
def adicionar_produtos(current_user):

    """
    Adiciona um produto

    :param User current_user: dados do usuario
    :return: Json
    """

    id_empresa = session.query(Empresa).filter_by(user_id=current_user.id).first()

    if not id_empresa:
        return abort(401)
    produto_data = request.get_json()


    if not produto_data :
        return jsonify({'message':'Nao foi possivel adicionar produto,tente novamente'})


    new_product = Produtos(produto_nome=produto_data['produto_nome'],  
                           produto_preco=produto_data['produto_preco'])

    session.add(new_product)
    session.commit()

    return jsonify({'info_message':'Produto adicionado'})

@produtos.route('/user/empresa/produtos/<int:id>', methods=['DELETE'])
@token_required
def deletar_produtos(current_user,id):

    """
    Deletar produto

    :param User current_user: dados do usuario
    :param int id: dados da rota id
    :return: Json
    """

    id_empresa = session.query(Empresa).filter_by(user_id=current_user.id).first()

    if not id_empresa:
        return abort(401)
    
    num_prod = session.query(Produtos).filter_by(id=id).first()

    if not num_prod:
        return abort(404)

    session.delete(num_prod)
    session.commit()

    return jsonify({'info_message': 'Produto deletado com sucesso'})

@produtos.route('/user/empresa/produtos/<int:id>', methods=['PUT'])
@token_required
def atualizar_produto(current_user, id):

    """
    Atualiza um produto

    :param User current_user: dados do usuario
    :param int id: dados da rota id
    :return: Json
    """

    id_empresa = session.query(Empresa).filter_by(user_id=current_user.id).first()

    if not id_empresa:
        return abort(401)

    data_json = request.get_json()
    
    id_pedido = session.query(Produtos).filter_by(id=id).first()

    

    if not data_json:
        return jsonify({'message': 'Nenhum campo pode ficar vazio'})

    if not id_pedido:
        return abort(404)

  
    if not data_json['produto_nome'] or data_json['produto_nome'] == '':
        id_pedido.produto_nome = id_pedido.produto_nome

    else:
        id_pedido.produto_nome = data_json['produto_nome']


   
    if not data_json['produto_preco'] or data_json['produto_preco'] == '':
        id_pedido.produto_preco = id_pedido.produto_preco

    else:
        id_pedido.produto_preco = data_json['produto_preco']

  

    session.commit()

    return jsonify({'info_message':'O produto foi atualizado'})

