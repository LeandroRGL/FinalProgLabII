document.addEventListener("DOMContentLoaded", function(){
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);

    if (urlParams.has("id")){
        const datId = urlParams.get("id");

        fetch(URL_base + "/pelicula/" + datId)
        .then(respuesta => respuesta.json())
        .then(pelicula => {
            let titulo = pelicula.título;
            let sinopsis = pelicula.sinopsis;
            let poster = pelicula.póster;
            let director_id = pelicula.director_id;
            let ano = pelicula.año;
            let genero_id = pelicula.género_id;

            document.getElementById("titulo").value = titulo;
            document.getElementById("sinopsis").value = sinopsis;
            document.getElementById("poster").value = poster;


        fetch(URL_base + "/directores")
        .then(respuesta => respuesta.json())
        .then(directores => {
            let select = document.getElementById("director");

            for (let d = 0; d < directores.length; d++){
                var opcion = directores[d].nombre;
                var valor = directores[d].id;

                let elemento = document.createElement("option");

                elemento.textContent = opcion;
                elemento.value = valor;

                if (valor == director_id){
                    elemento.selected = true;
                }

                select.appendChild(elemento);
            }
        })


        fetch(URL_base + "/generos")
        .then(respuesta => respuesta.json())
        .then(generos => {
            let select = document.getElementById("genero");

            for (let g = 0; g < generos.length; g++){
                var opcion = generos[g].denominación;
                var valor = generos[g].id;

                let elemento = document.createElement("option");

                elemento.textContent = opcion;
                elemento.value = valor;

                if (valor == genero_id){
                    elemento.selected = true;
                }

                select.appendChild(elemento);
            }
        })


        let select = document.getElementById("ano");

        for (let a = 1888; a < new Date().getFullYear() + 2; a++){
            var opcion = a;
            var valor = a;

            let elemento = document.createElement("option");

            elemento.textContent = opcion;
            elemento.value = valor;

            if (valor == ano){
                elemento.selected = true;
            }

            select.appendChild(elemento);
        }


        var edt_pelicula = document.getElementById("edt_pelicula");

        edt_pelicula.addEventListener("click", evento => {
            let datTitulo = document.getElementById("titulo").value;
            let datAno = document.getElementById("ano").value;
            let datDirector = document.getElementById("director").value;
            let datGenero = document.getElementById("genero").value;
            let datSinopsis = document.getElementById("sinopsis").value;
            let datPoster = document.getElementById("poster").value;

            let datpelicula = {
                título: datTitulo,
                año: datAno,
                director_id: datDirector,
                género_id: datGenero,
                sinopsis: datSinopsis,
                póster: datPoster
            }

            let request_cnf = {
                method: "PUT",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(datpelicula)
            }

            fetch(URL_base + "/pelicula/" + datId, request_cnf)
            .then(respuesta => respuesta.json())
            .then(datos => {
                alert(datos);

                location.assign("indexKCO.htm");
                })
            })
        })
    } else {
        console.log("nope");
    }
});