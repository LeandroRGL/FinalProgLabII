var btn_consulta = document.getElementById("cn1");

btn_consulta.addEventListener('click', evento => {
    fetch('http://127.0.0.1:5000/peliculas/')
        .then(respuesta => respuesta.json())
        .then(datos => {
        console.log(datos)

        var ff = datos;

        console.log(datos[0].título);
        })
})