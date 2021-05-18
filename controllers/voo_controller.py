from flask.globals import session

from database import SessionLocal
from models import Voo


def hw_list_voos(date, company):
    session = SessionLocal()
    voos = session.query(Voo).filter_by(data=date, companhia=company).all()
    list_voos = [
        {
            "id": voo.id,
            "data": voo.data,
            "destino": voo.destino,
        }
        for voo in voos
    ]
    session.close()
    return list_voos
