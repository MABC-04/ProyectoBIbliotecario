from pydantic import BaseModel

class UsuarioSchema(BaseModel):
    nombre: str
    email: str
    telefono: str
    direccion: str