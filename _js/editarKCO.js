document.addEventListener("DOMContentLoaded", function(){






    fetch(URL_base + "/directores/")
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


                if (valor == 5){
                    elemento.selected = true;
                }


            select.appendChild(elemento);
            }
        })

    fetch(URL_base + "/generos/")
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

                if (valor == 2){
                    elemento.selected = true;
                }

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

                if (valor == 1973){
                    elemento.selected = true;
                }

        select.appendChild(elemento);
        }


        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        var id;

        if (urlParams.has("id")){

                const datId = urlParams.get("id");

        fetch(URL_base + "/peliculas/" + datId)
            .then(respuesta => respuesta.json())
            .then(pelicula => {
//            document.getElementById("titulo").innerHTML = "(" + pelicula.año + ") " + pelicula.título;
//            document.getElementById("poster").src = pelicula.póster;
//            document.getElementById("sinopsis").innerHTML = pelicula.sinopsis;





   //document.getElementById("director").selectedIndex = 2;

//Array.from(document.querySelector("director").options).forEach(function(option_element) {
//    let option_value = option_element.value;
//
//
////
//    console.log('Option Value : ' + option_value);
////
//
//    console.log("\n\r");
//});



document.getElementById("titulo").value = pelicula.título;
document.getElementById("sinopsis").value = pelicula.sinopsis;
document.getElementById("poster").value = pelicula.póster;

            console.log(datId);
            console.log(pelicula);
            })
            }
        else{
            console.log("nope");
            }



    var edt_pelicula = document.getElementById("edt_pelicula");

    edt_pelicula.addEventListener('click', evento => {
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
            method: "PUT",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(pelicula)
        }

        fetch(URL_base + "/peliculas/" + id, request_cnf)
            .then(respuesta => respuesta.json())
            .then(datos => {

                if (datos.includes("no logueado")){
                    alert(datos);
                    location.assign("indexKCO.htm");
                }

            //console.log(datos);


            //alert(datos);
            })


        console.log(pelicula);


        document.getElementById("titulo").value = "";
        document.getElementById("ano").value = "";
        document.getElementById("director").value = "";
        document.getElementById("genero").value = "";
        document.getElementById("sinopsis").value = "";
        document.getElementById("poster").value = "";


    })
});