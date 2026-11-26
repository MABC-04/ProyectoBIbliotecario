from fastapi import FastAPI

from modelos import Libro
from modelos.__init__ import CrearTablas
from modelos.Usuarios import Usuario
from schemas import *

app = FastAPI(
    title="Proyecto de gestiom biblioteca",
    description="Implementacion de operaciones http",
    summary="API para la gestion de libros",
    version="0.0.1"
)

@app.on_event("startup")
def startup():
    CrearTablas()
    print("Creando base de datos....")

@app.on_event("shutdown")
def shutdown():
    print("Cerrando API...")

@app.get("/")
async def index():
    return {"Proyecto de gestion bibliotecaria"}

@app.get("/about")
async def about():
    return {"About"}


#peticion para los usuarios

@app.post("/usuario/")
async def crearusuario(datos: UsuarioSchema):
    datos = Usuario.create(
        nombre=datos.nombre,
        email=datos.email,
        telefono=datos.telefono,
        direccion=datos.direccion,
    )

@app.get("/usuario/{id}")
def get_usuario(usuario_id: int):
    usuario = Usuario.get_or_none(Usuario.id_usuario == usuario_id)
    return usuario


#peticiones para los libros

@app.post("/libros/")
async def crear_libro(info: libroschema):
    info = Libro.create(
        titulo = info.titulo,
        editorial = info.editorial,
        fecha_publicacion = info.fecha_publicacion,
        categoria = info.categoria,
        stock = info.stock,
    )
