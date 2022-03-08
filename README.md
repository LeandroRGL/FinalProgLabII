# Proyecto Final 2021
# Programación II - Lab. Programación II - TUP UTN FRBB
## Agustín Ascolani & Leandro M. Regolf

Crear una plataforma web para mantener una lista de películas recomendadas por parte de los usuarios

### Back-end
- Servidor API (server.py) (URLBase -> localhost:5000) ■■■
- CORS ■■□
- Data inicial JSON archivos externos ■■■
- Servicos básicos
  - Sistema de log-in ■■□<br/>
    &nbsp;&nbsp;&nbsp;/login&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;/logout
- Otros servicios
  - Devolver la lista de directores presentes en la plataforma ■■□<br/>
    &nbsp;&nbsp;&nbsp;/directores&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;/directores/
  - Devolver la lista de géneros presentes en la plataforma ■■□<br/>
    &nbsp;&nbsp;&nbsp;/generos&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;/generos/
  - Devolver la lista de películas dirigidas por un director en particular □□□<br/>
    &nbsp;&nbsp;&nbsp;localhost:5000/
  - Devolver las películas que tienen imagen de portada agregada □□□<br/>
    &nbsp;&nbsp;&nbsp;/peliculas/con_portada&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;/peliculas/con_portada/
  - ABM de cada película<br/>
    &nbsp;&nbsp;&nbsp;ALTA:&nbsp;&nbsp;&nbsp;/peliculas ■□□<br/>
    &nbsp;&nbsp;&nbsp;BAJA:&nbsp;&nbsp;&nbsp;/peliculas ■■□<br/>
    &nbsp;&nbsp;&nbsp;MODIF:&nbsp;&nbsp;&nbsp;/peliculas □□□<br/>

### Front-end
- Diseño básico (CSS precario) ■□□
- Diseño responsivo (CSS ausente) □□□
- Consulta básica GET ■■□
- Consulta básica POST ■■□
- Página LogIn (loginKCO.htm) ■■□
- Página LogOut (logoutKCO.htm) ■■□
- Página principal (indexKCO.htm) ■□□
- Película (peliculaKCO.htm) ■□□
  - ver ■■□
  - agregar comentario (precario) ■□□
  - borrar ■■□
- Película (agregarKCO.htm) ■□□
  - alta ■□□
  - modificar □□□

### Puntuales
- Listado películas (público) ■■□
- Listado películas (loguado) ■■□
- Ver película (público) ■□□
- Ver película (logueado) ■□□

### Recursos
- https://www.imdb.com/
- https://www.movieposters.com/
