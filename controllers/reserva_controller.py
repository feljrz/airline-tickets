import hashlib
from datetime import datetime

from database import SessionLocal
from models import Reserva


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


def populate_reserva(reservas):
    return [
        {
            "id": reserva.id,
            "id_voo": reserva.id_voo,
            "id_cadastro": reserva.id_cadastro,
            "e_ticket": None if reserva.e_ticket is None else reserva.e_ticket,
            "voo": populate_voo_aeroporto([reserva.voo]),
            "cadastro": populate_cadastro([reserva.cadastro]),
        }
        for reserva in reservas
    ]


# 8
def hw_add_reserva(request):
    session = SessionLocal()
    reserva = Reserva(id_voo=request["id_voo"], id_cadastro=request["id_cadastro"])
    session.add(reserva)
    session.commit()
    hash_obj = hashlib.md5(f"{reserva.id}".encode())
    md5_value = hash_obj.hexdigest()
    reserva.e_ticket = md5_value
    session.add(reserva)
    session.commit()
    reserva_json = hw_get_reserva(reserva.id)
    session.close()
    return reserva_json


def hw_get_reservas():
    session = SessionLocal()
    reservas = session.query(Reserva).all()
    reserva_json = populate_reserva(reservas)
    return reserva_json


def hw_remove_reserva(id):
    session = SessionLocal()
    reserva = session.query(Reserva).filter_by(id=id).first()
    session.delete(reserva)
    session.commit()
    session.close()
    return {"message": f"Reserva {reserva.id} was deleted"}


def hw_update_reserva(request):
    session = SessionLocal()
    reserva_old = session.query(Reserva).filter_by(id=request["id"]).first()
    session.delete(reserva_old)
    reserva = Reserva(
        id_voo=request["id_voo"],
        id_cadastro=request["id_cadastro"],
        e_ticket=request["e_ticket"],
    )
    session.add(reserva)
    session.commit()
    reserva_json = hw_get_reserva(reserva.id)
    session.close()
    return reserva_json


def hw_get_reserva(id):
    session = SessionLocal()
    reserva = session.query(Reserva).filter_by(id=id).first()
    reserva_json = populate_reserva([reserva])
    return reserva_json
