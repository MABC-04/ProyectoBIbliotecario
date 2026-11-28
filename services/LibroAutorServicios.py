from fastapi import APIRouter, HTTPException, status
from modelos.Libros import Libro, Libro_Autor
from modelos.Autores import Autor
from schemas import LibroAutorSchema

router = APIRouter(prefix="/libro-autores", tags=["Libro - Autores"])


def _formatear_relacion(relacion: Libro_Autor) -> dict:
    """Construye la respuesta incluyendo los datos completos del libro y del autor."""
    return {
        "id": relacion.id,
        "libro": relacion.libro.__data__,
        "autor": relacion.autores.__data__,
    }


@router.post("/", status_code=status.HTTP_201_CREATED)
def asignar_autor_a_libro(datos: LibroAutorSchema):
    libro = Libro.get_or_none(Libro.Id_Libro == datos.libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    autor = Autor.get_or_none(Autor.id_Autores == datos.autor_id)
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    # Evita registrar exactamente la misma relación dos veces
    existente = Libro_Autor.get_or_none(
        (Libro_Autor.libro == libro.Id_Libro)
        & (Libro_Autor.autores == autor.id_Autores)
    )
    if existente is not None:
        raise HTTPException(
            status_code=400, detail="Este autor ya está asignado a este libro"
        )

    nueva_relacion = Libro_Autor.create(
        libro=libro.Id_Libro,
        autores=autor.id_Autores,
    )
    return {
        "mensaje": "Autor asignado al libro correctamente",
        "detalle": _formatear_relacion(nueva_relacion),
    }


@router.get("/")
def listar_libros_autores():
    """Lista todas las relaciones mostrando la información del libro y su autor."""
    relaciones = list(
        Libro_Autor.select(Libro_Autor, Libro, Autor)
        .join(Libro)
        .switch(Libro_Autor)
        .join(Autor)
    )
    if not relaciones:
        raise HTTPException(
            status_code=404, detail="No hay relaciones libro-autor registradas"
        )

    return [_formatear_relacion(rel) for rel in relaciones]


@router.get("/{relacion_id}")
def obtener_libro_autor(relacion_id: int):
    """Consulta una relación específica por su ID con los datos del libro y autor."""
    relacion = Libro_Autor.get_or_none(Libro_Autor.id == relacion_id)
    if relacion is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return _formatear_relacion(relacion)


@router.get("/libro/{libro_id}")
def obtener_autores_por_libro(libro_id: int):
    """Consulta un libro y todos los autores que lo escribieron."""
    libro = Libro.get_or_none(Libro.Id_Libro == libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    relaciones = list(
        Libro_Autor.select(Libro_Autor, Autor)
        .join(Autor)
        .where(Libro_Autor.libro == libro.Id_Libro)
    )
    return {
        "libro": libro.__data__,
        "autores": [rel.autores.__data__ for rel in relaciones],
    }


@router.get("/autor/{autor_id}")
def obtener_libros_por_autor(autor_id: int):
    """Consulta un autor y todos los libros que ha escrito."""
    autor = Autor.get_or_none(Autor.id_Autores == autor_id)
    if autor is None:
        raise HTTPException(status_code=404, detail="Autor no encontrado")

    relaciones = list(
        Libro_Autor.select(Libro_Autor, Libro)
        .join(Libro)
        .where(Libro_Autor.autores == autor.id_Autores)
    )
    return {
        "autor": autor.__data__,
        "libros": [rel.libro.__data__ for rel in relaciones],
    }


@router.delete("/{relacion_id}")
def eliminar_relacion(relacion_id: int):
    """Elimina la vinculación entre un libro y un autor."""
    relacion = Libro_Autor.get_or_none(Libro_Autor.id == relacion_id)
    if relacion is None:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    relacion.delete_instance()
    return {"mensaje": "Relación eliminada correctamente"}