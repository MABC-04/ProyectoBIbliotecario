from peewee import Model, CharField, ForeignKeyField, AutoField, DateField
from core import BDCONEXION

class Autores(Model):
    id_Autores = AutoField(unique=True)
    nombre = CharField(max_length=60)
    nacionalidad = CharField(max_length=60)
    fecha_nacimiento = DateField()


class Meta:
    DB = BDCONEXION.DB
    db_table = 'Autores'