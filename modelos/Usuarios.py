from peewee import Model, AutoField, CharField
from core import   BDCONEXION



class Usuario(Model):
    id_Usuario = AutoField(unique=True)
    nombre = CharField(max_length=100, null=False)
    Email = CharField(max_length=100, null=False)
    telefono = CharField(max_length=100, null=False)
    direccion = CharField(max_length=100, null=False)


    def __str__(self):

        return str(self.id_Usuario)


    class Meta:
        DB = BDCONEXION.DB
        db_table = "Usuario"

