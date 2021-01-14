function formateDate(string) {
    var info = string.split('-').reverse().join('/');
    return info;
}

function nueva_cita() {
    var nombre_medico = document.getElementById("nombre_medico");
    var especialidad = document.getElementById("especialidad");
    var fecha = document.getElementById("fecha");
    var fecha_invertida = formateDate(fecha.value);
    var hora = document.getElementById("hora");
    var lugar = document.getElementById("lugar");
    var nota = document.getElementById("nota");

    if ((nombre_medico.value != "") && (especialidad.value != "") && (fecha.value != "") && (hora.value != "") && (lugar.value != "")) {
        var fila_nueva = "<tr><td>" + nombre_medico.value + "</td><td>" + especialidad.value + "</td><td>" + fecha_invertida + "</td><td>" + hora.value + "</td><td>" + lugar.value + "</td><td>" + nota.value + "</td></tr>";
        var btn = document.createElement("tr");
        btn.innerHTML = fila_nueva;
        document.getElementById("tabla_citas").appendChild(btn);

        nombre_medico.value = "";
        especialidad.value = "";
        fecha.value = "";
        hora.value = "";
        lugar.value = "";
        nota.value = "";
    } else {
        alert("Hay campos en blanco");
    }


}

function nuevo_examen() {
    var lugar_examen = document.getElementById("lugar_examen");
    var fecha_examen = document.getElementById("fecha_examen");
    var f_examen_invertida = formateDate(fecha_examen.value);
    var hora_examen = document.getElementById("hora_examen");
    var examen_direccion = document.getElementById("examen_direccion");
    var nota_examen = document.getElementById("nota_examen");

    if ((lugar_examen.value != "") && (fecha_examen.value != "") && (hora_examen.value != "")) {
        var fila_examen_nueva = "<tr><td>" + lugar_examen.value + "</td><td>" + f_examen_invertida + "</td><td>" + hora_examen.value + "</td><td>" + nota_examen.value + "</td></tr>";
        var btn_examen = document.createElement("tr");
        btn_examen.innerHTML = fila_examen_nueva;
        document.getElementById("tabla_examenes").appendChild(btn_examen);

        examen_direccion.value = "";
        lugar_examen.value = "";
        fecha_examen.value = "";
        hora_examen.value = "";
        nota_examen.value = "";
    } else {
        alert("Hay campos en blanco");
    }

}