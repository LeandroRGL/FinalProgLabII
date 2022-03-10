# Proyecto Final 2021
# Programación II - Lab. Programación II - TUP UTN FRBB
## Agustín Ascolani & Leandro M. Regolf

Crear una plataforma web para mantener una lista de películas recomendadas por parte de los usuarios

### Back-end
- Servidor API (server.py) (URLBase -> localhost:5000) ■■■
- CORS ■■■
- Data JSON mediante archivos externos
  - Lectura ■■■
  - Escritura ■■■
- Servicos básicos
  - Sistema de log-in ■■□<br/>
    &nbsp;&nbsp;&nbsp;[URLBase]/usuario/login&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[URLBase]/usuario/logout
- Otros servicios
  - Devolver la lista de directores presentes en la plataforma ■■■<br/>
    &nbsp;&nbsp;&nbsp;[URLBase]/directores&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[URLBase]/directores/
  - Devolver la lista de géneros presentes en la plataforma ■■■<br/>
    &nbsp;&nbsp;&nbsp;[URLBase]/generos &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[URLBase]/generos/
  - Devolver la lista de películas dirigidas por un director en particular ■■■<br/>
    &nbsp;&nbsp;&nbsp;[URLBase]/peliculas/director/<id>
  - Devolver las películas que tienen imagen de portada agregada ■■■<br/>
    &nbsp;&nbsp;&nbsp;[URLBase]/peliculas/con_portada&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[URLBase]/peliculas/con_portada/
  - ABM de cada película<br/>
    &nbsp;&nbsp;&nbsp;ALTA:&nbsp;&nbsp;&nbsp;[URLBase]/peliculas ■■■<br/>
    &nbsp;&nbsp;&nbsp;BAJA:&nbsp;&nbsp;&nbsp;[URLBase]/peliculas ■■■<br/>
    &nbsp;&nbsp;&nbsp;MODIF:&nbsp;&nbsp;&nbsp;[URLBase]/peliculas ■■■<br/>
  - Agregar comentarios ■□□<br/>

### Front-end
- Diseño básico (CSS precario) ■■□
- Diseño responsivo (CSS ausente) ■□□
- Consulta básicas
  - GET ■■■
  - POST ■■■
  - PUT ■■□
  - DELETE ■■■
- LogIn / LogOut
  - LogIn (loginKCO.htm) ■■□
  - LogOut (logoutKCO.htm) ■■□
- Página principal (indexKCO.htm)
  - Películas (NO logueado) ■■□
  - Películas (SI logueado) ■■□
  - Películas por director ■■□
- Película (peliculaKCO.htm)
  - ver ■■□
  - agregar comentario ■■□
  - borrar ■■■
- Película (agregarKCO.htm)
  - alta ■□□
- Película (modificarKCO.htm)
  - modificar ■□□

### Puntuales
- Listado películas (público) ■■□
- Listado películas (loguado) ■■□
- Ver película (público) ■■□
- Ver película (logueado) ■■□

### Extras
- Se implementó persitencia de datos leyendo y guardando datos JSON en archivos externos ■■■

### Recursos
- https://www.imdb.com/
- https://www.movieposters.com/
