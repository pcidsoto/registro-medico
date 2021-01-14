select = document.getElementById("year");
for(i = 1900; i <= 2020; i++){
    option = document.createElement("option");
    option.value = i;
    option.text = i;
    select.appendChild(option);
}



function registro(){
    var nombre_nuevo = document.getElementById("nombre");
    alert("Bienvenido" + nombre_nuevo.value );
    window.location.href = "index.html";
}