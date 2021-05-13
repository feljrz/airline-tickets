from flask.globals import session
from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine
from sqlalchemy.exc import DatabaseError
from sqlalchemy.orm import sessionmaker, relationship
from database import SessionLocal
from models import Aeroporto


def hw_add_aeroporto(request):
    session = SessionLocal()
    aeroporto = Aeroporto(nome=request["nome"], cidade=request["cidade"])
    print(aeroporto)
    session.add(aeroporto)
    session.commit()
    session.close()
    return {"message": "Adicionado"}

def  hw_list_aeroporto():
    session = SessionLocal()
    aeroportos = session.query(Aeroporto).order_by(Aeroporto.nome.asc()).all()
    list_aeroportos = [{'id': aeroporto.id,
                        'nome': aeroporto.nome,
                        'cidade': aeroporto.cidade} for aeroporto in aeroportos]
    session.close()
    return list_aeroportos
    