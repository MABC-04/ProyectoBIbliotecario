from fastapi import APIRouter, HTTPException, status
from modelos.Autores import Autor
from schemas import AutoresSchema

router = APIRouter(prefix="/autores", tags=["Autores"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def registrar_autores(autor: AutoresSchema):
    nuevo_autor = Autor.create(
        nombre=autor.nombre,
        nacionalidad=autor.nacionalidad,
        fecha_nacimiento=autor.fecha_nacimiento,
    )
    return nuevo_autor.__data__


@router.get("/{autor_id}")
def get_autores(autor_id: int):
    autor = Autor.get_or_none(Autor.id == autor_id)
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")
    return autor.__data__


@router.put("/{autor_id}")
def modificar_autores(autor_id: int, autor: AutoresSchema):
    autor_db = Autor.get_or_none(Autor.id == autor_id)
    if autor_db is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    if autor.nombre and autor.nombre != "string":
        autor_db.nombre = autor.nombre
    if autor.nacionalidad and autor.nacionalidad != "string":
        autor_db.nacionalidad = autor.nacionalidad
    if autor.fecha_nacimiento:
        autor_db.fecha_nacimiento = autor.fecha_nacimiento

    autor_db.save()
    return autor_db.__data__