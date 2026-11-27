from datetime import datetime, date
from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nombre: str
    email: str
    telefono: str
    direccion: str


class libroschema(BaseModel):
    titulo: str
    editorial: str
    fecha_publicacion:date
    Categoria: str
    stock: int


#schemas para prestamos

class prestamoschema(BaseModel):
    usuario: UsuarioSchema
    libro: libroschema
    fechaPrestamoSolicitado : date
    fechaPrestamoDevolucion: date
    FechalLimiteDevolucion: date



#Schema para autores

class AutoresSchema(BaseModel):
    nombre: str
    nacionalidad: str
    fecha_nacimiento: date

