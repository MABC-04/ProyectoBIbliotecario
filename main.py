from contextlib import asynccontextmanager
from fastapi import FastAPI
from modelos.__init__ import CrearTablas
from services import (
    UsuariosServices,
    LibroServices,
    PrestamosServices,
    AutorServices,
    LibroAutorServicios
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    CrearTablas()
    print("Creando base de datos....")
    yield
    print("Cerrando API...")


app = FastAPI(
    title="Proyecto de gestión biblioteca",
    description="Implementación de operaciones HTTP",
    summary="API para la gestión de libros",
    version="0.0.1",
    lifespan=lifespan,
)

app.include_router(UsuariosServices.router)
app.include_router(LibroServices.router)
app.include_router(PrestamosServices.router)
app.include_router(AutorServices.router)
app.include_router(LibroAutorServicios.router)


@app.get("/", tags=["General"])
def index():
    return {"mensaje": "Proyecto de gestión bibliotecaria"}


@app.get("/about", tags=["General"])
def about():
    return {"mensaje": "API de gestión bibliotecaria con FastAPI y Peewee"}