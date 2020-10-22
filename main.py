from Memory import *
from CargarArchivo import *
print("comenzando")
ruta = input("Ingrese la ruta del archivo\n")
print(ruta)
cargar = CargarArchivo()
cargar.cargarArchivo(ruta)
print(Memomry.content_script)
num_linea = 1
cadena = ""
estado = 0
lexemas = []
for linea in Memomry.content_script:
    for i in range(len(linea)):
        current = linea[i]
        if estado == 0:
            if current == ',':
                #print('current:', current)
                token = {'Nombre': 'tk_coma', 'Valor': ',', 'Descripcion': 'Separador de atributos', 'Linea': num_linea, 'Columna': i+1}
                print(token)
            elif current == '{':
                #print('current:', current)
                token = {'Nombre': 'tk_LlaveA', 'Valor': '{', 'Descripcion': 'Indica el inicio del contenido de una funcion o sentencia', 'Linea': num_linea, 'Columna': i+1}
                print(token)
            elif current == '}':
                #print('current:', current)
                token = {'Nombre': 'tk_LlaveC', 'Valor': '}', 'Descripcion': 'Indica el final del contenido de una funcion o sentencia', 'Linea': num_linea, 'Columna': i+1}
                print(token)
            elif current == '(':
                #print('current:', current)
                token = {'Nombre': 'tk_ParentesisA', 'Valor': '(', 'Descripcion': 'Indica el inicio del espacio para parametros de una funcion o sentencia', 'Linea': num_linea, 'Columna': i+1}
                print(token)
            elif current == ')':
                #print('current:', current)
                token = {'Nombre': 'tk_ParentesisC', 'Valor': ')', 'Descripcion': 'Indica el final del espacio para parametros de una funcion o sentencia', 'Linea': num_linea, 'Columna': i+1}
                print(token)
            elif current == ';':
                #print('current:', current)
                token = {'Nombre': 'tk_PuntoYComa', 'Valor': ';', 'Descripcion': 'Finaliza una asignacion o sentencia', 'Linea': num_linea, 'Columna': i+1}
                print(token)
            elif current == ':':
                #print('current:', current)
                token = {'Nombre': 'tk_DosPuntos', 'Valor': ':', 'Descripcion': 'Inicio de procedimientos para casos de switch', 'Linea': num_linea, 'Columna': i+1}
                print(token)
            elif current == '=':
                #print('current:', current)
                token = {'Nombre': 'tk_Igual', 'Valor': '=', 'Descripcion': 'Indica asignacion de un valos', 'Linea': num_linea, 'Columna': i+1}
                print(token)


    num_linea += 1
