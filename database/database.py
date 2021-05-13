from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

import sys, os

# sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd()+"/passagens_aereas")))
for d in sys.path:
    print(d)

from settings.settings import DATABASE_URL

x = 10
# print(DATABASE_URL)
