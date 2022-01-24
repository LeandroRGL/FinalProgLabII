# --------------------------------------------------
# Proyecto final 2021
#
# Programación II
# Laboratorio de computación II
# TUP - UTN FRBB
#
# Leandro M. Regolf & Agustín Ascolani
# --------------------------------------------------
#
# Crear una plataforma web para mantener una lista de
# películas recomendadas por parte de los usuarios
# --------------------------------------------------


from flask import Flask
from flask import jsonify


server_name = "Movies API server [ PrgLabII 2022 ]"


movies_server = Flask(server_name)


# Data
peliculas = [
    {
        "id": 1,
        "nombre": "ROBOCOP"
    },
    {
        "id": 2,
        "nombre": "Terminator"
    },
    {
        "id": 3,
        "nombre": "Volver al futuro"
    }
]


@movies_server.route("/", methods=["GET"])
def default():
    return server_name

@movies_server.route("/test", methods=["GET"])
def funcion():
    return jsonify(peliculas), 200


movies_server.run()