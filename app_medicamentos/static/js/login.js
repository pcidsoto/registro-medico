
function login(){
    var user = document.getElementById("login-user");
    var pass = document.getElementById("login-pass");

    if ( user.value == "user@awake.com" && pass.value == "pass" ){
        window.location.href="main.html";
    }else{
        alert("Error Usuario o Contraseña incorrecta");
    }
}

