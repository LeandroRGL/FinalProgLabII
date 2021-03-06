# --------------------------------------------------
# Proyecto final 2021
#
# Programación II
# Laboratorio de computación II
# TUP - UTN FRBB
#
# Agustín Ascolani & Leandro M. Regolf
# --------------------------------------------------
#
# Crear una plataforma web para mantener una lista de
# películas recomendadas por parte de los usuarios
# --------------------------------------------------


# Librerías
import os                               # Lectura y escritura de archivos
import json                             # Manipular JSON
from flask import Flask                 # Servidor FLASK
from flask import jsonify               # Manipular JSON
from flask import request               # Peticionar datos
from http import HTTPStatus             # Códigos HTTP legibles
from flask_cors import CORS             # Permitir Intercambio Recursos Origen Cruzado
from flask_cors import cross_origin     # Encabezado HTTP Origen Cruzado


# - - Configuración - -
servidor_nombre = "Movies API server [ PrgLabII 2021 ]"


# - - Globales - -
usuario_id_auth = 0
usuario_nombre_auth = ""

cantidad_peliculas_a_nologueados = 4


# - - Data inicial - -
ruta_actual = os.path.dirname(__file__)
ruta_data = ruta_actual + "/__data/"

ruta_data_usuarios = os.path.join(ruta_data, "usuarios.json")
ruta_data_peliculas = os.path.join(ruta_data, "peliculas.json")
ruta_data_directores = os.path.join(ruta_data, "directores.json")
ruta_data_generos = os.path.join(ruta_data, "generos.json")
ruta_data_comentarios = os.path.join(ruta_data, "comentarios.json")


with open(ruta_data_usuarios, "r", encoding="utf-16") as data_JSON:
    usuarios = json.load(data_JSON)

with open(ruta_data_peliculas, "r", encoding="utf-16") as data_JSON:
    peliculas = json.load(data_JSON)

with open(ruta_data_directores, "r", encoding="utf-16") as data_JSON:
    directores = json.load(data_JSON)

with open(ruta_data_generos, "r", encoding="utf-16") as data_JSON:
    generos = json.load(data_JSON)

with open(ruta_data_comentarios, "r", encoding="utf-16") as data_JSON:
    comentarios = json.load(data_JSON)


ult_id_usuarios = len(usuarios)
ult_id_peliculas = len(peliculas)
ult_id_directores = len(directores)
ult_id_generos = len(generos)
ult_id_comentarios = len(comentarios)


# - - Funciones - -
def usuario_loguear(id, nombre):
    global usuario_id_auth
    global usuario_nombre_auth

    usuario_id_auth = id
    usuario_nombre_auth = nombre

def usuario_desloguear():
    global usuario_id_auth
    global usuario_nombre_auth

    usuario_id_auth = 0
    usuario_nombre_auth = ""

def usuario_chequear_logged():
    global usuario_id_auth
    global usuario_nombre_auth

    if usuario_id_auth != 0:
        return True
    else:
        return False

def checkear_comentarios_foraneos(datUsuario_id, datPelicula_id):
    for i in range(len(comentarios)):
        if int(comentarios[i]["película_id"]) == int(datPelicula_id) and int(comentarios[i]["usuario_id"]) != int(datUsuario_id):
            return True
    return False


# - - Servidor - -
servidor_API = Flask(servidor_nombre)
cors = CORS(servidor_API, resources={r"/*/*/*": {"origins": "*"}})
servidor_API.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin(origin='*', headers=['Content-Type','Authorization'])


# - - Entry-Points - -
@servidor_API.route("/", methods=["GET"])
def default():
    return servidor_nombre, HTTPStatus.OK


# - Usuarios
@servidor_API.route("/usuarios/", methods=["GET"])
@servidor_API.route("/usuarios", methods=["GET"])
def usuarios_devolver_todos():
    rspUsuarios = [{k: v for k, v in d.items() if k != "clave"} for d in usuarios]

    return jsonify(rspUsuarios), HTTPStatus.OK


@servidor_API.route("/usuario/", methods=["GET"])
@servidor_API.route("/usuario", methods=["GET"])
def usuarios_chequear_logged():
    global usuario_id_auth
    global usuario_nombre_auth

    if usuario_chequear_logged():
        return jsonify("si"), HTTPStatus.OK
    else:
        return jsonify("ERROR: no logueado"), HTTPStatus.UNAUTHORIZED


@servidor_API.route("/usuario/login", methods=["POST"])
def usuarios_devolver_login():
    clnt_data = request.get_json()

    if "usuario" in clnt_data and "clave" in clnt_data:
        for usuario in usuarios:
            if usuario["nombre"] == clnt_data["usuario"] and usuario["clave"] == clnt_data["clave"]:
                usuario_loguear(usuario["id"], usuario["nombre"])

                return jsonify("Bienvenido " + usuario["nombre"] + "!"), HTTPStatus.OK
        return jsonify("INFO: <usuario> o <clave> incorrecta"), HTTPStatus.NOT_FOUND
    else:
        return jsonify("ERROR: request incompleto"), HTTPStatus.BAD_REQUEST


@servidor_API.route("/usuario/logout", methods=["POST"])
def usuarios_devolver_logout():
    usuario_desloguear()

    return jsonify("Deslogueado!"), HTTPStatus.OK


# - Películas
@servidor_API.route("/peliculas/", methods=["GET"])
@servidor_API.route("/peliculas", methods=["GET"])
def peliculas_devolver_todas():
    if (usuario_chequear_logged() == True):
        rspPeliculas = peliculas
    else:
        rspPeliculas = peliculas[cantidad_peliculas_a_nologueados * (-1):]

    response = jsonify(rspPeliculas)

    return response, HTTPStatus.OK


@servidor_API.route("/pelicula/<clnt_id>", methods=["GET"])
def peliculas_devolver_una(clnt_id):
    if clnt_id.isnumeric():
        id = int(clnt_id)

        for pelicula in peliculas:
            if pelicula["id"] == id:
                return jsonify(pelicula), HTTPStatus.OK
        return jsonify("ERROR: <" + str(id) + "> no existe"), HTTPStatus.NOT_FOUND
    else:
        return jsonify("ERROR: <id> debe ser entero"), HTTPStatus.BAD_REQUEST


@servidor_API.route("/peliculas/director/<clnt_id>", methods=["GET"])
def peliculas_devolver_por_director(clnt_id):
    if clnt_id.isnumeric():
        id = int(clnt_id)

        rspPeliculas = [p for p in peliculas if str(p["director_id"]) == str(id)]

        return jsonify(rspPeliculas), HTTPStatus.OK
    else:
        return jsonify("ERROR: <id> debe ser entero"), HTTPStatus.BAD_REQUEST


@servidor_API.route("/peliculas/con_portada/", methods=["GET"])
@servidor_API.route("/peliculas/con_portada", methods=["GET"])
def peliculas_devolver_con_poster():
    rspPeliculas = [p for p in peliculas if len(p["póster"]) > 0]

    return jsonify(rspPeliculas), HTTPStatus.OK


@servidor_API.route("/pelicula/", methods=["POST"])
@servidor_API.route("/pelicula", methods=["POST"])
def peliculas_agregar_una():
    global ult_id_peliculas
    global usuario_id_auth

    clnt_data = request.get_json()

    if usuario_chequear_logged():
        if len(clnt_data["título"]) > 0 and len(clnt_data["año"]) > 0 and len(clnt_data["director_id"]) > 0:
            ult_id_peliculas += 1

            id = ult_id_peliculas
            titulo = clnt_data["título"]
            ano = clnt_data["año"]
            director_id = clnt_data["director_id"]
            genero_id = clnt_data["género_id"] if "género_id" in clnt_data else ""
            sinopsis = clnt_data["sinopsis"] if "sinopsis" in clnt_data else ""
            poster = clnt_data["póster"] if "póster" in clnt_data else ""
            usuario_id = usuario_id_auth

            peliculas.append({
                "id": id,
                "título": titulo,
                "año": ano,
                "director_id": director_id,
                "género_id": genero_id,
                "sinopsis": sinopsis,
                "póster": poster,
                "usuario_id": usuario_id
            })

            objArchivo = open(ruta_data_peliculas, "w", encoding="utf-16")
            objArchivo.write(json.dumps(peliculas, indent=4, ensure_ascii=False))
            objArchivo.close()

            return jsonify("INFO: película agregada: " + str(id)), HTTPStatus.CREATED
        else:
            return jsonify("ERROR: <título> <año> <director_id> deben estar presentes"), HTTPStatus.BAD_REQUEST
    else:
        return jsonify("ERROR: debe loguearse para agregar esta película"), HTTPStatus.FORBIDDEN


@servidor_API.route("/pelicula/<clnt_id>", methods=["PUT"])
def peliculas_modificar_una(clnt_id):
    global ult_id_peliculas
    global usuario_id_auth

    id = int(clnt_id)

    clnt_data = request.get_json()

    if usuario_chequear_logged():
        if len(clnt_data["título"]) > 0 and len(clnt_data["año"]) > 0 and len(clnt_data["director_id"]) > 0:
            for i in range(len(peliculas)):
                if peliculas[i]["id"] == id:
                    titulo = clnt_data["título"]
                    ano = clnt_data["año"]
                    director_id = clnt_data["director_id"]
                    genero_id = clnt_data["género_id"] if "género_id" in clnt_data else ""
                    sinopsis = clnt_data["sinopsis"] if "sinopsis" in clnt_data else ""
                    poster = clnt_data["póster"] if "póster" in clnt_data else ""

                    peliculas[i]["título"] = titulo
                    peliculas[i]["año"] = ano
                    peliculas[i]["director_id"] = director_id
                    peliculas[i]["género_id"] = genero_id
                    peliculas[i]["sinopsis"] = sinopsis
                    peliculas[i]["póster"] = poster

                    objArchivo = open(ruta_data_peliculas, "w", encoding="utf-16")
                    objArchivo.write(json.dumps(peliculas, indent=4, ensure_ascii=False))
                    objArchivo.close()

                    return jsonify("INFO: película actualizada!"), HTTPStatus.OK

            return jsonify("ERROR: película no encontrada"), HTTPStatus.NOT_FOUND
        else:
            return jsonify("ERROR: <título> <año> <director_id> deben estar presentes"), HTTPStatus.BAD_REQUEST
    else:
        return jsonify("ERROR: debe loguearse para modificar esta película"), HTTPStatus.FORBIDDEN


@servidor_API.route("/pelicula/", methods=["DELETE"])
@servidor_API.route("/pelicula", methods=["DELETE"])
def peliculas_borrar_una():
    global usuario_id_auth

    clnt_data = request.get_json()

    id = clnt_data["id"]

    if usuario_chequear_logged():
        if "id" in clnt_data:
            for i in range(len(peliculas)):
                if peliculas[i]["id"] == int(id):
                    if peliculas[i]["usuario_id"] == usuario_id_auth:
                        if checkear_comentarios_foraneos(usuario_id_auth, id):
                            return jsonify("ERROR: no puede eliminarse, existen comentarios foráneos"), HTTPStatus.FORBIDDEN
                        else:
                            pelicula_eliminada = peliculas.pop(i)

                            objArchivo = open(ruta_data_peliculas, "w", encoding="utf-16")
                            objArchivo.write(json.dumps(peliculas, indent=4, ensure_ascii=False))
                            objArchivo.close()

                            return jsonify("INFO: película eliminada!"), HTTPStatus.OK
                    else:
                        return jsonify("ERROR: la película no es de su autoría"), HTTPStatus.FORBIDDEN
            return jsonify("INFO: <" + str(id) + "> no existe"), HTTPStatus.NOT_FOUND
        else:
            return jsonify("INFO: <id> debe estar presente"), HTTPStatus.BAD_REQUEST
    else:
        return jsonify("ERROR: debe loguearse para borrar esta película"), HTTPStatus.FORBIDDEN


# - Comentarios
@servidor_API.route("/comentarios/", methods=["GET"])
@servidor_API.route("/comentarios", methods=["GET"])
def comentarios_devolver_todos():
    return jsonify(comentarios), HTTPStatus.OK


@servidor_API.route("/pelicula/<clnt_id>/comentarios/", methods=["GET"])
@servidor_API.route("/pelicula/<clnt_id>/comentarios", methods=["GET"])
def comentarios_devolver_por_pelicula(clnt_id):
    if clnt_id.isnumeric():
        id = int(clnt_id)

        comentarios_por_pelicula = [comentario for comentario in comentarios if comentario["película_id"] == id]

        return jsonify(comentarios_por_pelicula), HTTPStatus.OK
    else:
        return jsonify("[err] - <id> debe ser entero"), HTTPStatus.BAD_REQUEST


@servidor_API.route("/usuario/<clnt_id>/comentarios/", methods=["GET"])
@servidor_API.route("/usuario/<clnt_id>/comentarios", methods=["GET"])
def comentarios_devolver_por_usuario(clnt_id):
    if clnt_id.isnumeric():
        id = int(clnt_id)

        for comentario in comentarios:
            if comentario["usuario_id"] == id:
                return jsonify(comentario["opinión"]), HTTPStatus.OK
        return jsonify("[nfo] - <" + str(id) + "> no existe"), HTTPStatus.NOT_FOUND
    else:
        return jsonify("[err] - <id> debe ser entero"), HTTPStatus.BAD_REQUEST


@servidor_API.route("/pelicula/<clnt_id>/comentario/", methods=["POST"])
@servidor_API.route("/pelicula/<clnt_id>/comentario", methods=["POST"])
def comentarios_agregar_uno(clnt_id):
    global ult_id_comentarios
    global usuario_id_auth

    clnt_data = request.get_json()

    if usuario_chequear_logged():
        if clnt_id.isnumeric():
            ult_id_comentarios += 1

            id = int(clnt_id)

            if "opinión" in clnt_data:
                comentarios.append({
                    "id": ult_id_comentarios,
                    "película_id": id,
                    "opinión": clnt_data["opinión"],
                    "usuario_id": usuario_id_auth
                })

                objArchivo = open(ruta_data_comentarios, "w", encoding="utf-16")
                objArchivo.write(json.dumps(comentarios, indent=4, ensure_ascii=False))
                objArchivo.close()

                return jsonify("INFO: opinión agregada!"), HTTPStatus.CREATED
            else:
                return jsonify("ERROR: <id> <opinión> deben estar presentes"), HTTPStatus.BAD_REQUEST
        else:
            return jsonify("ERROR: <id> debe ser entero"), HTTPStatus.BAD_REQUEST
    else:
        return jsonify("ERROR: debe loguearse para agregar este comentario"), HTTPStatus.FORBIDDEN


# - Directores
@servidor_API.route("/directores/", methods=["GET"])
@servidor_API.route("/directores", methods=["GET"])
def directores_devolver_todos():
    return jsonify(directores), HTTPStatus.OK


@servidor_API.route("/director/<clnt_id>", methods=["GET"])
def directores_devolver_uno(clnt_id):
    if clnt_id.isnumeric():
        id = int(clnt_id)

        for director in directores:
            if director["id"] == id:
                return jsonify(director["nombre"]), HTTPStatus.OK
        return jsonify("INFO: <" + str(id) + "> no existe"), HTTPStatus.NOT_FOUND
    else:
        return jsonify("ERROR: <id> debe ser entero"), HTTPStatus.BAD_REQUEST


# - Géneros
@servidor_API.route("/generos/", methods=["GET"])
@servidor_API.route("/generos", methods=["GET"])
def generos_devolver_todos():
    return jsonify(generos), HTTPStatus.OK


@servidor_API.route("/genero/<clnt_id>", methods=["GET"])
def generos_devolver_uno(clnt_id):
    if clnt_id.isnumeric():
        id = int(clnt_id)

        for genero in generos:
            if genero["id"] == id:
                return jsonify(genero["denominación"]), HTTPStatus.OK
        return jsonify("INFO: <" + str(id) + "> no existe"), HTTPStatus.NOT_FOUND
    else:
        return jsonify("ERROR: <id> debe ser entero"), HTTPStatus.BAD_REQUEST


servidor_API.run()