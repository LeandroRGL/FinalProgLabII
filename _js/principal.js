var cns_peliculas = document.getElementById("cn1");

cns_peliculas.addEventListener('click', evento => {
    fetch('http://127.0.0.1:5000/peliculas/')
        .then(respuesta => respuesta.json())
        .then(peliculas => {
        console.log(peliculas)

        console.log(peliculas[0].título);
        })
})


var cns_directores = document.getElementById("cn2");

cns_directores.addEventListener('click', evento => {
    fetch('http://127.0.0.1:5000/directores/')
        .then(respuesta => respuesta.json())
        .then(directores => {
        console.log(directores)

        console.log(directores[0].nombre);
        })
})