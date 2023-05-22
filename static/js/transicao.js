function addClass() {
    let msgList = document.querySelectorAll(".text-response")

    mostRecentElement = msgList[msgList.length-1]

    setTimeout(function() {
        mostRecentElement.classList.replace("text-response","text-response-fade")
    }, 30)
}