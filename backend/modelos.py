from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()   

class Membro(Base):
    __tablename__ = 'membro'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    nome = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)

    tarefas = relationship("Tarefa", back_populates="membro")

    def __init__(self, email, nome, senha):
        self.email = email
        self.nome = nome
        self.senha = senha

