from datetime import datetime

from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nombre: str
    email: str
    telefono: str
    direccion: str


class libroschema(BaseModel):
    titulo: str
    editorial: str
    fecha_publicacion:datetime
    categoria: str
    stock: int
