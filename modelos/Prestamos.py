from datetime import date
from modelos.Usuarios import Usuario
from modelos.Libros import Libro
from peewee import Model, DateField, ForeignKeyField
from core import BDCONEXION


class Prestamos(Model):
    Usuario = ForeignKeyField(Usuario, backref="Prestamos", on_delete='CASCADE')
    Libro = ForeignKeyField(Libro, backref="Prestamos", on_delete='CASCADE')
    fechaPrestamoSolicitado = DateField(default=date.today)
    fechaPrestamoDevolucion = DateField(null=True)
    fechaLimiteDevolucion = DateField()



    class Meta:
        database = BDCONEXION.DB
        db_table = "prestamos"