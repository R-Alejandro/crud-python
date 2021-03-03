import sys
sys.path.insert(1,
"C:/Users/Aleja/documents/universidad/programacion/python/crud/modelos")
from contacto import Contacto

class controlBase:

    def carga_modelo(self):
        modelo = Contacto()
        return modelo
    