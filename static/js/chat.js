const chat_frame = document.querySelector('#chat-container-frame')
let input = document.querySelector('#input-text')
const mensagem = "Sinto muito, os serviços do bacaxinho ainda não estão disponíveis."

input.addEventListener("keydown", function(event) {
    if (event.keyCode === 13) {
        document.getElementById("input-submit").click();
    }
})

function enviarMensagem(id,mensagem,delay) {
    //remove qualquer tag html do texto, uma forma de tratar antes de enviar para a div
    let msg = mensagem.replace(/<\/?[^>]+(>|$)/g, "");

    setTimeout(function() {
        chat_frame.innerHTML += `<div id="${id}" class="text-response"><p>${mensagem}</p></div>`

        scrollDown()
        addClass()
        return;
    }, delay);

}

function userSend() {
    enviarMensagem("user-response",input.value,0)
    input.value = ""
}

function scrollDown() {
    chat_frame.scrollTop = chat_frame.scrollHeight;
}