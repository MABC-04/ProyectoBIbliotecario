from peewee import Model, CharField, AutoField, ForeignKeyField, DateField, IntegerField
from modelos import Autores
from core import BDCONEXION

class Libro(Model):
    Id_Libro = AutoField(unique=True)
    titulo = CharField(max_length=200, null=False)
    editorial = CharField(max_length=200, null=False)
    fecha_Publicacion = DateField()
    Categoria = CharField(max_length=20, null=False)
    Stock = IntegerField(null=False, default=1)

    class Meta:
        DB = BDCONEXION.DB
        db_table = 'Libros'

class Libro_Autor(Model):
    Libro = ForeignKeyField(Libro, on_delete='CASCADE')
    autores = ForeignKeyField(Autores.Autor, on_delete='CASCADE')


    class Meta:
        DB = BDCONEXION.DB
        db_table = 'Libro_Autor'