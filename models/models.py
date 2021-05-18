from datetime import date, datetime

from sqlalchemy import (Column, Date, DateTime, Float, ForeignKey, Integer,
                        Sequence, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

from database import Base


class Aeroporto(Base):
    __tablename__ = "aeroporto"
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    voos = relationship("Voo", back_populates="aeroporto")


class Voo(Base):
    __tablename__ = "voo"
    id = Column(Integer, primary_key=True)
    destino = Column(String(100), nullable=False)
    companhia = Column(String(100), nullable=False)
    data = Column(DateTime )
    capacidade = Column(Integer, nullable=False)
    ocupacao = Column(Integer, nullable=False)
    preco = Column(Float)
    id_aeroporto = Column(Integer, ForeignKey("aeroporto.id")) #Acho que não é necessário POSSO ESTAR ENGANADO
    aeroporto = relationship("Aeroporto", back_populates="voos") # vai ser sempre o de origem 
