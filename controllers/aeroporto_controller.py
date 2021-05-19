from database import SessionLocal
from models import Aeroporto

def populate_aeroporto(aeroportos):
    return [{'id': aeroporto.id,
                        'nome': aeroporto.nome,
                        'cidade': aeroporto.cidade} for aeroporto in aeroportos]
    
# aeroporto(where origem == x) . voos(destino == y) 
def hw_destinos(origem):
    # session = SessionLocal()
    pass







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
    aeroporto = session.query(Aeroporto).filter_by(id=id).all() #Verificar se existe mais de um
    print(aeroporto)
    aeroporto_json = populate_aeroporto(aeroporto)
    session.close()
    return aeroporto_json

def hw_remove_aeroporto(id):
    session = SessionLocal()
    aeroporto = session.query(Aeroporto).filter_by(id=id).first() #Verificar se existe mais de um
    session.delete(aeroporto)
    session.commit()
    session.close()
    return {"message": f"Aeroporto {aeroporto.id} was deleted"}

def hw_update_aeroporto(request):
    session = SessionLocal()
    aeroporto_old = session.query(Aeroporto).filter_by(id=request['id']).first()
    session.delete(aeroporto_old)
    aeroporto = Aeroporto(id = request['id'], nome=request["nome"], cidade=request["cidade"])
    session.add(aeroporto)
    session.commit()
    aeroporto_json = hw_get_aeroporto(aeroporto.id)
    session.close()
    return aeroporto_json

