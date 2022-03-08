const URL_base = "http://127.0.0.1:5000";


document.addEventListener("DOMContentLoaded", function(){
    fetch(URL_base + "/usuario")
    .then(respuesta => respuesta.json())
    .then(datos => {
        let mnu_login = document.getElementById("mnulogin");

        if (datos == "si"){
            mnu_login.innerHTML = "[logueado] LogOut";
            mnu_login.href = "logoutKCO.htm";
        } else {
        //    console.log("nope");
        }
    })
});