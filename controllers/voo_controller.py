from datetime import datetime, timedelta

from sqlalchemy.sql import text

from database import SessionLocal
from models import Aeroporto, Voo


def populate_aeroporto(aeroportos):
    return [
        {"id": aeroporto.id, "nome": aeroporto.nome, "cidade": aeroporto.cidade}
        for aeroporto in aeroportos
    ]


def populate_voo(voos):
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
        }
        for voo in voos
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


def hw_add_voo(request):
    session = SessionLocal()
    voo = Voo(
        data=datetime.strptime(request["data"], "%d/%m/%Y %H:%M:%S"),
        destino=request["destino"],
        companhia=request["companhia"],
        capacidade=request["capacidade"],
        ocupacao=request["ocupacao"],
        preco=request["preco"],
        id_aeroporto=request["id_aeroporto"],
    )
    session.add(voo)
    session.commit()
    voo_json = hw_get_voo(voo.id)
    session.close()
    return voo_json


def hw_get_voos():
    session = SessionLocal()
    voos = session.query(Voo).order_by(Voo.data.asc()).all()
    voos_json = populate_voo(voos)
    session.close()
    return voos_json


def hw_get_voos_aeroportos():
    session = SessionLocal()
    voos = session.query(Voo).order_by(Voo.data.asc()).all()
    voos_json = populate_voo_aeroporto(voos)
    session.close()
    return voos_json


def hw_get_voo(id):
    session = SessionLocal()
    voo = session.query(Voo).filter_by(id=id).all()
    voo_json = populate_voo(voo)
    session.close()
    return voo_json


def hw_remove_voo(id):
    session = SessionLocal()
    voo = session.query(Voo).filter_by(id=id).first()
    session.delete(voo)
    session.commit()
    session.close()
    return {"message": f"Voo {voo.id} was deleted"}


def hw_update_voo(request):
    session = SessionLocal()
    voo_old = session.query(Voo).filter_by(id=request["id"]).first()
    session.delete(voo_old)
    voo = Voo(
        id=request["id"],
        data=datetime.strptime(request["data"], "%d/%m/%Y %H:%M:%S"),
        destino=request["destino"],
        companhia=request["companhia"],
        capacidade=request["capacidade"],
        ocupacao=request["ocupacao"],
        preco=request["preco"],
    )
    session.add(voo)
    session.commit()
    voo_json = hw_get_voo(voo.id)
    session.close()
    return voo_json


# 4
def hw_get_aeroporto_by_company(company):
    session = SessionLocal()
    voos_company = session.query(Voo).filter_by(companhia=company).all()

    voos_company_json = populate_voo_aeroporto(voos_company)
    cidades_destino = [elem["aeroporto"][0] for elem in voos_company_json]
    session.close()
    return cidades_destino


# 6
def hw_get_voos_companhia(request):
    session = SessionLocal()
    date = datetime.strptime(request["data"] + " 00:00:00", "%d/%m/%Y %H:%M:%S")
    time_after = date + timedelta(hours=23, minutes=59, seconds=59)
    voos = (
        session.query(Voo)
        .filter(Voo.data >= date, Voo.data <= time_after)
        .filter_by(companhia=request["companhia"])
        .all()
    )
    voos_json = populate_voo_aeroporto(voos)
    session.close()
    return voos_json


# 7
def hw_get_voos_passageiros(n):
    session = SessionLocal()
    voos_disponibilidade = (
        session.query(Voo, (Voo.capacidade - Voo.ocupacao).label("disponibilidade"))
        .filter(text(f"disponibilidade > {n}"))
        .order_by(Voo.preco.asc())
        .all()
    )
    voo_list = [voo[0] for voo in voos_disponibilidade]
    voos_json = populate_voo_aeroporto(voo_list)
    session.close()
    return voos_json
