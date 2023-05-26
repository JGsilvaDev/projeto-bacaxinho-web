// Função para definir um cookie
function setCookie(name, value, expires) {
    var cookie = name + "=" + encodeURIComponent(value);

    if (expires) {
        cookie += "; expires=" + expires.toUTCString();
    }

    document.cookie = cookie;
}
  
  // data de expiração de 1 minuto
  var expirationDate = new Date();
  expirationDate.setTime(expirationDate.getTime() + (60 * 1000));
  

  