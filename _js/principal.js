document.addEventListener("DOMContentLoaded", function(){
    var cns_peliculas = document.getElementById("cns_peliculas");

    cns_peliculas.addEventListener('click', evento => {
        fetch('http://127.0.0.1:5000/peliculas/')
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
                new_titulo.innerHTML = peliculas[g].título;

                div_pelicula.appendChild(new_titulo);


                let new_link = document.createElement('a');
                new_link.classList.add("button");
                new_link.href = "peliculaKCO.htm";
                new_link.innerHTML = "ver detalles";

                div_pelicula.appendChild(new_link);
            }
        })


        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);

        if (urlParams.has("id")){
            const product = urlParams.get("id");
            console.log(product);
            }
    })
});