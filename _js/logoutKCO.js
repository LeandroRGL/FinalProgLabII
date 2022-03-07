document.addEventListener("DOMContentLoaded", function(){
        let request_cnf = {
            method: "POST",
            headers: {"Content-Type": "application/json"},
        }

        fetch(URL_base + "/logout", request_cnf)
            .then(respuesta => respuesta.json())
            .then(datos => {
                alert(datos);

                if (datos.includes("Deslogueado")){
                    location.assign("indexKCO.htm");
                }
            })



});