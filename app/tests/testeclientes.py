import pytest
import requests

"""
TESTE DA PARTE CLIENTE.

Esse teste foi criado para testar as rotas do cliente e sua api,
dentre elas todos os metodos sao para testar com e sem autenticacao jwt.
"""
ENDPOINT = 'http://localhost:5000/user'
class TestClient:

    

    def test_all_clients_return_401(self):
        """
        TESTA A ROTA TODOS CLIENTES E RETORNA 401 POIS FALTA O JWT
        """
        assert requests.get(ENDPOINT).status_code == 401

    def test_one_client_return_401(self):
        """
        TESTA A ROTA UM CLIENTE E RETORNA 401 POIS FALTA O JWT
        """
        assert requests.get(f'{ENDPOINT}/{1}').status_code == 401


    def test_put_client_return_401(self):
        """
        TESTA A ROTA DE ATUALIZACAO E RETORNA 401 POIS FALTA O JWT
        """
        assert requests.put(f'{ENDPOINT}/{1}').status_code == 401

    def test_delete_client_return_401(self):
        """
        TESTA A ROTA DE DELETE E RETORNA 401 POIS FALTA O JWT
        """
        assert requests.delete(f'{ENDPOINT}/{1}').status_code == 401