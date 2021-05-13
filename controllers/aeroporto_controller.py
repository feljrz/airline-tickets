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
