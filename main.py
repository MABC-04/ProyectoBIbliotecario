from fastapi import FastAPI
from modelos.__init__ import CrearTablas

app = FastAPI(
    title="Proyecto de gestiom biblioteca",
    description="Implementacion de operaciones http",
    summary="API para la gestion de libros",
    version="0.0.1"
)

@app.on_event("startup")
def startup():
    CrearTablas()

@app.on_event("shutdown")
def shutdown():
    print("Cerrando API...")

@app.get("/")
async def index():
    return {"Proyecto de gestion bibliotecaria"}

@app.get("/about")
async def about():
    return {"About"}