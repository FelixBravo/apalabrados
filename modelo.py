from sqlalchemy import Column, String, Integer, CHAR

from base import Base

class Numero(Base):
    __tablename__ = 'numeros'

    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    acumulado = Column(Integer)

    def __init__(self,
                numero,
                acumulado):
        self.numero = numero
        self.acumulado = acumulado

class Texto(Base):
    __tablename__ = 'textos'

    id = Column(Integer, primary_key=True)
    texto = Column(String)
    inicial = Column(CHAR)
    final = Column(CHAR)

    def __init__(self,
                texto,
                inicial,
                final):
        self.texto = texto
        self.inicial = inicial
        self.final = final

class Caracter(Base):
    __tablename__ = 'caracteres'

    id = Column(Integer, primary_key=True)
    caracter = Column(CHAR)

    def __init__(self,
                caracter):
        self.caracter = caracter
