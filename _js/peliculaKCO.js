document.addEventListener("DOMContentLoaded", function(){
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);

    if (urlParams.has("id")){
        const datId = urlParams.get("id");

        fetch(URL_base + "/peliculas/" + datId)
            .then(respuesta => respuesta.json())
            .then(pelicula => {
            document.getElementById("titulo").innerHTML = "(" + pelicula.año + ") " + pelicula.título;
            document.getElementById("poster").src = pelicula.póster;
            document.getElementById("sinopsis").innerHTML = pelicula.sinopsis;


            fetch(URL_base + "/peliculas/" + pelicula.director_id + "/directores/")
                .then(respuesta => respuesta.json())
                .then(director => {
                document.getElementById("director").innerHTML = director;
                })


            fetch(URL_base + "/peliculas/" + pelicula.género_id + "/generos/")
                .then(respuesta => respuesta.json())
                .then(genero => {
                document.getElementById("genero").innerHTML = genero;
                })


            fetch(URL_base + "/peliculas/" + datId + "/comentarios")
                .then(respuesta => respuesta.json())
                .then(comentarios => {
                let div_comentarios = document.getElementById("comentarios");

                for (let c = 0; c < comentarios.length; c++) {
                    let new_div_comentario = document.createElement('div');
                    new_div_comentario.classList.add("comentario");
                    new_div_comentario.innerHTML = comentarios[c].opinión;

                    div_comentarios.appendChild(new_div_comentario);
                    }
                })
            })
    }else{
         alert("nope!");;
    }
});