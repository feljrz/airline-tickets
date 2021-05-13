from sqlalchemy import Column, Integer, String, Table, Sequence, ForeignKey, Float, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from database import Base
from datetime import date, datetime


class Aeroporto(Base):
    __tablename__ = 'aeroporto'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    voos = relationship("Voo", back_populates="aeroporto")

class Voo(Base):
    __tablename__ = 'voo'
    id = Column(Integer, primary_key=True)
    destino = Column(String(100), nullable=False)
    companhia = Column(String(100), nullable=False)
    data = Column(DateTime)
    capacidade = Column(Integer, nullable=False)
    ocupacao  = Column(Integer, nullable=False)
    preco = Column(Float)
    id_aeroporto = Column(Integer, ForeignKey('aeroporto.id'))
    aeroporto = relationship("Aeroporto", back_populates="voos")

