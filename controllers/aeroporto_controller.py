from database import SessionLocal
from models import Aeroporto

def populate_aeroporto(aeroportos):
    return [{'id': aeroporto.id,
                        'nome': aeroporto.nome,
                        'cidade': aeroporto.cidade} for aeroporto in aeroportos]
    

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
    aeroportos_json = populate_aeroporto(aeroportos)
    session.close()
    return aeroportos_json
    
