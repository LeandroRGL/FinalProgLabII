document.addEventListener("DOMContentLoaded", function(){
    fetch('http://127.0.0.1:5000/directores/')
        .then(respuesta => respuesta.json())
        .then(directores => {
        let select = document.getElementById("director");

        for (let d = -1; d < directores.length; d++){
            if (d == -1){
                var opcion = "";
                var valor = "";
            }else{
                var opcion = directores[d].nombre;
                var valor = directores[d].id;
            }

            let elemento = document.createElement("option");

            elemento.textContent = opcion;
            elemento.value = valor;

            select.appendChild(elemento);
            }
        })

    fetch('http://127.0.0.1:5000/generos/')
        .then(respuesta => respuesta.json())
        .then(generos => {
        let select = document.getElementById("genero");

        for (let g = -1; g < generos.length; g++){
            if (g == -1){
                var opcion = "";
                var valor = "";
            }else{
                var opcion = generos[g].denominación;
                var valor = generos[g].id;
            }

            let elemento = document.createElement("option");

            elemento.textContent = opcion;
            elemento.value = valor;

            select.appendChild(elemento);
            }
        })


    let select = document.getElementById("ano");

    for (let a = 1887; a < new Date().getFullYear() + 2; a++){
        if (a == 1887){
            var opcion = "";
            var valor = "";
        }else{
            var opcion = a;
            var valor = a;
        }

        let elemento = document.createElement("option");

        elemento.textContent = opcion;
        elemento.value = valor;

        select.appendChild(elemento);
        }


    var add_pelicula = document.getElementById("add_pelicula");

    add_pelicula.addEventListener('click', evento => {
        let datTitulo = document.getElementById("titulo").value;
        let datAno = document.getElementById("ano").value;
        let datDirector = document.getElementById("director").value;
        let datGenero = document.getElementById("genero").value;
        let datSinopsis = document.getElementById("sinopsis").value;
        let datPoster = document.getElementById("poster").value;

        let pelicula = {
            título: datTitulo,
            año: datAno,
            director_id: datDirector,
            género_id: datGenero,
            sinopsis: datSinopsis,
            póster: datPoster
        }

        let request_cnf = {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(pelicula)
        }

        fetch("http://127.0.0.1:5000/peliculas/", request_cnf)
            .then(respuesta => respuesta.json())
            .then(datos => {

            console.log(datos);


            alert(datos);
            })


        console.log(pelicula);


        document.getElementById("titulo").value = "";
        document.getElementById("ano").value = "";
        document.getElementById("director").value = "";
        document.getElementById("genero").value = "";
        document.getElementById("sinopsis").value = "";
        document.getElementById("poster").value = "";

        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);

        if (urlParams.has("id")){
            const id = urlParams.get("id");
            console.log(id);
            }
        else{
            console.log("nope");
            }
    })
});