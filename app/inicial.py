from flask import Flask
from sqlalchemy.orm import sessionmaker
from app.models import engine
from pymongo import MongoClient


app = Flask(__name__)
Session = sessionmaker(bind=engine)
session = Session()


#database = MongoClient('localhost', 27017)
#clientedb = database['clientes']
#empresa = database['empresas']
#usuarios = database['usuarios']