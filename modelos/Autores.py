from peewee import Model, CharField, ForeignKeyField, AutoField, DateField
from core import BDCONEXION

class Autor(Model):
    id_Autores = AutoField(unique=True)
    nombre = CharField(max_length=60)
    nacionalidad = CharField(max_length=60)
    fecha_nacimiento = DateField()


    class Meta:
        database = BDCONEXION.DB
        db_table = "autor"