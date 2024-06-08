document.addEventListener('DOMContentLoaded', function() {

    fetch('http://127.0.0.1:8000/membros', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => {
        if (response.ok) {
            console.log(response);
        } else {
            alert('Erro ao cadastrar membro.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao cadastrar membro. Verifique sua conexão com a internet.');
    });
    




})