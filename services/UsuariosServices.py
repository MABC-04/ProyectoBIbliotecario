from fastapi import APIRouter, HTTPException, status
from modelos.Usuarios import Usuario
from schemas import UsuarioSchema

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_usuario(datos: UsuarioSchema):
    nuevo_usuario = Usuario.create(
        nombre=datos.nombre,
        email=datos.email,
        telefono=datos.telefono,
        direccion=datos.direccion,
    )
    return nuevo_usuario.__data__


@router.get("/{usuario_id}")
def get_usuario(usuario_id: int):
    usuario = Usuario.get_or_none(Usuario.id_Usuario == usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario.__data__


@router.put("/{usuario_id}")
def actualizar_usuario(usuario_id: int, datos: UsuarioSchema):
    usuario = Usuario.get_or_none(Usuario.id_Usuario == usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    campos_enviados = datos.model_dump(exclude_unset=True)
    for campo, valor in campos_enviados.items():
        if valor is not None and valor != "string":
            setattr(usuario, campo, valor)

    usuario.save()
    return usuario.__data__