import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from settings.settings import DATABASE_URL

# sys.path.append(os.path.abspath(os.path.dirname(os.getcwd()+"/passagens_aereas"))) #Necessário durante o  desenvolvimento


engine = create_engine(DATABASE_URL, convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from models import models

    Base.metadata.create_all(bind=engine)
