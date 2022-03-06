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
usuario_id_auth = 1
usuario_nombre_auth = ""


# - - Data inicial - -
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

ult_id_usuarios = 3
ult_id_peliculas = 5
ult_id_directores = 4
ult_id_generos = 5
ult_id_comentarios = 4


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


def check_tiene_poster(pelicula):
    if len(pelicula["póster"]) > 0:
        return True
    else:
        return False

def check_es_dirigida_por(pelicula, director_id):
    if pelicula["director_id"] == director_id:
        return True
    else:
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
@servidor_API.route("/usuarios", methods=["GET"])
@servidor_API.route("/usuarios/", methods=["GET"])
def usuarios_devolver_todos():
    if usuario_chequear_logged():
        return jsonify(usuarios), HTTPStatus.OK
    else:
        return jsonify("no leogueado"), HTTPStatus.FORBIDDEN

@servidor_API.route("/login", methods=["POST"])
def usuarios_devolver_login():
    clnt_data = request.get_json()

    if "usuario" in clnt_data and "clave" in clnt_data:
        for usuario in usuarios:
            if usuario["nombre"] == clnt_data["usuario"] and usuario["clave"] == clnt_data["clave"]:
                usuario_loguear(usuario["id"], usuario["nombre"])

                return jsonify("Bienvenido " + usuario["nombre"] + "!"), HTTPStatus.OK
        return jsonify("[nfo] - <usuario> o <clave> incorrecta"), HTTPStatus.NOT_FOUND
    else:
        return jsonify("[err] - request incompleto"), HTTPStatus.BAD_REQUEST

@servidor_API.route("/logout", methods=["POST"])
def usuarios_devolver_logout():
    usuario_desloguear()

    return jsonify("Deslogueado!"), HTTPStatus.OK




# - Películas
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
                return jsonify(pelicula), HTTPStatus.OK
        return jsonify("[nfo] - <" + str(id) + "> no existe"), HTTPStatus.NOT_FOUND
    else:
        return jsonify("[err] - <id> debe ser entero"), HTTPStatus.BAD_REQUEST



@servidor_API.route("/peliculas/directores/<clnt_id>", methods=["GET"])
def peliculas_devolver_por_director(clnt_id):
    # peliculas_dirigida_por = list(filter(check_es_dirigida_por(2), peliculas))

    return jsonify("peliculas_dirigida_por"), HTTPStatus.BAD_REQUEST


@servidor_API.route("/peliculas/con_portada", methods=["GET"])
@servidor_API.route("/peliculas/con_portada/", methods=["GET"])
def peliculas_devolver_con_poster(clnt_id):
    peliculas_con_poster = list(filter(check_tiene_poster, peliculas))

    return jsonify(peliculas_con_poster), HTTPStatus.OK


@servidor_API.route("/peliculas", methods=["POST"])
@servidor_API.route("/peliculas/", methods=["POST"])
def peliculas_agregar_una():
    global ult_id_peliculas
    global usuario_id_auth

    clnt_data = request.get_json()

    if usuario_chequear_logged():
        # if "título" in clnt_data and "año" in clnt_data and "director_id" in clnt_data:
        if len(clnt_data["título"]) > 0 and len(clnt_data["año"]) > 0 and len(clnt_data["director_id"]) > 0:
            ult_id_peliculas += 1

            id = ult_id_peliculas
            titulo = clnt_data["título"]
            ano = clnt_data["año"]
            director_id = clnt_data["director_id"]
            genero_id = clnt_data["género"] if "género" in clnt_data else ""
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

            return jsonify("agregado: " + str(id)), HTTPStatus.CREATED
        else:
            return jsonify("ERROR: <título> <año> <director_id> deben estar presentes"), HTTPStatus.BAD_REQUEST
    else:
        return jsonify("no leogueado"), HTTPStatus.FORBIDDEN




@servidor_API.route("/peliculas/ggg/comentario/", methods=["POST"])
@servidor_API.route("/peliculas/ggg/comentario", methods=["POST"])
def peliculas_agregar_unad():
    global ult_id_peliculas
    global usuario_id_auth

    clnt_data = request.get_json()

    if usuario_chequear_logged():
        # if "título" in clnt_data and "año" in clnt_data and "director_id" in clnt_data:
        if len(clnt_data["título"]) > 0 and len(clnt_data["año"]) > 0 and len(clnt_data["director_id"]) > 0:
            ult_id_peliculas += 1

            id = ult_id_peliculas
            titulo = clnt_data["título"]
            ano = clnt_data["año"]
            director_id = clnt_data["director_id"]
            genero_id = clnt_data["género"] if "género" in clnt_data else ""
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

            return jsonify("agregado: " + str(id)), HTTPStatus.CREATED
        else:
            return jsonify("ERROR: <título> <año> <director_id> deben estar presentes"), HTTPStatus.BAD_REQUEST
    else:
        return jsonify("no leogueado"), HTTPStatus.FORBIDDEN




@servidor_API.route("/peliculas", methods=["DELETE"])
@servidor_API.route("/peliculas/", methods=["DELETE"])
def peliculas_borrar_una():
    clnt_data = request.get_json()

    id = clnt_data["id"]

    if usuario_chequear_logged():
        if "id" in clnt_data:
            for i in range(len(peliculas)):
                if peliculas[i]["id"] == id:
                    pelicula_eliminada = peliculas.pop(i)

                    return jsonify(pelicula_eliminada), HTTPStatus.OK

            return jsonify("[nfo] - <" + str(id) + "> no existe"), HTTPStatus.NOT_FOUND
        else:
            return jsonify("[err] - <id> debe estar presente"), HTTPStatus.BAD_REQUEST
    else:
        return jsonify("no leogueado"), HTTPStatus.FORBIDDEN



# - Comentarios
@servidor_API.route("/comentarios", methods=["GET"])
@servidor_API.route("/comentarios/", methods=["GET"])
def comentarios_devolver_todos():
    return jsonify(comentarios), HTTPStatus.OK

@servidor_API.route("/peliculas/<clnt_id>/comentarios", methods=["GET"])
@servidor_API.route("/peliculas/<clnt_id>/comentarios/", methods=["GET"])
def comentarios_devolver_por_pelicula(clnt_id):
    if clnt_id.isnumeric():
        id = int(clnt_id)

        comentarios_por_pelicula = [comentario for comentario in comentarios if comentario["película_id"] == id]

        return jsonify(comentarios_por_pelicula), HTTPStatus.OK
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

@servidor_API.route("/peliculas/<clnt_id>/comentario/", methods=["POST"])
@servidor_API.route("/peliculas/<clnt_id>/comentario", methods=["POST"])
def comentarios_agregar_uno(clnt_id):
    if clnt_id.isnumeric():
        id = int(clnt_id)

        clnt_data = request.get_json()

        if "opinión" in clnt_data:
            comentarios.append({
                "id": id,
                "película_id": id,
                "opinión": clnt_data["opinión"],
                "usuario_id": 2
            })

            return jsonify(clnt_data), HTTPStatus.CREATED
        else:
            return jsonify("[err] - <opinión> debe estar presente"), HTTPStatus.BAD_REQUEST
    else:
        return jsonify("[err] - <id> debe ser entero"), HTTPStatus.BAD_REQUEST
    # global ult_id_peliculas
    # global usuario_id_auth
    #
    # clnt_data = request.get_json()
    #
    # if usuario_chequear_logged():
    #     # if "título" in clnt_data and "año" in clnt_data and "director_id" in clnt_data:
    #     if len(clnt_data["título"]) > 0 and len(clnt_data["año"]) > 0 and len(clnt_data["director_id"]) > 0:
    #         ult_id_peliculas += 1
    #
    #         id = ult_id_peliculas
    #         titulo = clnt_data["título"]
    #         ano = clnt_data["año"]
    #         director_id = clnt_data["director_id"]
    #         genero_id = clnt_data["género"] if "género" in clnt_data else ""
    #         sinopsis = clnt_data["sinopsis"] if "sinopsis" in clnt_data else ""
    #         poster = clnt_data["póster"] if "póster" in clnt_data else ""
    #         usuario_id = usuario_id_auth
    #
    #         peliculas.append({
    #             "id": id,
    #             "título": titulo,
    #             "año": ano,
    #             "director_id": director_id,
    #             "género_id": genero_id,
    #             "sinopsis": sinopsis,
    #             "póster": poster,
    #             "usuario_id": usuario_id
    #         })
    #
    #         return jsonify("agregado: " + str(id)), HTTPStatus.CREATED
    #     else:
    #         return jsonify("ERROR: <título> <año> <director_id> deben estar presentes"), HTTPStatus.BAD_REQUEST
    # else:
    #     return jsonify("no leogueado"), HTTPStatus.FORBIDDEN

# - Directores
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
        return jsonify("INFO: <" + str(id) + "> no existe"), HTTPStatus.NOT_FOUND
    else:
        return jsonify("ERROR: <id> debe ser entero"), HTTPStatus.BAD_REQUEST


# - Géneros
@servidor_API.route("/generos", methods=["GET"])
@servidor_API.route("/generos/", methods=["GET"])
def generos_devolver_todos():
    return jsonify(generos), HTTPStatus.OK

@servidor_API.route("/peliculas/<clnt_id>/generos", methods=["GET"])
@servidor_API.route("/peliculas/<clnt_id>/generos/", methods=["GET"])
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