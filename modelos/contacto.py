from dataBase import dataBase

class Contacto(dataBase):
    def __init__(self):
        self.con = super().conexion()
#nombre,id_g,tip,num,corr,dire
    def registra_contacto(self, *args):
        cur = self.con.cursor()
        sql = "INSERT INTO contactos (nombre,id_grupo,tipo_t,numero,correo,direccion) VALUES (%s, %s, %s, %s, %s, %s);"
        data = (args[0],args[1],args[2],args[3],args[4],args[5])
        cur.execute(sql, data)
        self.con.commit()
        #ojo esto puede dar problemas
        cur.close()
        self.con.close()

    def busca_contacto(self, *args):
        cur = self.con.cursor()
        if args[1] == None:
            sql = f"""SELECT contactos.nombre,contactos.numero,tipo_tel.tipo,grupo.nombre,
            contactos.correo,contactos.direccion
            FROM contactos 
            INNER JOIN tipo_tel ON tipo_tel.id=contactos.tipo_t
            INNER JOIN grupo ON grupo.id=contactos.id_grupo
            WHERE contactos.nombre LIKE '%{args[0]}%' 
            AND contactos.correo LIKE '%{args[2]}%' AND contactos.direccion LIKE '%{args[3]}%';"""
        else:
            sql = f"""SELECT contactos.nombre,contactos.numero,tipo_tel.tipo,grupo.nombre,
            contactos.correo,contactos.direccion
            FROM contactos 
            INNER JOIN tipo_tel ON tipo_tel.id=contactos.tipo_t
            INNER JOIN grupo ON grupo.id=contactos.id_grupo
            WHERE contactos.nombre LIKE '%{args[0]}%' 
            AND contactos.numero={args[1]} AND contactos.correo LIKE '%{args[2]}%' AND contactos.direccion LIKE '%{args[3]}%';"""
        cur.execute(sql)
        return cur.fetchall()

    def todos_los_contactos(self):
        cur = self.con.cursor()
        sql = """SELECT contactos.nombre,tipo_tel.tipo,contactos.numero,contactos.correo,contactos.direccion,
         grupo.nombre FROM contactos
         INNER JOIN grupo ON grupo.id=contactos.id_grupo
         INNER JOIN tipo_tel ON tipo_tel.id=contactos.tipo_t;"""
        cur.execute(sql)
        res = cur.fetchall()
        datos = []
        for i in res:
            datos.append(i)
        return datos

    def elimina_contacto(self, nombre, tel):
        cur = self.con.cursor()
        sql = f"DELETE FROM contactos WHERE nombre='{nombre}' AND numero={tel};"
        cur.execute(sql)
        self.con.commit()
        
    def atualiza_contacto(self, *args):
        cur = self.con.cursor()
        sql = f"UPDATE contactos SET nombre='{args[0]}' WHERE id="


#ALTER SEQUENCE contactos_id_seq RESTART WITH 0

