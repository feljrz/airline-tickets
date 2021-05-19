from datetime import datetime

from database import SessionLocal
from models import Aeroporto, Voo


def populate_aeroporto(aeroportos):
    return [
        {"id": aeroporto.id, "nome": aeroporto.nome, "cidade": aeroporto.cidade}
        for aeroporto in aeroportos
    ]


def populate_voo_aeroporto(voos):
    return [
        {
            "id": voo.id,
            "data": datetime.strftime(voo.data, "%d/%m/%Y %H:%M:%S"),
            "destino": voo.destino,
            "companhia": voo.companhia,
            "capacidade": voo.capacidade,
            "ocupacao": voo.ocupacao,
            "preco": voo.preco,
            "id_aeroporto": voo.id_aeroporto,
            "aeroporto": populate_aeroporto([voo.aeroporto]),
        }
        for voo in voos
    ]


def hw_add_aeroporto(request):
    session = SessionLocal()
    aeroporto = Aeroporto(nome=request["nome"], cidade=request["cidade"])
    aeroporto_json = populate_aeroporto([aeroporto])
    session.add(aeroporto)
    session.commit()
    session.close()
    return aeroporto_json


def hw_get_aeroportos():
    session = SessionLocal()
    aeroportos = session.query(Aeroporto).order_by(Aeroporto.nome.asc()).all()
    aeroportos_json = populate_aeroporto(aeroportos)
    session.close()
    return aeroportos_json


def hw_get_aeroporto(id):
    session = SessionLocal()
    aeroporto = (
        session.query(Aeroporto).filter_by(id=id).all()
    ) 
    aeroporto_json = populate_aeroporto(aeroporto)
    session.close()
    return aeroporto_json


def hw_remove_aeroporto(id):
    session = SessionLocal()
    aeroporto = (
        session.query(Aeroporto).filter_by(id=id).first()
    )  
    session.delete(aeroporto)
    session.commit()
    session.close()
    return {"message": f"Aeroporto {aeroporto.id} was deleted"}


def hw_update_aeroporto(request):
    session = SessionLocal()
    aeroporto_old = session.query(Aeroporto).filter_by(id=request["id"]).first()
    session.delete(aeroporto_old)
    aeroporto = Aeroporto(
        id=request["id"], nome=request["nome"], cidade=request["cidade"]
    )
    session.add(aeroporto)
    session.commit()
    aeroporto_json = hw_get_aeroporto(aeroporto.id)
    session.close()
    return aeroporto_json


# 5
def hw_get_aeroportos_destino(origem):
    session = SessionLocal()
    voo_origem = (
        session.query(Voo).join(Aeroporto).filter(Aeroporto.cidade == origem).all()
    )
    voo_origem_json = populate_voo_aeroporto(voo_origem)
    destinos = [{"destino": elem["destino"]} for elem in voo_origem_json]
    return destinos
