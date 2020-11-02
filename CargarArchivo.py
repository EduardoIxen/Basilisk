from  Memory import *
import os.path as path
class CargarArchivo:
    def cargarArchivo(self, ruta_Archivo):
        if path.exists(ruta_Archivo):
            #print(f"El archivo {ruta_Archivo} si existe")
            archivo =open(ruta_Archivo, 'r')
            Memomry.content_script = archivo.readlines()
            archivo.close()
            print(f"Archivo {path.basename(ruta_Archivo)} cargado correctamente")
        elif path.exists(f'Script/{ruta_Archivo}'):
            #print(f'{ruta_Archivo} existe en la carpeta script')
            archivo = open(f'Script/{ruta_Archivo}', 'r')
            Memomry.content_script = archivo.readlines()
            archivo.close()
            print(f"Archivo {path.basename(ruta_Archivo)} cargado correctamente")
        else:
            print(f"El archivo {path.basename(ruta_Archivo)} no existe.")