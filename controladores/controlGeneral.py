import sys
sys.path.insert(1,
"C:/Users/Aleja/documents/universidad/programacion/python/crud/controladores")
from controlBase import controlBase

class controlGeneral(controlBase):
    
    def nuevo_contacto(self):
        nombre = input("Ingrese el nombre: ")
        grupo = input("Desea añadir un grupo? Y/N: ")
        if grupo == 'Y':
            grupo = int(input("""[1 -> familiar]\n[2 -> amigo]\n[3 -> trabajo]\n -> """))
            if grupo > 3 or grupo < 1:
                grupo = 0
        else:
            grupo = 0
        tipo_tel = input("Desea añadir un tipo de telefono? Y/N: ")
        if tipo_tel == 'Y':
            tipo_tel = int(input("[100 -> casa]\n[200 -> trabajo]\n[300 -> celular]\n-> "))
        else:
            tipo_tel = 300
        numero = int(input("Ingrese numero del contaco: "))
        correo = input("añadir correo? Y/N: ")
        if correo == 'Y':
            correo = input("-> ")
        else:
            correo = 'no'
        direc = input("añadir direccion? Y/N: ")
        if direc == 'Y':
            direc = input("-> ")
        else:
            direc = 'no'
        self.carga_modelo().registra_contacto(nombre,grupo,tipo_tel,numero,correo,direc)

        print("Usuario Registrado con exito\n\n")
    
    def buscar_contacto(self):
        print("Ingrese datos a buscar del usuario\n")
        nombre = input("Nombre: ")
        numero = input("Numero: ")
        correo = input("Correo: ")
        direcc = input("Direccion: ")
        resultado = self.carga_modelo().busca_contacto(nombre, numero, correo, direcc)
        for i in resultado:
            print(i)
        print("\n")
    
    def eliminar(self):
        print("Ingrese el usuario a eliminar\n")
        nombre = input("Nombre: ")
        numero = input("Numero: ")
        resul = self.carga_modelo().busca_contacto(nombre, numero, '','')
        var = input(f"Esta seguro de eliminar el contacto: {resul} Y/N\n -> ")
        if var == 'Y':
            self.carga_modelo().elimina_contacto(nombre, numero)
            print("Usuario Eliminado")
        else:
            print("operacion cancelada")

    def actualizar(self):
        pass
