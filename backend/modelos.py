from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

class Membro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(50), nullable=False)

    __table_args__ = (
        CheckConstraint('LENGTH(nome) >= 5', name='nome_min_length'),
        CheckConstraint('LENGTH(senha) >= 3', name='senha_min_length'),
    )

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(140))
    finalizada = db.Column(db.Boolean, default=False, nullable=False)
    data_termino = db.Column(db.DateTime)
    prioridade = db.Column(db.Enum('Baixa', 'Média', 'Alta'), default='Baixa', nullable=False)
    id_membro = db.Column(db.Integer, db.ForeignKey('membro.id'), nullable=False)
    membro = db.relationship('Membro', backref=db.backref('tarefas', lazy=True))

    __table_args__ = (
        CheckConstraint('LENGTH(nome) >= 5', name='nome_min_length'),
        CheckConstraint('LENGTH(nome) <= 50', name='nome_max_length'),
        CheckConstraint('LENGTH(descricao) <= 140', name='descricao_max_length'),
    )
