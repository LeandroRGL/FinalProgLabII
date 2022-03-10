document.addEventListener("DOMContentLoaded", function(){
    var login = document.getElementById("login");

    login.addEventListener("click", evento => {
        let datUsuario = document.getElementById("usuario").value;
        let datClave = document.getElementById("clave").value;

        let usuario = {
            usuario: datUsuario,
            clave: datClave
        }

        let request_cnf = {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(usuario)
        }

        fetch(URL_base + "/usuario/login", request_cnf)
            .then(respuesta => respuesta.json())
            .then(datos => {
                document.getElementById("usuario").value = "";
                document.getElementById("clave").value = "";

                alert(datos);

                if (datos.includes("Bienvenido")){
                    location.assign("indexKCO.htm");
                }
            })
    })
});