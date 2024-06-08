document.addEventListener('DOMContentLoaded', function() {
    const formCadastrotarefa = document.getElementById('form-cadastro-tarefa');
    const cadastroBtn = document.getElementById('cadastro-btn');

    cadastroBtn.addEventListener('click', function(event) {
        event.preventDefault();

        const nome = document.getElementById('nome').value;
        const descricao = document.getElementById('descricao').value;
        const prioridade = document.getElementById('prioridade').value;
        const membro = document.getElementById('membro').value;

        fetch('http://127.0.0.1:8000/tarefas', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nome,
                descricao,
                prioridade,
                membro
            })
        })
        .then(response => {
            if (response.ok) {
                alert('tarefa cadastrada com sucesso!');
            } else {
                alert('Erro ao cadastrar tarefa.');
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert('Erro ao cadastrar tarefa. Verifique sua conexão com a internet.');
        });
    });
});
