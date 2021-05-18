from flask.globals import session
from database import SessionLocal
from models import Voo

def populate_voo(voos):
    return [{'id' : voo.id,
                  'data' : voo.data,
                  'destino' : voo.destino,} for voo in voos]

def hw_list_voos(date, company):
    session = SessionLocal()
    voos = session.query(Voo).filter_by(data=date, companhia=company).all()
    voos_json = populate_voo(voos)
    session.close()
    return voos_json