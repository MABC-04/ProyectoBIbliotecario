from peewee import Model, AutoField, CharField
from core import   BDCONEXION



class Usuario(Model):
    id_Usuario = AutoField(unique=True)
    nombre = CharField(max_length=100, nullable=False)
    Email = CharField(max_length=100, nullable=False)
    telefono = CharField(max_length=100, nullable=False)
    direccion = CharField(max_length=100, nullable=False)


    def __str__(self):

        return str(self.id_Usuario)

    class Meta:
        DB = BDCONEXION.DB
        db_table = 'usuarios'

