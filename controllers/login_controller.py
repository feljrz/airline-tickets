from flask.globals import session
from models.models import Cadastro
from database import SessionLocal
from flask_login import login_user, logout_user



def populate_cadastro(cadastros):
    return [
        {"id": cadastro.id, 
        "nome": cadastro.nome, 
        "email": cadastro.email,
        "senha": cadastro.senha} for cadastro in cadastros
    ]


def hw_load_user(id):
    session = SessionLocal()
    return session.query(Cadastro).filter_by(id = id).first()

def hw_get_cadastros():
    session = SessionLocal()
    cadastros = session.query(Cadastro).order_by(Cadastro.nome.asc()).all()
    cadastros_json = populate_cadastro(cadastros)
    session.close()
    return cadastros_json

def hw_add_cadastro(request):
    session = SessionLocal()
    cadastro = Cadastro(nome = request["nome"], email = request["email"], senha = request["senha"])
    cadastro_json = populate_cadastro([cadastro])
    session.add(cadastro)
    session.commit()
    session.close()
    return cadastro_json

def hw_login(request):
    session = SessionLocal()
    user = session.query(Cadastro).filter_by(email = request['email'], senha = request['senha']).first()
    login_user(user)
    session.close()
    return 'Voce entrou'

def hw_logout():
    session = SessionLocal()
    logout_user()
    return 'Voce saiu'