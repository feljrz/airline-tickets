# from flask.globals import session
# from models.models import Aeroporto
from database import SessionLocal
from models import Voo, Aeroporto
from datetime import datetime



def populate_aeroporto(aeroportos):
    return [{'id': aeroporto.id,
                        'nome': aeroporto.nome,
                        'cidade': aeroporto.cidade} for aeroporto in aeroportos]

def populate_voo(voos):
    return [{'id' : voo.id,
                  'data' : datetime.strftime(voo.data, "%d/%m/%Y %H:%M:%S"),
                  'destino' : voo.destino,
                  'companhia': voo.companhia,
                  'capacidade':voo.capacidade,
                  'ocupacao': voo.ocupacao,
                  'preco': voo.preco,
                  'id_aeroporto': voo.id_aeroporto} for voo in voos]

def populate_voo_aeroporto(voos):
    return [{'id' : voo.id,
                  'data' : voo.data,
                  'destino' : voo.destino,
                  'companhia': voo.companhia,
                  'capacidade':voo.capacidade,
                  'ocupacao': voo.ocupacao,
                  'preco': voo.preco,
                  'id_aeroporto': voo.id_aeroporto,
                  'aeroporto': populate_aeroporto([voo.aeroporto])} for voo in voos]



def hw_add_voo(request):
    print("-----------------------------hw_add_voo---------------------------")
    session = SessionLocal()
    voo = Voo(data=datetime.strptime(request["data"], "%d/%m/%Y %H:%M:%S"), 
            destino=request["destino"], 
            companhia=request["companhia"], 
            capacidade=request["capacidade"],
            ocupacao=request["ocupacao"], 
            preco=request["preco"],
            id_aeroporto=request["id_aeroporto"])
    print(voo.data)
    voo_json = populate_voo([voo])
    session.add(voo)
    session.commit()
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
    voo_old = session.query(Voo).filter_by(id=request['id']).first()
    session.delete(voo_old)
    voo = Voo(id=request['id'],
            data=datetime.strptime(request["data"], "%d/%m/%Y %H:%M:%S"), 
            destino=request["destino"], 
            companhia=request["companhia"], 
            capacidade=request["capacidade"],
            ocupacao=request["ocupacao"], 
            preco=request["preco"])
    session.add(voo)
    session.commit()
    voo_json = hw_get_voo(voo.id)
    session.close()
    # voo_json = populate_voo([voo])
    return voo_json



def hw_get_aeroporto_by_company(company):
    session = SessionLocal()
    voos_company = session.query(Voo).filter_by(companhia=company).all()
    print(voos_company['aeroporto']['cidade'])
    voos_company_json = populate_voo_aeroporto(voos_company)
    cidades_destino = []
    for voos_company_ele in voos_company_json:
        cidades_destino.append(voos_company_ele['aeroporto']['cidade'])
        print(voos_company_ele)
    
    session.close()
    return {"message": "aaaaaaaaa"}

#5
def hw_get_aeroportos_destino(origem):
    session = SessionLocal()
    voo_origem = session.query(Voo).join(Aeroporto).filter(Aeroporto.cidade == origem).all()
    voo_origem_json = populate_voo_aeroporto(voo_origem)
    destinos = [{"destino": elem["destino"]} for elem in voo_origem_json]
    return destinos


def hw_list_voos(date, company):
    session = SessionLocal()
    voos = session.query(Voo).filter_by(datetime.strftime(Voo.data, "%d/%m/%Y %H:%M:%S").date()==date, companhia=company).all()
    voos_json = populate_voo(voos)
    session.close()
    return voos_json


def hw_search_voos(n):
    session = SessionLocal()
    voos = session.query(Voo).filter((Voo.capacidade-Voo.ocupacao)>n).order_by(Voo.preco.asc()).all()
    voos_json = populate_voo(voos)
    session.close()
    return voos_json