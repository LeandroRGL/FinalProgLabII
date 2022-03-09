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
                fetch(URL_base + "/usuarios/")
                .then(respuesta => respuesta.json())
                .then(usuarios => {
                    let div_comentarios = document.getElementById("comentarios");

                    for (let c = 0; c < comentarios.length; c++) {
                        let new_div_comentario = document.createElement("div");
                        new_div_comentario.classList.add("comentario");
                        new_div_comentario.innerHTML = comentarios[c].opinión;


                        div_comentarios.appendChild(new_div_comentario);


                    for (let u = 0; u < usuarios.length; u++){
                        if (String(comentarios[c].usuario_id) == String(usuarios[u].id)){
                            let ssdiv_comentarios = document.getElementsByClassName("comentario")[c];
                            let new_p_usuario = document.createElement("p");

                            new_p_usuario.classList.add("usr");
                            new_p_usuario.innerText = "(por " + usuarios[u].nombre + ")";

                            div_comentarios.appendChild(new_p_usuario);
                        }
                    }
                }
                })
            })


            document.getElementById("edt_pelicula").addEventListener("click", evento => {
                location.assign("editarKCO.htm?id=" + datId);
            })


            document.getElementById("agr_comentario").addEventListener("click", evento => {
                let datOpinion = document.getElementById("comentario").value;

                let opinion = {
                    opinión: datOpinion
                    }

                let request_cnf = {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify(opinion)
                    }

                fetch(URL_base + "/peliculas/" + datId +"/comentario", request_cnf)
                    .then(respuesta => respuesta.json())
                    .then(datos => {
                        document.getElementById("comentario").value = "";

                        let div_comentarios = document.getElementById("comentarios");

                        let new_div_comentario = document.createElement("div");
                        new_div_comentario.classList.add("comentario");
                        new_div_comentario.innerHTML = datOpinion;

                        div_comentarios.appendChild(new_div_comentario);

                        alert(datos);
                    })
                })


            document.getElementById("brr_pelicula").addEventListener("click", evento => {
                if (window.confirm("¿Seguro desea borrar esta película?")) {

                    let borrar = {
                        id: datId
                    }

                    let request_cnf = {
                        method: "DELETE",
                        headers: {"Content-Type": "application/json"},
                        body: JSON.stringify(borrar)
                        }

                    fetch(URL_base + "/peliculas/", request_cnf)
                    .then(respuesta => respuesta.json())
                    .then(datos => {
                        if (datos.includes("eliminada")){
                            alert(datos);

                            location.assign("indexKCO.htm");
                        } else {
                            alert(datos);
                        }
                    })
                } else {
                    alert("casi...");
                }
            })
        })
    } else {
        alert("nope!");;
    }
});