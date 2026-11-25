from modelos.Autores import Autor
from modelos.Libros import Libro, Libro_Autor
from modelos.Usuarios import Usuario
from modelos.Prestamos import Prestamos
from core.BDCONEXION import DB

ALL_MODELOS = [
    Autor,
    Libro,
    Libro_Autor,
    Usuario,
    Prestamos
]

def CrearTablas():
    with DB:
        DB.crearTablas(ALL_MODELOS)


