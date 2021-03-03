#librerias
from tabulate import tabulate
import sys 
sys.path.append("..") #carpeta root 
from controladores.controlGeneral import controlGeneral

if __name__ == '__main__':
    objeto = controlGeneral()
    bandera = True
    menu = [['Acciones','Opciones'],['Añadir Contacto','1'],['Buscar Contacto','2'],
            ['Eliminar Contacto','3'],['Actualizar Contacto','4'],['Todos los Contactos','5'],['Salir','6']]

    while bandera:
        print(" MENU \n------------------------------------")
        print(tabulate(menu,headers='firstrow',tablefmt='pipe'))
        opcion = int(input("\nOpcion:: "))

        if opcion == 1:
            objeto.nuevo_contacto()
        if opcion == 2:
            objeto.buscar_contacto()
        if opcion == 3:
            objeto.eliminar()
        if opcion == 4:
            objeto.actualizar()
        if opcion == 5:
            objeto.todos()
        if opcion == 6:
            bandera = False
