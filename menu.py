#librerias
from tabulate import tabulate
import sys 
sys.path.append("..") #carpeta root 


#funciones 

#programa main
bandera = True
menu = [['Acciones','Opciones'],['Añadir Contacto','1'],['Buscar Contacto','2'],
        ['Eliminar Contacto','3'],['Actualizar Contacto','4'],['Exportar Datos','5'],['Salir',6]]

while bandera:
    print(" MENU \n------------------------------------")
    print(tabulate(menu,headers='firstrow',tablefmt='pipe'))
    opcion = int(input("\nOpcion:: "))

    if opcion == 6:
        bandera = False
