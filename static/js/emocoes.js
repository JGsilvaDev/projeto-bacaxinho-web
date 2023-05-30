// feliz, neutro, triste, raiva
const emocoes = {'alegria':'😄🍍', 'neutro':'😐🍍', 'tristeza':'😢🍍','raiva':'😠🍍'}
const emo_output = document.querySelector('#emocao')

// atualizar_emocao()
emo_output.innerHTML = emocoes['neutro']

function atualizar_emocao() {
    $.ajax({
        url: '/obter_dados',
        type: 'GET',
        success: function(response) {
            emo_output.innerHTML = emocoes[response.emocao_usuario]
            console.log('emocao: '+ response.emocao_usuario)
        },
        error: function(error) {
            alert('Erro ao atualizar os dados')
        }
    });
}
