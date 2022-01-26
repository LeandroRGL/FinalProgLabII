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


# Includes
import os                       # Lectura y escritura de archivos
import json                     # Manipular JSON
from flask import Flask         # Servidor FLASK
from flask import jsonify       # Manipular JSON
from http import HTTPStatus     # Códigos HTTP legibles


# Configuración
servidor_nombre = "Movies API server [ PrgLabII 2022 ]"

servidor_API = Flask(servidor_nombre)


# Data
ruta_actual = os.path.dirname(__file__)
ruta_data = ruta_actual + "/__data/"

with open(os.path.join(ruta_data, 'usuarios.json'), 'r', encoding="utf-8") as data_JSON:
    usuarios = json.load(data_JSON)

with open(os.path.join(ruta_data, 'peliculas.json'), 'r', encoding="utf-8") as data_JSON:
    peliculas = json.load(data_JSON)

with open(os.path.join(ruta_data, 'directores.json'), 'r', encoding="utf-8") as data_JSON:
    directores = json.load(data_JSON)

with open(os.path.join(ruta_data, 'generos.json'), 'r', encoding="utf-8") as data_JSON:
    generos = json.load(data_JSON)

with open(os.path.join(ruta_data, 'comentarios.json'), 'r', encoding="utf-8") as data_JSON:
    comentarios = json.load(data_JSON)






# - - Principal - -

@servidor_API.route("/", methods=["GET"])
def default():
    return servidor_nombre, HTTPStatus.OK


@servidor_API.route("/test", methods=["GET"])
@servidor_API.route("/test/", methods=["GET"])
def funcion():
    return jsonify(peliculas), HTTPStatus.OK



@servidor_API.route("/usuarios", methods=["GET"])
@servidor_API.route("/usuarios/", methods=["GET"])
def funcionusuarios():
    return jsonify(usuarios), HTTPStatus.OK


@servidor_API.route("/peliculas", methods=["GET"])
@servidor_API.route("/peliculas/", methods=["GET"])
def peliculasr():
    return jsonify(peliculas), HTTPStatus.OK


servidor_API.run()