from flask import Blueprint, jsonify, request
from app.middlewares import token_required
from app.models import Produtos, Pedido
from app.inicial import session
import socket


produtos = Blueprint('produto', __name__, template_folder='templates')

@produtos.route('/user/empresa/produtos', methods=['GET'])
@token_required
def listar_produtos(current_user):
    produtos = session.query(Produtos).all()

    output = [] 

    for produto in produtos:
        produto_data = {}
        produto_data['id'] = produto.id
        produto_data['quantidade'] = produto.quantidade
        produto_data['nome_produto'] = produto.produto_nome
        produto_data['produto_preco'] = produto.produto_preco
        output.append(produto_data)
    
    return jsonify({'Produto': output})

@produtos.route('/user/empresa/produtos/<int:id>', methods=['GET'])
@token_required
def ver_um_produtos(current_user,id):
    produto = session.query(Produtos).filter_by(id=id).first()

    if not produto:
        return jsonify({'message':'Nenhum produto encontrado'})

    produto_data = {}

    produto_data['id'] = produto.id
    produto_data['produto_nome'] = produto.produto_nome
    produto_data['quantidade'] = produto.quantidade
    produto_data['produto_preco'] = produto.produto_preco

    return jsonify({'produto': produto_data})


@produtos.route('/user/empresa/produtos/', methods=['POST'])
@token_required
def adicionar_produtos(current_user):
    produto_data = request.get_json()


    if not produto_data :
        return jsonify({'message':'Nao foi possivel adicionar produto,tente novamente'})


    new_product = Produtos(produto_nome=produto_data['produto_nome'], quantidade=produto_data['quantidade'], 
                           produto_preco=produto_data['produto_preco'])

    session.add(new_product)
    session.commit()

    return jsonify({'message':'Produto adicionado'})

@produtos.route('/user/empresa/produtos/<int:id>', methods=['DELETE'])
@token_required
def deletar_produtos(current_user,id):
    
    num_prod = session.query(Produtos).filter_by(id=id).first()

    if not num_prod:
        return jsonify({'message':'Produto nao encontrado'})

    session.delete(num_prod)
    session.commit()

    return jsonify({'message': 'Produto deletado com sucesso'})

@produtos.route('/user/empresa/produtos/<int:id>', methods=['PUT'])
@token_required
def atualizar_produto(current_user, id):


    
    num_prod = session.query(Produtos).filter_by(id=id).first()

    if not num_prod :
        return jsonify({'message':'Nao foi encontrado o produto'})

    num_prod.produto_nome = request.json['produto_nome']
    num_prod.quantidade = request.json['quantidade']
    num_prod.produto_preco = request.json['produto_preco']

    session.commit()

    return jsonify({'message':'O produto foi atualizado'})

