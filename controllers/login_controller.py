import hashlib

from flask.globals import session
from flask_login import login_user, logout_user

from database import SessionLocal
from models.models import Cadastro


def populate_cadastro(cadastros):
    return [
        {
            "id": cadastro.id,
            "nome": cadastro.nome,
            "email": cadastro.email,
            "senha": cadastro.senha,
        }
        for cadastro in cadastros
    ]


def hw_load_user(id):
    session = SessionLocal()
    return session.query(Cadastro).filter_by(id=id).first()


def hw_get_cadastros():
    session = SessionLocal()
    cadastros = session.query(Cadastro).order_by(Cadastro.nome.asc()).all()
    cadastros_json = populate_cadastro(cadastros)
    session.close()
    return cadastros_json


def hw_add_cadastro(request):
    session = SessionLocal()
    senha = request["senha"]
    hash_obj = hashlib.md5(f"{senha}".encode())
    md5_value = hash_obj.hexdigest()
    cadastro = Cadastro(nome=request["nome"], email=request["email"], senha=md5_value)
    cadastro_json = populate_cadastro([cadastro])
    session.add(cadastro)
    session.commit()
    session.close()
    return cadastro_json


def hw_login(request):
    session = SessionLocal()
    senha = request["senha"]
    hash_obj = hashlib.md5(f"{senha}".encode())
    md5_value = hash_obj.hexdigest()
    user = (
        session.query(Cadastro)
        .filter_by(email=request["email"], senha=md5_value)
        .first()
    )
    login_user(user)
    session.close()
    return "Voce entrou"


def hw_logout():
    session = SessionLocal()
    logout_user()
    return "Voce saiu"
