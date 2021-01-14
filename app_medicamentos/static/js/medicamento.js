//MODAL HEMOGRAMA
function nuevo_medicamento() {
    var horario_valor = document.getElementById("horario");
    var medicamento_valor = document.getElementById("medicamento");
    var dosis_valor = document.getElementById("dosis");

    console.log("horario: " + horario_valor.value);
    console.log("medicamento: " + medicamento_valor.value);
    console.log("dosis: " + dosis_valor.value);

    var fila_nueva1 = "<tr><td>" + medicamento_valor.value + "</td><td>" + horario_valor.value + "</td><td>" + dosis_valor.value + "</td></tr>";
    console.log(fila_nueva1);
    var btn = document.createElement("tr");
    btn.innerHTML = fila_nueva1;
    console.log("btn: ", btn);
    document.getElementById("tabla_medicamento").appendChild(btn);
}