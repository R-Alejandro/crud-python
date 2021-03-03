#librerias
from tabulate import tabulate
import sys 
sys.path.append("..") #carpeta root 
from controladores.controlGeneral import controlGeneral

if __name__ == '__main__':
#funciones 
    objeto = controlGeneral()
    #programa main
    bandera = True
    menu = [['Acciones','Opciones'],['Añadir Contacto','1'],['Buscar Contacto','2'],
            ['Eliminar Contacto','3'],['Actualizar Contacto','4'],['Exportar Datos','5'],['Salir','6']]

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
            pass
        if opcion == 6:
            bandera = False
