CREATE TABLE Membro (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    nome VARCHAR(50) NOT NULL,
    senha VARCHAR(50) NOT NULL
);

CREATE TABLE Tarefa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(140),
    finalizada BOOLEAN NOT NULL DEFAULT FALSE,
    data_termino DATETIME,
    prioridade ENUM('Baixa', 'Média', 'Alta') NOT NULL DEFAULT 'Baixa'
);


