document.addEventListener("DOMContentLoaded", function(){
    function cargar_pagina(prmdirector){
        fetch(URL_base + "/directores")
        .then(respuesta => respuesta.json())
        .then(directores => {
            let select = document.getElementById("mnudirector");

            for (let d = -1; d < directores.length; d++){
                if (d == -1){
                    var opcion = "[todos]";
                    var valor = "0";
                } else {
                    var opcion = directores[d].nombre;
                    var valor = directores[d].id;
                }

                let elemento = document.createElement("option");

                elemento.textContent = opcion;
                elemento.value = valor;

                if (prmdirector == d + 1){
                    elemento.selected = true;
                }
                select.appendChild(elemento);
            }
        })


        if (prmdirector == 0){
            var URL_API = "/peliculas/";
        } else {
            var URL_API = "/peliculas/director/" + prmdirector;
        }

        fetch(URL_base + URL_API)
        .then(respuesta => respuesta.json())
        .then(peliculas => {
            let div_principal = document.getElementById('principal');
            div_principal.innerHTML = "";

            for (let g = 0; g < peliculas.length; g++) {
                let div_principal = document.getElementById('principal');


                let new_div_pelicula = document.createElement('div');
                new_div_pelicula.setAttribute("id", peliculas[g].id);
                new_div_pelicula.classList.add("pelicula");

                div_principal.appendChild(new_div_pelicula);


                let div_pelicula = document.getElementById(peliculas[g].id);
                let new_poster = document.createElement('img');
                new_poster.classList.add("titulo");
                new_poster.src = peliculas[g].póster;

                div_pelicula.appendChild(new_poster);


                let new_titulo = document.createElement('div');
                new_titulo.classList.add("titulo");
                new_titulo.innerHTML = "(" + peliculas[g].año + ") " + peliculas[g].título;

                div_pelicula.appendChild(new_titulo);


                let new_link = document.createElement('a');
                new_link.classList.add("button");
                new_link.href = "peliculaKCO.htm?id=" + peliculas[g].id;
                new_link.innerHTML = "ver detalles";

                div_pelicula.appendChild(new_link);
            }
        })
    }


    window.onload = cargar_pagina(0);


    var directores = document.getElementById("mnudirector");

    directores.addEventListener('change', evento => {
        let director_id = directores.value;

        directores.options.length = 0;

        cargar_pagina(director_id);
    })
});