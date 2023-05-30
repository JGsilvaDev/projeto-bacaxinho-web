function addClass() {
    let msgList = document.querySelectorAll(".text-response")

    mostRecentElement = msgList[msgList.length-1]

    setTimeout(function() {
        mostRecentElement.classList.replace("text-response","text-response-fade")
    }, 30)
}

function ouvindo(bool) {
  if (bool == true) {
    document.getElementById('overflow-message').style.display = 'flex'
  }
  else {
    document.getElementById('overflow-message').style.display = 'none'
  }
}


var meuBotao = document.getElementById("modo-fala");
var meuSvg = document.getElementById("meuSvg");

meuBotao.addEventListener("mouseover", function() {
  var svgDoc = meuSvg.contentDocument;
  var svgElement = svgDoc.querySelector("path");

  svgElement.style.fill = "#08e900";
});

meuBotao.addEventListener("mouseout", function() {
  var svgDoc = meuSvg.contentDocument;
  var svgElement = svgDoc.querySelector("path");

  svgElement.style.fill = "#2e2e2e"; 
});
