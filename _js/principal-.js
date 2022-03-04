document.addEventListener("DOMContentLoaded", function(){

var cns_peliculas = document.getElementById("cns_peliculas");

cns_peliculas.addEventListener('click', evento => {
    fetch('http://127.0.0.1:5000/peliculas/')
        .then(respuesta => respuesta.json())
        .then(peliculas => {
//        console.log(peliculas)

console.log(peliculas.length)

        let principal = document.getElementById('principal');
 //       principal.innerHTML += 'Hello, I am Arun';




//        console.log(peliculas[0].título);
        for (let g = 0; g < peliculas.length; g++) {
            console.log(peliculas[g].id);
            console.log(peliculas[g].póster);
            console.log(peliculas[g].título);

                var elem = document.createElement('div');
                elem.setAttribute("id", peliculas[g].id);
                elem.classList.add("pelicula");
                principal.appendChild(elem);

                let principalx = document.getElementById(peliculas[g].id);

                var elem2 = document.createElement('img');
                elem2.classList.add("titulo");

                elem2.src = peliculas[g].póster;

                principalx.appendChild(elem2);




                var elem3 = document.createElement('div');
                elem3.classList.add("titulo");
                principalx.appendChild(elem3);

            //principal.innerHTML += "<div>" + peliculas[g].id + "</div>";
           // principal.innerHTML += peliculas[g].id;
            principalx.innerHTML += peliculas[g].póster;
            principalx.innerHTML += peliculas[g].título;
            //principal.innerHTML += "</div>";

            }
        })
})


var cns_directores = document.getElementById("cns_directores");

cns_directores.addEventListener('click', evento => {
    fetch('http://127.0.0.1:5000/directores/')
        .then(respuesta => respuesta.json())
        .then(directores => {
        console.log(directores)

        console.log(directores[0].nombre);
        })
})


console.log(document.body);

ww = document.body.getElementsByTagName('a');

console.log(ww);
console.log(Object.keys(ww).length);


for (let i = 0; i < Object.keys(ww).length; i++) {
  console.log(ww[i].href);
}


w = document.getElementById('1a');
console.log(w.className);
});