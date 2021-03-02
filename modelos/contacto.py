import sys
sys.path.append("..")
from modelos.dataBase import dataBase

class Contacto(dataBase):
    def __init__(self):
        self.con = super().conexion()

    def registra_contacto(self, nombre,id_g,tip,num,corr,dire):
        cur = self.con.cursor()
        sql = "INSERT INTO contactos (nombre,id_grupo,tipo_t,numero,correo,direccion) VALUES (%s, %s, %s, %s, %s, %s);"
        data = (nombre,id_g,tip,num,corr,dire)
        cur.execute(sql, data)
        self.con.commit()

    def busca_contacto(self, nombre, tel=None):
        pass
    def todos_los_contactos(self):
        cur = self.con.cursor()
        sql = """SELECT contactos.nombre,contactos.numero,contactos.correo,contactos.direccion,
         grupo.nombre, tipo_tel.tipo FROM contactos
         INNER JOIN grupo ON grupo.id=contactos.id_grupo
         INNER JOIN tipo_tel ON tipo_tel.id=contactos.tipo_t;"""
        cur.execute(sql)
        res = cur.fetchall()
        datos = []
        for i in res:
            datos.append(i)
        return datos

    def elimina_contacto(self, nombre, tel):
        pass
    def elimina_telefono(self, tel):
        pass
    def atualiza_contacto(self, *args):
        pass

obj = Contacto()
lis = obj.todos_los_contactos()
for i in lis:
    print(i)

#ALTER SEQUENCE product_id_seq RESTART WITH 1453

