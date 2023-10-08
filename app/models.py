from werkzeug.security import check_password_hash
import sqlalchemy
from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship

engine = sqlalchemy.create_engine('sqlite:///pizzaria.db', echo=True)


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id: int = Column(Integer, primary_key=True, nullable=False)
    email: str = Column(String(50), nullable=False, unique=True)
    name: str = Column(String(50), nullable=False)
    time_created: datetime = Column(DateTime, default=datetime.now)
    status_log: bool = Column(Boolean, default=False)
    age: str = Column(Integer, nullable=False)
    password: str = Column(String(80), nullable=False)
    empresa = relationship('Empresa', cascade='all,delete',backref='users')
    pedido = relationship('Pedido',cascade='all,delete', backref='pedidos')

    def verifica_password(self, pwd):
        return check_password_hash(self.password, pwd)

    def __str__(self) -> str:
        return self.name

    def __init__(self, name, email,  age, password) -> None:
        self.name = name
        self.email = email
        self.age = age
        self.password = password
    
    def is_authenticated(self):
        return True
    


class Empresa(Base):
    __tablename__ = 'empresa'
    id: int = Column(Integer, primary_key=True,
                     autoincrement=True, unique=True)
    user_id: str = Column(String, ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    empresa: str = Column(String(50), nullable=False)
    cnpj: str = Column(String(20), nullable=False)
    is_admin: bool = Column(Boolean, default=False)

    def __init__(self, empresa, cnpj, user_id, is_admin) -> None:
        self.empresa = empresa
        self.cnpj = cnpj
        self.user_id = user_id
        self.is_admin = is_admin
    



class Produtos(Base):
    __tablename__ = 'produtos'
    id: int = Column(Integer, primary_key=True,
                     autoincrement=True, unique=True)
    produto_nome: str = Column(String(50))
    produto_preco: float = Column(Float)
    pedido_nome = relationship('Pedido', backref='produtos') 

    def __init__(self, produto_nome, produto_preco) -> None:
        self.produto_nome = produto_nome
        self.produto_preco = produto_preco


class Pedido(Base):
    __tablename__ = 'pedido'
    id: int = Column(Integer, primary_key=True, nullable=False)
    email: str = Column(String(50), ForeignKey(
        'user.email', ondelete='CASCADE'), nullable=False)
    pedido_nome: str = Column(String(50), ForeignKey(
        'produtos.produto_nome', ondelete='CASCADE'
    ), nullable=False)
    data_pedido: datetime = Column(DateTime, default=datetime.now)
    status: str = Column(String(30),  nullable=False)
    frete: float = Column(Float)
    custo_total: float = Column(Float)

    def __init__(self, email, pedido_nome, status, frete, custo_total) -> None:
        self.email = email
        self.pedido_nome = pedido_nome
        self.status = status
        self.frete = frete
        self.custo_total = custo_total


Base.metadata.create_all(engine)
