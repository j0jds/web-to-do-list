document.addEventListener('DOMContentLoaded', function() {
    const formCadastroMembro = document.getElementById('form-cadastro-membro');
    const cadastroBtn = document.getElementById('cadastro-btn');

    cadastroBtn.addEventListener('click', function(event) {
        event.preventDefault();

        const email = document.getElementById('email').value;
        const senha = document.getElementById('senha').value;

        console.log('Email:', email);
        console.log('Senha:', senha);

        fetch('http://127.0.0.1:8000/membros', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: email,
                nome: 'Nome', 
                senha: senha
            })
        })
        .then(response => {
            if (response.ok) {
                alert('Membro cadastrado com sucesso!');
            } else {
                alert('Erro ao cadastrar membro.');
            }
        })
        .catch(error => {
            console.error('Erro:', error);
            alert('Erro ao cadastrar membro. Verifique sua conexão com a internet.');
        });
    });
});
