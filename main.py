from Memory import *
from CargarArchivo import *
print("comenzando")
ruta = input("Ingrese la ruta del archivo\n")
print(ruta)
cargar = CargarArchivo()
cargar.cargarArchivo(ruta)
print(Memomry.content_script)
startComent = 0
num_linea = 1
columna = 0
cadena = ""
estado = 0
lexemas = []
for linea in Memomry.content_script:
    contTab = 0
    tab = False
    for i in range(len(linea)):
        if linea[i] == '\t':
            tab = True
            contTab += 1
        if tab:
            if contTab > 1:
                columna = i + 4 * contTab - contTab + 1
            else:
                columna = i + 4 * contTab
        else:
            columna = i + 1
        current = linea[i]
        #print(f"col{i}_{linea[i]}")
        if estado == 0:
            if current == ',':
                #print('current:', current)
                token = {'Nombre': 'tk_coma', 'Valor': ',', 'Descripcion': 'Separador de atributos', 'Linea': num_linea, 'Columna': columna}
                print(token)
                lexemas.append(token)
            elif current == '{':
                #print('current:', current)
                token = {'Nombre': 'tk_LlaveA', 'Valor': '{', 'Descripcion': 'Indica el inicio del contenido de una funcion o sentencia', 'Linea': num_linea, 'Columna': columna}
                print(token)
                lexemas.append(token)
            elif current == '}':
                #print('current:', current)
                token = {'Nombre': 'tk_LlaveC', 'Valor': '}', 'Descripcion': 'Indica el final del contenido de una funcion o sentencia', 'Linea': num_linea, 'Columna': columna}
                print(token)
                lexemas.append(token)
            elif current == '(':
                #print('current:', current)
                token = {'Nombre': 'tk_ParentesisA', 'Valor': '(', 'Descripcion': 'Indica el inicio del espacio para parametros de una funcion o sentencia', 'Linea': num_linea, 'Columna': columna}
                print(token)
                lexemas.append(token)
            elif current == ')':
                #print('current:', current)
                token = {'Nombre': 'tk_ParentesisC', 'Valor': ')', 'Descripcion': 'Indica el final del espacio para parametros de una funcion o sentencia', 'Linea': num_linea, 'Columna': columna}
                print(token)
                lexemas.append(token)
            elif current == ';':
                #print('current:', current)
                token = {'Nombre': 'tk_PuntoYComa', 'Valor': ';', 'Descripcion': 'Finaliza una asignacion o sentencia', 'Linea': num_linea, 'Columna': columna}
                print(token)
                lexemas.append(token)
            elif current == ':':
                #print('current:', current)
                token = {'Nombre': 'tk_DosPuntos', 'Valor': ':', 'Descripcion': 'Inicio de procedimientos para casos de switch', 'Linea': num_linea, 'Columna': columna}
                print(token)
                lexemas.append(token)
            elif current == '=' and linea[i+1] != '>':
                #print('current:', current)
                token = {'Nombre': 'tk_Igual', 'Valor': '=', 'Descripcion': 'Indica asignacion de un valos', 'Linea': num_linea, 'Columna': columna}
                print(token)
                lexemas.append(token)
            elif current == '/' and linea[i+1] == '*':
                estado = 1
                cadena += current
                startComent = columna
            elif current.isalpha() or current == '_':
                cadena += current
                estado = 2
        elif estado == 1:
            if current == '/' and linea[i-1] == '*':
                cadena += current
                print('comentario final', cadena)
                token = {'Nombre': 'tk_Comentario', 'Valor': cadena, 'Descripcion': 'Es un comentario', 'Linea': num_linea, 'Columna': startComent}
                print(token)
                estado = 0
                cadena = ''
            else:
                if current != '\n':
                    cadena += current
        elif estado == 2:
            


    num_linea += 1
