from Memory import *
from CargarArchivo import *
from Reporte import *
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
errores = []
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
            elif current == '=':
                if linea[i+1] != '>':
                    token = {'Nombre': 'tk_Igual', 'Valor': '=', 'Descripcion': 'Indica asignacion de un valos', 'Linea': num_linea, 'Columna': columna}
                    print(token)
                    lexemas.append(token)
                else:
                    cadena += current
                    startComent = columna
            elif current == '>' and cadena == '=':
                token = {'Nombre': 'tk_Flecha', 'Valor': '=>', 'Descripcion': 'Flecha para funciones', 'Linea': num_linea, 'Columna': startComent}
                print(token)
                lexemas.append(token)
                cadena = ''
            elif current == '/' and linea[i+1] == '*':
                estado = 1
                cadena += current
                startComent = columna
            elif current.isalpha() or current == '_':
                startComent = columna
                cadena += current
                estado = 2
                #print("volvio a cadena",estado)
            elif current == ' ':
                estado = 0
                #print("vacio")
            elif current == '"':
                estado = 3
                cadena += current
                startComent = columna
            elif current.isdigit():
                cadena = cadena + current
                estado = 4
                startComent = columna
                try:
                    if linea[i+1] != '.' and linea[i+1].isdigit() == False:
                        if linea[i + 1] == '(' or linea[i + 1] == ')' or linea[i + 1] == '{' or linea[i + 1] == '}' or \
                                linea[
                                    i + 1] == ';' or linea[i + 1] == ':' or linea[i + 1] == '=' or linea[i + 1] == ',' or \
                                linea[i + 1] == ' ' or linea[i + 1] == '' or linea[i + 1].isdigit() == False:
                            newToken = {'Nombre': 'tk_Numero', 'Valor': cadena,
                                        'Descripcion': 'Valor numerico', 'Linea': num_linea,
                                        'Columna': startComent}
                            lexemas.append(newToken)
                            estado = 0
                            cadena = ''
                except:
                    print("catch en estado 6")
            else:
                if current != " " and current != "\n" and current != "\t":
                    newError = {'Error': current, 'Linea': num_linea, 'Columna': columna}
                    errores.append(newError)
                    cadena = ''

        elif estado == 1:
            if current == '/' and linea[i-1] == '*':
                cadena += current
                print('comentario final', cadena)
                token = {'Nombre': 'tk_Comentario', 'Valor': cadena, 'Descripcion': 'Es un comentario', 'Linea': num_linea, 'Columna': startComent}
                print(token)
                lexemas.append(token)
                estado = 0
                cadena = ''
            else:
                if current != '\n':
                    cadena += current
        elif estado == 2:
            if current != " ":
                cadena += current
                # for token in Memomry.lista_tk:
                #     if token.get('Valor') == cadena:
                #         newToken = {'Nombre': token.get('Nombre'), 'Valor': token.get('Valor'), 'Descripcion': token.get('Descripcion'), 'Linea': num_linea, 'Columna': startComent}
                #         print("estado 2 vacio", newToken)
                #         lexemas.append(newToken)
                #         cadena = ''
                #         estado = 0
            else:
                flag = True
                for token in Memomry.lista_tk:
                    if token.get('Valor') == cadena:
                        newToken = {'Nombre': token.get('Nombre'), 'Valor': token.get('Valor'), 'Descripcion': token.get('Descripcion'), 'Linea': num_linea, 'Columna': startComent}
                        print(newToken)
                        lexemas.append(newToken)
                        print("estado 2 else vacio", newToken)
                        cadena = ''
                        estado = 0
                        flag = False
#                        print(estado)
                if flag:
                    newToken = {'Nombre': 'tk_Identificador', 'Valor': cadena,
                                'Descripcion': 'Palabra que funciona como identificador', 'Linea': num_linea, 'Columna': startComent}
                    print(newToken)
                    lexemas.append(newToken)
                    print("estado 2 if flag", newToken)
                    cadena = ''
                    estado = 0
            try:
                if linea[i+1] == '(' or linea[i+1] == ')' or linea[i+1] == '{' or linea[i+1] == '}' or linea[i+1] == ';'\
                        or linea[i+1] == ':' or linea[i+1] == '=' or linea[i+1] == ',':
                    if cadena != "":
                        print("cadena", len(cadena))
                        flag = True
                        for token in Memomry.lista_tk:
                            if token.get('Valor') == cadena:
                                newToken = {'Nombre': token.get('Nombre'), 'Valor': token.get('Valor'),
                                            'Descripcion': token.get('Descripcion'), 'Linea': num_linea,
                                            'Columna': startComent}
                                print(newToken)
                                lexemas.append(newToken)
                                cadena = ''
                                estado = 0
                                flag = False
                        #                        print(estado)
                        if flag:
                            newToken = {'Nombre': 'tk_Identificador', 'Valor': cadena,
                                        'Descripcion': 'Palabra que funciona como identificador', 'Linea': num_linea,
                                        'Columna': startComent}
                            print(newToken)
                            lexemas.append(newToken)
                            cadena = ''
                            estado = 0
            except:
                print("no exixte")

        elif estado == 3:
            if current != '"':
                cadena += current
            else:
                cadena += current
                newToken = {'Nombre': 'tk_Cadena', 'Valor': cadena,
                            'Descripcion': 'Cadena de caracteres', 'Linea': num_linea,
                            'Columna': startComent}
                print(newToken)
                lexemas.append(newToken)
                cadena = ''
                estado = 0

        elif estado == 4:
            errorNum = False
            if current.isdigit():
                cadena = cadena + current
            elif current == '.':
                flag2 = 0
                cadena = cadena + current
                estado = 5
                try:
                    if linea[i+1].isdigit() == False:
                        print("no es valido", num_linea)
                        newError = {'Error': cadena, 'Linea': num_linea, 'Columna': columna}
                        errores.append(newError)
                        estado = 0
                        cadena = ''
                        errorNum = True
                except:
                    print("error en estado 4")
            try:
                if linea[i + 1] == '(' or linea[i + 1] == ')' or linea[i + 1] == '{' or linea[i + 1] == '}' or linea[
                    i + 1] == ';' or linea[i + 1] == ':' or linea[i + 1] == '=' or linea[i + 1] == ',' or linea[i+1] == ' ' or linea[i+1] == '':
                    if estado != 5:
                        if errorNum == False:
                            newToken = {'Nombre': 'tk_Numero', 'Valor': cadena,
                                        'Descripcion': 'Valor numerico', 'Linea': num_linea,
                                        'Columna': startComent}
                            lexemas.append(newToken)
                            estado = 0
                            cadena = ''
            except:
                print("no existe sig en estado 4")

        elif estado == 5:
            if current.isdigit():
                cadena = cadena + current
                estado = 6

        elif estado == 6:
            if current.isdigit():
                cadena = cadena + current
            try:
                if linea[i + 1] == '(' or linea[i + 1] == ')' or linea[i + 1] == '{' or linea[i + 1] == '}' or linea[
                    i + 1] == ';' or linea[i + 1] == ':' or linea[i + 1] == '=' or linea[i + 1] == ',' or linea[i+1] == ' ' or linea[i+1] == '' or linea[i+1].isdigit() == False:
                    newToken = {'Nombre': 'tk_Numero', 'Valor': cadena,
                                'Descripcion': 'Valor numerico', 'Linea': num_linea,
                                'Columna': startComent}
                    print(newToken)
                    lexemas.append(newToken)
                    estado = 0
                    cadena = ''
            except:
                print("catch en estado 6")

    num_linea += 1
repo = Reporte()
repo.crearHtml(lexemas, "Tokens_Validos")
repo.crearHtml(errores, "Errores_Encontrados")