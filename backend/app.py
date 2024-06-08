from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
import bcrypt
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:admin@localhost/to-do-list-web'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return 'Hello, Flask with SQLAlchemy!'

@app.route("/login")
@cross_origin(supports_credentials=True)
def login():
  return jsonify({'success': 'ok'})

@app.route('/membros', methods=['GET', 'POST'])
def manage_membros():
    if request.method == 'POST':
        data = request.json
        novo_membro = Membro(email=data['email'], nome=data['nome'], senha=data['senha'])
        db.session.add(novo_membro)
        db.session.commit()
        return jsonify({'message': 'Membro criado com sucesso!'}), 201

    membros = Membro.query.all()
    return jsonify([{'id': membro.id, 'email': membro.email, 'nome': membro.nome} for membro in membros])

@app.route('/membros/<int:id_membro>', methods=['GET'])
def get_membro(id_membro):
    membro = Membro.query.get_or_404(id_membro)
    return jsonify({'id': membro.id, 'email': membro.email, 'nome': membro.nome})

@app.route('/tarefas', methods=['GET', 'POST'])
def manage_tarefas():
    if request.method == 'POST':
        data = request.json
        nova_tarefa = Tarefa(
            nome=data['nome'],
            descricao=data.get('descricao'),
            prioridade=data['prioridade'],
            id_membro=data['id_membro']
        )
        db.session.add(nova_tarefa)
        db.session.commit()
        return jsonify({'message': 'Tarefa criada com sucesso!'}), 201

    tarefas = Tarefa.query.all()
    return jsonify([{'id': tarefa.id, 'nome': tarefa.nome, 'descricao': tarefa.descricao, 'finalizada': tarefa.finalizada, 'data_termino': tarefa.data_termino, 'prioridade': tarefa.prioridade, 'id_membro': tarefa.id_membro} for tarefa in tarefas])

@app.route('/tarefas/<int:id_tarefa>', methods=['GET', 'PUT', 'DELETE'])
def manage_tarefa(id_tarefa):
    tarefa = Tarefa.query.get_or_404(id_tarefa)

    if request.method == 'PUT':
        data = request.json
        if tarefa.finalizada:
            return jsonify({'message': 'Tarefas finalizadas não podem ser editadas!'}), 403
        tarefa.nome = data['nome']
        tarefa.descricao = data.get('descricao')
        tarefa.prioridade = data['prioridade']
        db.session.commit()
        return jsonify({'message': 'Tarefa atualizada com sucesso!'})

    if request.method == 'DELETE':
        db.session.delete(tarefa)
        db.session.commit()
        return jsonify({'message': 'Tarefa deletada com sucesso!'})

    return jsonify({'id': tarefa.id, 'nome': tarefa.nome, 'descricao': tarefa.descricao, 'finalizada': tarefa.finalizada, 'data_termino': tarefa.data_termino, 'prioridade': tarefa.prioridade, 'id_membro': tarefa.id_membro})

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000, debug=True)

