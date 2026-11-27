from datetime import date, timedelta
from fastapi import APIRouter, HTTPException, status
from modelos.Libros import Libro
from modelos.Usuarios import Usuario
from modelos.Prestamos import Prestamos

router = APIRouter(prefix="/prestamos", tags=["Préstamos"])


@router.post("/solicitar", status_code=status.HTTP_201_CREATED)
def post_prestamo(usuario_id: int, libro_id: int, fecha_limite: date | None = None):
    usuario = Usuario.get_or_none(Usuario.id_Usuario == usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    libro = Libro.get_or_none(Libro.Id_Libro == libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")

    if libro.Stock <= 0:
        raise HTTPException(
            status_code=400, detail="No existen más copias disponibles para préstamo"
        )

    libro.Stock = libro.Stock - 1
    libro.save()

    nuevo_prestamo = Prestamos.create(
        Usuario=usuario.id_Usuario,
        Libro=libro.Id_Libro,
        fechaPrestamoSolicitado=date.today(),
        fechaPrestamoDevolucion=None,
        fechaLimiteDevolucion=fecha_limite or (date.today() + timedelta(days=7)),
    )
    return {
        "mensaje": "Se ha completado el préstamo con éxito",
        "prestamo": nuevo_prestamo.__data__,
    }


@router.put("/devolucion/{prestamo_id}")
def devolucion(prestamo_id: int, fecha_devolucion: date | None = None):
    prestamo = Prestamos.get_or_none(Prestamos.id == prestamo_id)
    if prestamo is None:
        raise HTTPException(status_code=404, detail="Préstamo no encontrado")

    if prestamo.fechaPrestamoDevolucion is not None:
        raise HTTPException(
            status_code=400, detail="Este préstamo ya fue devuelto anteriormente"
        )

    libro = Libro.get_or_none(Libro.Id_Libro == prestamo.Libro_id)
    if libro is not None:
        libro.Stock = libro.Stock + 1
        libro.save()

    prestamo.fechaPrestamoDevolucion = fecha_devolucion or date.today()
    prestamo.save()

    return {
        "mensaje": "Devolución registrada con éxito",
        "prestamo": prestamo.__data__,
    }