//MODALES
function formateDate(string) {
    var info = string.split('-').reverse().join('/');
    return info;
}
//MODAL HEMOGRAMA
function nuevo_hemograma() {
    var fecha = document.getElementById("fecha");
    var nueva_fecha = formateDate(fecha.value);
    console.log(fecha)
    var hematocrito_valor = document.getElementById("hematocrito");
    var hemoglobina_valor = document.getElementById("hemoglobina");

    console.log("Fecha: " + nueva_fecha);
    console.log("Hematocrito: " + hematocrito_valor.value);
    console.log("Hemoglobina: " + hemoglobina_valor.value);

    var fila_nueva = "<tr><td>" + nueva_fecha + "</td><td>" + hematocrito_valor.value + "</td><td>" + hemoglobina_valor.value + "</td></tr>";
    console.log(fila_nueva);
    var btn = document.createElement("tr");
    btn.innerHTML = fila_nueva;
    console.log("btn: ", btn);
    document.getElementById("tabla_hemograma").appendChild(btn);
}

//MODAL PERFIL LIPIDICO
function nuevo_plipidico() {
    var fecha1 = document.getElementById("fecha1");
    var nueva_fecha1 = formateDate(fecha1.value);
    console.log(fecha1)
    var colesterol_valor = document.getElementById("colesterol");
    var bilirrubina_valor = document.getElementById("bilirrubina");

    console.log("Fecha: " + nueva_fecha1);
    console.log("Colesterol: " + colesterol_valor.value);
    console.log("Bilirrubina: " + bilirrubina_valor.value);

    var fila_nueva1 = "<tr><td>" + nueva_fecha1 + "</td><td>" + colesterol_valor.value + "</td><td>" + bilirrubina_valor.value + "</td></tr>";
    console.log(fila_nueva1);
    var btn1 = document.createElement("tr");
    btn1.innerHTML = fila_nueva1;
    console.log("btn: ", btn1);
    document.getElementById("tabla_plipidico").appendChild(btn1);
}

//MODAL PERFIL BIOQUIMICO
function nuevo_pbioquimico() {
    var fecha = document.getElementById("fecha3");
    var nueva_fecha3 = formateDate(fecha3.value);
    console.log(fecha3)
    var PTD_valor = document.getElementById("PTD");
    var TBR_valor = document.getElementById("TBR");

    console.log("Fecha: " + nueva_fecha3);
    console.log("PTD: " + PTD_valor.value);
    console.log("TBR: " + TBR_valor.value);

    var fila_nueva3 = "<tr><td>" + nueva_fecha3 + "</td><td>" + PTD_valor.value + "</td><td>" + TBR_valor.value + "</td></tr>";
    console.log(fila_nueva3);
    var btn3 = document.createElement("tr");
    btn3.innerHTML = fila_nueva3;
    console.log("btn: ", btn3);
    document.getElementById("tabla_pbioquimico").appendChild(btn3);
}

//MODAL PRESION ARTERIAL
function nuevo_parterial() {
    var fecha4 = document.getElementById("fecha4");
    var nueva_fecha4 = formateDate(fecha4.value);
    console.log(fecha4)
    var f_mañana_valor = document.getElementById("f_mañana");
    var f_tarde_valor = document.getElementById("f_tarde");

    console.log("Fecha: " + nueva_fecha4);
    console.log("Frecuencia mañana: " + f_mañana_valor.value);
    console.log("Frecuencia tarde: " + f_tarde_valor.value);

    var fila_nueva4 = "<tr><td>" + nueva_fecha4 + "</td><td>" + f_mañana_valor.value + "</td><td>" + f_tarde_valor.value + "</td></tr>";
    console.log(fila_nueva4);
    var btn4 = document.createElement("tr");
    btn4.innerHTML = fila_nueva4;
    console.log("btn: ", btn4);
    document.getElementById("tabla_parterial").appendChild(btn4);
}
//GRAFICOS

//Hemograma
var speedCanvas = document.getElementById("graph_hemograma");

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

var speedData = {
    labels: ["0s", "10s", "20s", "30s", "40s", "50s", "60s"],
    datasets: [{
        label: "Hemograma",
        data: [0, 59, 75, 20, 20, 55, 40],
    }]
};

var chartOptions = {
    legend: {
        display: true,
        position: 'top',
        labels: {
            boxWidth: 80,
            fontColor: 'black'
        }
    }
};

var lineChart = new Chart(speedCanvas, {
    type: 'bar',
    data: speedData,
    options: chartOptions
});

//Perfil lipídico


var densityCanvas = document.getElementById("graph_lipidico");

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 13;

var densityData = {
    label: 'Valores lipídicos1',
    data: [1000, 1326, 687, 1271, 1638],
    backgroundColor: 'rgba(0, 99, 132, 0.6)',
    borderWidth: 0,
    yAxisID: "y-axis-density"
};

var gravityData = {
    label: 'Valores lipídicos2',
    data: [3.7, 4.1, 9.0, 8.7, 11.0],
    backgroundColor: 'rgba(99, 132, 0, 0.6)',
    borderWidth: 0,
    yAxisID: "y-axis-gravity"
};

var planetData = {
    labels: ["Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
    datasets: [densityData, gravityData]
};

var chartOptions = {
    scales: {
        xAxes: [{
            barPercentage: 1,
            categoryPercentage: 0.6
        }],
        yAxes: [{
            id: "y-axis-density"
        }, {
            id: "y-axis-gravity"
        }]
    }
};

var barChart = new Chart(densityCanvas, {
    type: 'line',
    data: planetData,
    options: chartOptions
});



//Perfil bioquimico
var ctx = document.getElementById("graph_bioquimico");
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Group 1", "Group 2", "Group 3"],
        datasets: [{
            label: 'Perfiles bioquímicos',
            data: [12, 5, 3]
        }]
    }
});
//Presion arterial

var ctx = document.getElementById("graph_presion");
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["Semana 1", "Semana 2", "Semana 3", "Semana 4", "Semana 5"],
        datasets: [{
            label: 'Presión arterial',
            data: [12, 19, 5, 14, 10]
        }]
    }
});