from fastapi import APIRouter, HTTPException, status
from modelos.Libros import Libro
from schemas import libroschema

router = APIRouter(prefix="/libros", tags=["Libros"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_libro(info: libroschema):
    nuevo_libro = Libro.create(
        titulo=info.titulo,
        editorial=info.editorial,
        Fecha_Publicacion=info.fecha_publicacion,
        Categoria=info.Categoria,
        Stock=info.stock,
    )
    return nuevo_libro.__data__


@router.get("/{libro_id}")
def get_libro(libro_id: int):
    libro = Libro.get_or_none(Libro.Id_Libro == libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro.__data__


@router.put("/{libro_id}")
def put_libro(libro_id: int, info: libroschema):
    libro = Libro.get_or_none(Libro.Id_Libro == libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    if info.titulo and info.titulo != "string":
        libro.titulo = info.titulo
    if info.editorial and info.editorial != "string":
        libro.editorial = info.editorial
    if info.fecha_publicacion:
        libro.Fecha_Publicacion = info.fecha_publicacion
    if info.Categoria and info.Categoria != "string":
        libro.Categoria = info.Categoria
    if info.stock is not None:
        libro.Stock = info.stock

    libro.save()
    return libro.__data__