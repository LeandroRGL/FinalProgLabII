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


# Librerías
import os                       # Lectura y escritura de archivos
import json                     # Manipular JSON
from flask import Flask         # Servidor FLASK
from flask import jsonify       # Manipular JSON
from flask import request       # Peticionar datos
from http import HTTPStatus     # Códigos HTTP legibles


# Configuración
servidor_nombre = "Movies API server [ PrgLabII 2022 ]"


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
servidor_API = Flask(servidor_nombre)


@servidor_API.route("/", methods=["GET"])
def default():
    return servidor_nombre, HTTPStatus.OK


# -- Usuarios
@servidor_API.route("/usuarios", methods=["GET"])
@servidor_API.route("/usuarios/", methods=["GET"])
def usuarios_devolver_todos():
    return jsonify(usuarios), HTTPStatus.OK


# -- Películas
@servidor_API.route("/peliculas", methods=["GET"])
@servidor_API.route("/peliculas/", methods=["GET"])
def peliculas_devolver_todas():
    response = jsonify(peliculas)
    return response, HTTPStatus.OK

@servidor_API.route("/peliculas/<clnt_id>", methods=["GET"])
def peliculas_devolver_una(clnt_id):
    if clnt_id.isnumeric():
        id = int(clnt_id)

        for pelicula in peliculas:
            if pelicula["id"] == id:
                return jsonify(pelicula["título"]), HTTPStatus.OK
        return jsonify("[nfo] - <" + str(id) + "> no existe"), HTTPStatus.NOT_FOUND
    else:
        return jsonify("[err] - <id> debe ser entero"), HTTPStatus.BAD_REQUEST


@servidor_API.route("/peliculas", methods=["POST"])
@servidor_API.route("/peliculas/", methods=["POST"])
def peliculas_agregar_una():
    clnt_data = request.get_json()

    if "título" in clnt_data:
        peliculas.append({
            "id": 33,
            "título": clnt_data["título"],
            "año": 2005,
            "director_id": 2,
            "género_id": 33,
            "sinopsis": clnt_data["título"],
            "póster": "sdsddsfsdfsdf",
            "usuario_id": 2
        })
        return jsonify(clnt_data), HTTPStatus.CREATED
    else:
        return jsonify("[err] - <título> debe estar presente"), HTTPStatus.BAD_REQUEST



# -- Comentarios
@servidor_API.route("/comentarios", methods=["GET"])
@servidor_API.route("/comentarios/", methods=["GET"])
def comentarios_devolver_todos():
    return jsonify(comentarios), HTTPStatus.OK

@servidor_API.route("/peliculas/<clnt_id>/comentarios", methods=["GET"])
@servidor_API.route("/peliculas/<clnt_id>/comentarios/", methods=["GET"])
def comentarios_devolver_por_pelicula(clnt_id):
    if clnt_id.isnumeric():
        id = int(clnt_id)

        for comentario in comentarios:
            if comentario["película_id"] == id:
                return jsonify(comentario["opinión"]), HTTPStatus.OK
        return jsonify("[nfo] - <" + str(id) + "> no existe"), HTTPStatus.NOT_FOUND
    else:
        return jsonify("[err] - <id> debe ser entero"), HTTPStatus.BAD_REQUEST

@servidor_API.route("/usuarios/<clnt_id>/comentarios", methods=["GET"])
@servidor_API.route("/usuarios/<clnt_id>/comentarios/", methods=["GET"])
def comentarios_devolver_por_usuario(clnt_id):
    if clnt_id.isnumeric():
        id = int(clnt_id)

        for comentario in comentarios:
            if comentario["usuario_id"] == id:
                return jsonify(comentario["opinión"]), HTTPStatus.OK
        return jsonify("[nfo] - <" + str(id) + "> no existe"), HTTPStatus.NOT_FOUND
    else:
        return jsonify("[err] - <id> debe ser entero"), HTTPStatus.BAD_REQUEST


@servidor_API.route("/peliculas/<clnt_id>/comentarios", methods=["POST"])
@servidor_API.route("/peliculas/<clnt_id>/comentarios/", methods=["POST"])
def comentarios_agregar_uno(clnt_id):
    if clnt_id.isnumeric():
        id = int(clnt_id)

        clnt_data = request.get_json()

        if "opinión" in clnt_data:
            comentarios.append({
                "id": 33,
                "película_id": 2,
                "opinión": clnt_data["opinión"],
                "usuario_id": 2
            })
            return jsonify(clnt_data), HTTPStatus.CREATED
        else:
            return jsonify("[err] - <opinión> debe estar presente"), HTTPStatus.BAD_REQUEST
    else:
        return jsonify("[err] - <id> debe ser entero"), HTTPStatus.BAD_REQUEST



# -- Directores
@servidor_API.route("/directores", methods=["GET"])
@servidor_API.route("/directores/", methods=["GET"])
def directores_devolver_todos():
    return jsonify(directores), HTTPStatus.OK


@servidor_API.route("/peliculas/<clnt_id>/directores", methods=["GET"])
@servidor_API.route("/peliculas/<clnt_id>/directores/", methods=["GET"])
def directores_devolver_uno(clnt_id):
    if clnt_id.isnumeric():
        id = int(clnt_id)

        for director in directores:
            if director["id"] == id:
                return jsonify(director["nombre"]), HTTPStatus.OK
        return jsonify("[nfo] - <" + str(id) + "> no existe"), HTTPStatus.NOT_FOUND
    else:
        return jsonify("[err] - <id> debe ser entero"), HTTPStatus.BAD_REQUEST



# -- Géneros
@servidor_API.route("/generos", methods=["GET"])
@servidor_API.route("/generos/", methods=["GET"])
def generos_devolver_todos():
    return jsonify(generos), HTTPStatus.OK



servidor_API.run()