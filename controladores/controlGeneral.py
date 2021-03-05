import sys
from tabulate import tabulate
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
        numero = input("Ingrese numero del contacto: ") #######
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

        print("\nUsuario Registrado con exito\n")
    
    def buscar_contacto(self):
        print("Ingrese datos a buscar del contacto\nPuede saltar valores\n")
        nombre = input("Nombre: ")
        numero = input("Numero: ")
        if len(numero) == 0:
            numero = None  #######
        correo = input("Correo: ")
        direcc = input("Direccion: ")
        resultado = self.carga_modelo().busca_contacto(nombre, numero, correo, direcc)
        if len(resultado) != 0:
            print(f"\n{len(resultado)} contactos encontrados!!!!!")
            tabla = [['Nombre','Grupo','Tipo Telefono','Telefono','Correo','Direccion']]
            for i in resultado:
                tabla.append([i[0],i[1],i[2],i[3],i[4],i[5]])
            print(tabulate(tabla,headers='firstrow',tablefmt='fancy_grid'),'\n')          
        else:
            print("\nContacto no encontrado!!!")
        print()
    
    def todos(self):
        contactos = self.carga_modelo().todos_los_contactos()
        tabla = [['Nombre','Grupo','Tipo Telefono','Telefono','Correo','Direccion']]
        print(f"Contactos:: {len(contactos)}")
        for i in contactos:
            tabla.append([i[0],i[1],i[2],i[3],i[4],i[5]])
        print(tabulate(tabla,headers='firstrow',tablefmt='fancy_grid'),'\n')

    def eliminar(self):
        print("Ingrese el contacto a eliminar\n")
        nombre = input("Nombre: ")
        numero = input("Numero: ")
        resul = self.carga_modelo().busca_contacto(nombre, numero, '','')
        var = input(f"Esta seguro de eliminar el contacto: {resul} Y/N\n -> ")
        if var == 'Y':
            self.carga_modelo().elimina_contacto(nombre, numero)
            print("Usuario Eliminado")
        else:
            print("Operacion cancelada")

    def actualizar(self):
        print("Editar usuario\n")
        nombre = input("Nombre: ")
        numero = input("Numero: ")
        resul = self.carga_modelo().busca_actual(nombre, numero)
        if resul != None:
            var = input(f"Actualizar el contacto: {resul} ? Y/N\n -> ")
            datos = [resul[0],resul[1],resul[2],resul[3],resul[4],resul[5],resul[6]]
            while var == 'Y':
                sel = int(input("""Actualizar\n[1 -> nombre]\n[2 -> grupo]\n[3 -> tipo de telefono]
                \n[4 -> telefono]\n[5 -> correo]\n[6 -> direccion]\n --> """))
                if sel == 1:
                    datos[1] = input("Nuevo Nombre: ")
                if sel == 2:
                    print("[0 -> ninguno]\n[1 -> familiar]\n[2 -> amigo]\n[3 -> trabajo]")
                    datos[2] = int(input("Nuevo Grupo: "))
                if sel == 3:
                    print("[100 -> casa]\n[200 -> trabajo]\n[300 -> celular]")
                    datos[3] = int(input("Nuevo Tipo de telefono: "))
                if sel == 4:
                    datos[4] = input("Nuevo Telefono: ") ####
                if sel == 5:
                    datos[5] = input("Nuevo Correo: ")
                if sel == 6:
                    datos[6] = input("Nueva Direccion: ")

                var = input(f"Seguir editando el contacto? Y/N\n -> ")
                if var == 'N':
                    print(f"Nuevos Datos {datos}")
                    confirma = input("confirmar cambios? Y/N: ")
                    if confirma == 'Y':
                        self.carga_modelo().actualiza_contacto(datos)
                    else:
                        print("Operacion cancelada")
            else:
                print("Actualizacion Terminada")
        else:
            print("El contacto no existe, asegurese que digito bien los datos\n")