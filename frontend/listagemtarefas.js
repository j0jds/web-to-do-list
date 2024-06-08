document.addEventListener('DOMContentLoaded', function() {

    fetch('http://127.0.0.1:8000/tarefas', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        },
    })
    .then(response => {
        if (response.ok) {
            console.log(response);
            response.json().then(tarefas=>{
                console.log(tarefas);
            });
        } else {
            alert('Erro ao obter tarefas.');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Erro ao obter tarefas. Verifique sua conexão com a internet.');
    });
    
})