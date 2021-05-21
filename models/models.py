from datetime import date, datetime

from flask_login import UserMixin
from sqlalchemy import (Column, Date, DateTime, Float, ForeignKey, Integer,
                        Sequence, String, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.sqltypes import VARCHAR

from database import Base


class Reserva(Base):
    __tablename__ = "reserva"
    id = Column(Integer, primary_key=True)
    id_voo = Column(Integer, ForeignKey("voo.id"))
    id_cadastro = Column(Integer, ForeignKey("cadastro.id"))
    e_ticket = Column(String(45))
    voo = relationship("Voo", back_populates="reservas")
    cadastro = relationship("Cadastro", back_populates="reservas")


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
    data = Column(DateTime)
    capacidade = Column(Integer, nullable=False)
    ocupacao = Column(Integer, nullable=False)
    preco = Column(Float)
    id_aeroporto = Column(Integer, ForeignKey("aeroporto.id"))
    aeroporto = relationship("Aeroporto", back_populates="voos")
    reservas = relationship("Reserva", back_populates="voo")


class Cadastro(UserMixin, Base):
    __tablename__ = "cadastro"
    id = Column(Integer, primary_key=True)
    nome = Column(String(245), nullable=False)
    email = Column(String(45), nullable=False)
    senha = Column(String(45), nullable=False)
    reservas = relationship("Reserva", back_populates="cadastro")
