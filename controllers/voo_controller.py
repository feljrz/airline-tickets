from flask.globals import session
from database import SessionLocal
from models import Voo


def populate_aeroporto(aeroportos):
    return [{'id': aeroporto.id,
                        'nome': aeroporto.nome,
                        'cidade': aeroporto.cidade} for aeroporto in aeroportos]

def populate_voo(voos):
    return [{'id' : voo.id,
                  'data' : voo.data,
                  'destino' : voo.destino,
                  'companhia': voo.companhia,
                  'capacidade':voo.capacidade,
                  'ocupacao': voo.ocupacao,
                  'preco': voo.preco,} for voo in voos]

def populate_voo_aeroporto(voos):
    return [{'id' : voo.id,
                  'data' : voo.data,
                  'destino' : voo.destino,
                  'companhia': voo.companhia,
                  'capacidade':voo.capacidade,
                  'ocupacao': voo.ocupacao,
                  'preco': voo.preco,
                  'aeroporto': populate_aeroporto(voo.aeroporto)} for voo in voos]



def hw_add_voo(request):
    session = SessionLocal()
    voo = Voo(destino=request["destino"], companhia=request["companhia"], capacidade=request["capacidade"],
             ocupacao=request["ocupacao"], preco=request["preco"])
    voo_json = populate_voo([voo])
    print('oi')
    session.add(voo)
    print('oiii')
    session.commit()
    print("oiiiiiii")
    session.close()
    return voo_json

def hw_get_voos():
    session = SessionLocal()
    voos = session.query(Voo).order_by(Voo.data.asc()).all()
    voos_json = populate_voo(voos)
    session.close()
    return voos_json

def hw_get_voo(id):
    session = SessionLocal()
    voo = session.query(Voo).filter_by(id=id).all()
    voo_json = populate_voo(voo)
    session.close()
    return voo_json



def hw_list_voos(date, company):
    session = SessionLocal()
    voos = session.query(Voo).filter_by(data=date, companhia=company).all()
    voos_json = populate_voo(voos)
    session.close()
    return voos_json