from Memory import *
from CargarArchivo import *
from Reporte import *
from Pila import *
from graphviz import Digraph
from tabulate import *


def main():
    opcion = 0
    while(opcion != "5"):
        print("/////////////////////////////////////// MENU ///////////////////////////////////////")
        print("1. Cargar script")
        print("2. Manejo AFD")
        print("3. Pila interactiva")
        print("4. Diagrama")
        print("5. Salir")
        opcion = input("Ingrese la opcion a seleccionar\n")
        if opcion == "1":
            cargarArchivo()
        elif opcion == "2":
            if Memomry.content_script != []:
                Memomry.createReport = True
                manejoAFD()
            else:
                print("ERROR// NO EXISTEN ARCHIVOS CARGADOS")
        elif opcion == "3":
            if Memomry.content_script != []:
                Memomry.createReport = False
                manejoAFD()
                AP()
            else:
                print("ERROR// NO EXISTEN ARCHIVOS CARGADOS")
        elif opcion == "4":
            if Memomry.content_script != []:
                Memomry.createReport = False
                manejoAFD()
                diagrama()
            else:
                print("ERROR// NO EXISTEN ARCHIVOS CARGADOS")
        elif opcion == "5":
            print("Saliendo...")
            exit(0)
        else:
            print("ERROR// OPCION INVALIDA\n")

def cargarArchivo():
    print("////////////////////////////////////////////////////////////////////////////////////")
    ruta = input("Ingrese la ruta del archivo\n")
    #print(ruta)
    cargar = CargarArchivo()
    cargar.cargarArchivo(ruta)
    #print(Memomry.content_script)


def manejoAFD():
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
                    #print(token)
                    lexemas.append(token)
                elif current == '{':
                    #print('current:', current)
                    token = {'Nombre': 'tk_LlaveA', 'Valor': '{', 'Descripcion': 'Indica el inicio del contenido de una funcion o sentencia', 'Linea': num_linea, 'Columna': columna}
                    #print(token)
                    lexemas.append(token)
                elif current == '}':
                    #print('current:', current)
                    token = {'Nombre': 'tk_LlaveC', 'Valor': '}', 'Descripcion': 'Indica el final del contenido de una funcion o sentencia', 'Linea': num_linea, 'Columna': columna}
                    #print(token)
                    lexemas.append(token)
                elif current == '(':
                    #print('current:', current)
                    token = {'Nombre': 'tk_ParentesisA', 'Valor': '(', 'Descripcion': 'Indica el inicio del espacio para parametros de una funcion o sentencia', 'Linea': num_linea, 'Columna': columna}
                    #print(token)
                    lexemas.append(token)
                elif current == ')':
                    #print('current:', current)
                    token = {'Nombre': 'tk_ParentesisC', 'Valor': ')', 'Descripcion': 'Indica el final del espacio para parametros de una funcion o sentencia', 'Linea': num_linea, 'Columna': columna}
                    #print(token)
                    lexemas.append(token)
                elif current == ';':
                    #print('current:', current)
                    token = {'Nombre': 'tk_PuntoYComa', 'Valor': ';', 'Descripcion': 'Finaliza una asignacion o sentencia', 'Linea': num_linea, 'Columna': columna}
                    #print(token)
                    lexemas.append(token)
                elif current == ':':
                    #print('current:', current)
                    token = {'Nombre': 'tk_DosPuntos', 'Valor': ':', 'Descripcion': 'Inicio de procedimientos para casos de switch', 'Linea': num_linea, 'Columna': columna}
                    #print(token)
                    lexemas.append(token)
                elif current == '=':
                    if linea[i+1] != '>':
                        token = {'Nombre': 'tk_Igual', 'Valor': '=', 'Descripcion': 'Indica asignacion de un valos', 'Linea': num_linea, 'Columna': columna}
                        #print(token)
                        lexemas.append(token)
                    else:
                        cadena += current
                        startComent = columna
                elif current == '>' and cadena == '=':
                    token = {'Nombre': 'tk_Flecha', 'Valor': '=>', 'Descripcion': 'Flecha para funciones', 'Linea': num_linea, 'Columna': startComent}
                    #print(token)
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
                                    linea[i + 1] == ';' or linea[i + 1] == ':' or linea[i + 1] == '=' or linea[i + 1] == ',' or \
                                    linea[i + 1] == ' ' or linea[i + 1] == '' or linea[i + 1].isdigit() == False:
                                newToken = {'Nombre': 'tk_Numero', 'Valor': cadena,
                                            'Descripcion': 'Valor numerico', 'Linea': num_linea,
                                            'Columna': startComent}
                                lexemas.append(newToken)
                                estado = 0
                                cadena = ''
                    except:
                        print("Error con los numeros")
                else:
                    if current != " " and current != "\n" and current != "\t":
                        newError = {'Error': current, 'Linea': num_linea, 'Columna': columna}
                        errores.append(newError)
                        cadena = ''

            elif estado == 1:
                if current == '/' and linea[i-1] == '*':
                    cadena += current
                    #print('comentario final', cadena)
                    token = {'Nombre': 'tk_Comentario', 'Valor': cadena, 'Descripcion': 'Es un comentario', 'Linea': num_linea, 'Columna': startComent}
                    #print(token)
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
                            #print(newToken)
                            lexemas.append(newToken)
                            #print("estado 2 else vacio", newToken)
                            cadena = ''
                            estado = 0
                            flag = False
    #                        print(estado)
                    if flag:
                        newToken = {'Nombre': 'tk_Identificador', 'Valor': cadena,
                                    'Descripcion': 'Palabra que funciona como identificador', 'Linea': num_linea, 'Columna': startComent}
                        #print(newToken)
                        lexemas.append(newToken)
                        #print("estado 2 if flag", newToken)
                        cadena = ''
                        estado = 0
                try:
                    if linea[i+1] == '(' or linea[i+1] == ')' or linea[i+1] == '{' or linea[i+1] == '}' or linea[i+1] == ';'\
                            or linea[i+1] == ':' or linea[i+1] == '=' or linea[i+1] == ',':
                        if cadena != "":
                            #print("cadena", len(cadena))
                            flag = True
                            for token in Memomry.lista_tk:
                                if token.get('Valor') == cadena:
                                    newToken = {'Nombre': token.get('Nombre'), 'Valor': token.get('Valor'),
                                                'Descripcion': token.get('Descripcion'), 'Linea': num_linea,
                                                'Columna': startComent}
                                    #print(newToken)
                                    lexemas.append(newToken)
                                    cadena = ''
                                    estado = 0
                                    flag = False
                            #                        print(estado)
                            if flag:
                                newToken = {'Nombre': 'tk_Identificador', 'Valor': cadena,
                                            'Descripcion': 'Palabra que funciona como identificador', 'Linea': num_linea,
                                            'Columna': startComent}
                                #print(newToken)
                                lexemas.append(newToken)
                                cadena = ''
                                estado = 0
                except:
                    print("no exixte", current + " --" + cadena)
                    print("numlin", num_linea)
                    newError = {'Error': cadena, 'Linea': num_linea, 'Columna': columna}
                    errores.append(newError)
                    cadena = ''
                    estado = 0
                    ff = 0
            elif estado == 3:
                if current != '"':
                    cadena += current
                else:
                    cadena += current
                    newToken = {'Nombre': 'tk_Cadena', 'Valor': cadena,
                                'Descripcion': 'Cadena de caracteres', 'Linea': num_linea,
                                'Columna': startComent}
                    #print(newToken)
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
                            #print("no es valido", num_linea)
                            newError = {'Error': cadena, 'Linea': num_linea, 'Columna': columna}
                            errores.append(newError)
                            estado = 0
                            cadena = ''
                            errorNum = True
                    except:
                        print("error en estado 4")
                try:
                    if linea[i + 1] == '(' or linea[i + 1] == ')' or linea[i + 1] == '{' or linea[i + 1] == '}' or linea[
                        i + 1] == ';' or linea[i + 1] == ':' or linea[i + 1] == '=' or linea[i + 1] == ',' or linea[i+1] == ' ' or linea[i+1] == '' or linea[i+1].isalpha() == True or linea[i+1] == '_':
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
                try:
                    if linea[i + 1] == '(' or linea[i + 1] == ')' or linea[i + 1] == '{' or linea[i + 1] == '}' or \
                            linea[
                                i + 1] == ';' or linea[i + 1] == ':' or linea[i + 1] == '=' or linea[i + 1] == ',' or \
                            linea[i + 1] == ' ' or linea[i + 1] == '' or linea[i + 1].isdigit() == False or linea[
                        i + 1] == '_':
                        newToken = {'Nombre': 'tk_Numero', 'Valor': cadena,
                                    'Descripcion': 'Valor numerico', 'Linea': num_linea,
                                    'Columna': startComent}
                        #print(newToken)
                        lexemas.append(newToken)
                        estado = 0
                        cadena = ''
                except:
                    print("catch en estado 6")

            elif estado == 6:
                if current.isdigit():
                    cadena = cadena + current
                try:
                    if linea[i + 1] == '(' or linea[i + 1] == ')' or linea[i + 1] == '{' or linea[i + 1] == '}' or linea[
                        i + 1] == ';' or linea[i + 1] == ':' or linea[i + 1] == '=' or linea[i + 1] == ',' or linea[i+1] == ' ' or linea[i+1] == '' or linea[i+1].isdigit() == False or linea[i+1] == '_':
                        newToken = {'Nombre': 'tk_Numero', 'Valor': cadena,
                                    'Descripcion': 'Valor numerico', 'Linea': num_linea,
                                    'Columna': startComent}
                        #print(newToken)
                        lexemas.append(newToken)
                        estado = 0
                        cadena = ''
                except:
                    print("catch en estado 6")

        num_linea += 1

    repo = Reporte()
    repo.crearHtml(lexemas, "Tokens_Validos")
    repo.crearHtml(errores, "Errores_Encontrados")
    Memomry.lexemas = lexemas
    #print(Memomry.lexemas)


def AP():
    print("///////////////////////// AP /////////////////////////////////")
    listToken = Memomry.lexemas
    tranciociones = Memomry.transitions
    terminales = Memomry.terminales
    noTerminales = Memomry.noTerminales
    pila = Pila()
    estado = 0
    Memomry.reporteEntrada = listToken

    primeraTrancicion()
    if estado == 0:
        for trancicion in tranciociones:
            if trancicion["first"]["estado"] == 0:
                mostrarTrancicion(pila, trancicion["string"])
                pila.push(trancicion["last"]["insertoPila"])
                estado = trancicion["last"]["estadoFinal"]
                input()
    if estado == 1:
        for trancicion in tranciociones:
            if trancicion["first"]["estado"] == 1:
                mostrarTrancicion(pila, trancicion["string"])
                pila.push(trancicion["last"]["insertoPila"])
                #mostrarTrancicion(pila, trancicion["string"])
                input()

    condi = True

    while condi:
        if len(listToken) > 0:
            if listToken[0]["Nombre"] == "tk_Comentario":
                del listToken[0]

        if len(listToken) == 0:

            if pila.obtenerUltimoAgregado() == "#":
                #print(f"{pila.getItems()} ----Entrada valida----")
                mostrarTrancicion(pila, "2, epsilon, # ; 3 , epsilon")
                print("---------------- ENTRADA VALIDA ----------------")
                input()
                rep = Reporte()
                Memomry.createReport = True
                rep.crearHtml(Memomry.reporteAP, "ReporteAutomataPila")
            elif pila.obtenerUltimoAgregado() == "S":
                quitNT(pila, pila.obtenerUltimoAgregado(), "epsilon", listToken)
                continue
            else:
                print("----Entrada invalida")
                condi = False
            break

        temp = pila.obtenerUltimoAgregado()
        #print("temp", temp) aca se imprime el ultimo agregado
        #print("tk", listToken[0]["Nombre"]) imprime el token que se evalua
        if temp in noTerminales:
            quitNT(pila, temp, listToken[0], listToken)
        elif temp == listToken[0]["Nombre"]:
            quitTerminal(pila, listToken)


def quitTerminal(pila, listTk):
    for tr in Memomry.transitions:
        if tr["first"]["entrada"] == tr["first"]["cimaPila"] == listTk[0]["Nombre"]:
            mostrarTrancicion(pila, tr["string"])
            pila.pop()
            del listTk[0]
            #print(pila.getItems()) imprime el estado de la pila despues de una trancicion
            input()
            break

def quitNT(pila, noTerminal, entrada, listaToknes):
    for q in Memomry.transitions:
        if q["first"]["cimaPila"] == noTerminal:
            if noTerminal == "S":
                if entrada != "epsilon":
                    if entrada["Nombre"] == "tk_let" or entrada["Nombre"] == "tk_var" or entrada["Nombre"] == "tk_const":
                        if listaToknes[3]["Nombre"] != "tk_ParentesisA":
                            if type(q["last"]["insertoPila"]) == list: #puedo colocar else para la declaracion de funcion
                                if q["last"]["insertoPila"][0] == "DECLARACION_VARIABLE":
                                    mostrarTrancicion(pila, q["string"])
                                    pila.pop()
                                    pila.extend(q["last"]["insertoPila"])
                                    pila.getItems()
                                    input()
                                    break
                        else:
                            if q["last"]["insertoPila"][0] == "DEF_FUNCION":
                                cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                                break
                    elif entrada["Nombre"] == "tk_if":
                        if type(q["last"]["insertoPila"]) == list:
                            if q["last"]["insertoPila"][0] == "SENTENCIA_IF" and q["first"]["cimaPila"] == "S":
                                mostrarTrancicion(pila, q["string"])
                                pila.pop()
                                pila.extend(q["last"]["insertoPila"])
                                pila.getItems()
                                input()
                                break
                    elif entrada["Nombre"] == "tk_while":
                        if q["last"]["insertoPila"][0] == "SENTENCIA_WHILE" and q["first"]["cimaPila"] == "S":
                            cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                            break
                    elif entrada["Nombre"] == "tk_foreach":
                        if q["last"]["insertoPila"][0] == "SENTENCIA_FOREACH" and q["first"]["cimaPila"] == "S":
                            cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                            break
                    elif entrada["Nombre"] == "tk_Switch":
                        if q["last"]["insertoPila"][0] == "SENTENCIA_SWITCH" and q["first"]["cimaPila"] == "S":
                            cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                            break
                    elif entrada["Nombre"] == "tk_Identificador" and listaToknes[1]["Nombre"] == "tk_ParentesisA":
                        if q["last"]["insertoPila"][0] == "LLAMADA_FUNCION" and q["first"]["cimaPila"] == "S":
                            cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                            break

                else:
                    if q["last"]["insertoPila"] == entrada:
                        #print("entro al else")
                        mostrarTrancicion(pila, q["string"])
                        pila.pop()
                        input()
                        break
            elif noTerminal == "DECLARACION_VARIABLE":
                if q["first"]["cimaPila"] == noTerminal:
                    mostrarTrancicion(pila, q["string"])
                    pila.pop()
                    pila.extend(q["last"]["insertoPila"])
                    #print(pila.getItems()) imprime el estado de la pila despues de una trancicion
                    input()
                    break
            elif noTerminal == "TIPO_VARIABLE":
                if q["last"]["insertoPila"] == entrada["Nombre"]:
                    mostrarTrancicion(pila, q["string"])
                    pila.pop()
                    pila.push(q["last"]["insertoPila"])
                    #print(pila.getItems()) imprime el estadod e la pila despues de una trancicion
                    input()
                    break
            elif noTerminal == "VALOR":
                if entrada["Nombre"] != "tk_true" and entrada["Nombre"] != "tk_false":
                    if q["last"]["insertoPila"] == entrada["Nombre"]:
                        mostrarTrancicion(pila, q["string"])
                        pila.pop()
                        pila.push(q["last"]["insertoPila"])
                        #print(pila.getItems()) estado de la pila
                        input()
                        break
                else:
                    if q["last"]["insertoPila"] == "BOOLEANO":
                        cambioNT(pila, q["string"], q["last"]["insertoPila"], "P" )
                        break

            elif noTerminal == "SENTENCIA_IF":
                if q["first"]["cimaPila"] == noTerminal:
                    cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                    break
            elif noTerminal == "BOOLEANO":
                if q["last"]["insertoPila"] == entrada["Nombre"]:
                    cambioNT(pila, q["string"], q["last"]["insertoPila"], "P")
                    break
            elif noTerminal == "CONDICION":
                if entrada["Nombre"] == "tk_Identificador":
                    if q["last"]["insertoPila"] == entrada["Nombre"]:
                        cambioNT(pila, q["string"], q["last"]["insertoPila"], "P")
                        break
                else:
                    if q["first"]["cimaPila"] == noTerminal and q["last"]["insertoPila"] == "BOOLEANO":
                        cambioNT(pila, q["string"], q["last"]["insertoPila"], "P")
                        break
            elif noTerminal == "CONTENIDO":
                if entrada["Nombre"] == "tk_LlaveC" or entrada["Nombre"] == "tk_Break" or entrada["Nombre"] == "tk_Case" or entrada["Nombre"] == "tk_Default":
                    if q["first"]["cimaPila"] == "CONTENIDO" and q["last"]["insertoPila"] == "epsilon":
                        mostrarTrancicion(pila, q["string"])
                        pila.pop()
                        #print(pila.getItems()) estado de la pila
                        input()
                        break
                if entrada["Nombre"] == "tk_let" or entrada["Nombre"] == "tk_var" or entrada["Nombre"] == "tk_const":
                    if listaToknes[3]["Nombre"] != "tk_ParentesisA":
                        if type(q["last"]["insertoPila"]) == list:
                            if q["last"]["insertoPila"][0] == "DECLARACION_VARIABLE":
                                cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                                break
                    else:
                        if q["last"]["insertoPila"][0] == "DEF_FUNCION":
                            cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                            break
                elif entrada["Nombre"] == "tk_if":
                    if q["first"]["cimaPila"] == "CONTENIDO" and q["last"]["insertoPila"][0] == "SENTENCIA_IF":
                        cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                        break
                elif entrada["Nombre"] == "tk_while":
                    if q["last"]["insertoPila"][0] == "SENTENCIA_WHILE" and q["first"]["cimaPila"] == "CONTENIDO":
                        cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                        break
                elif entrada["Nombre"] == "tk_foreach":
                    if q["last"]["insertoPila"][0] == "SENTENCIA_FOREACH" and q["first"]["cimaPila"] == "CONTENIDO":
                        cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                        break
                elif entrada["Nombre"] == "tk_Switch":
                    if q["last"]["insertoPila"][0] == "SENTENCIA_SWITCH" and q["first"]["cimaPila"] == "CONTENIDO":
                        cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                        break
                elif entrada["Nombre"] == "tk_Identificador" and listaToknes[1]["Nombre"] == "tk_ParentesisA":
                    if q["last"]["insertoPila"][0] == "LLAMADA_FUNCION" and q["first"]["cimaPila"] == "CONTENIDO":
                        cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                        break



            elif noTerminal == "SENTENCIA_WHILE":
                if q["first"]["cimaPila"] == noTerminal:
                    cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                    break
            elif noTerminal == "SENTENCIA_FOREACH":
                if q["first"]["cimaPila"] == noTerminal:
                    cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                    break
            elif noTerminal == "SENTENCIA_SWITCH":
                if q["first"]["cimaPila"] == noTerminal:
                    cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                    break
            elif noTerminal == "CASES":
                if entrada["Nombre"] == "tk_LlaveC":
                    if q["first"]["cimaPila"] == "CASES" and q["last"]["insertoPila"] == "epsilon":
                        mostrarTrancicion(pila, q["string"])
                        pila.pop()
                        input()
                        break
                elif entrada["Nombre"] == "tk_Case":
                    if q["first"]["cimaPila"] == "CASES" and q["last"]["insertoPila"][0] == "CASE":
                        cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                        break
                elif entrada["Nombre"] == "tk_Default":
                    if q["last"]["insertoPila"] == "DEFAULT":
                        cambioNT(pila, q["string"], q["last"]["insertoPila"], "P")
                        break
            elif noTerminal == "CASE":
                if q["first"]["cimaPila"] == "CASE":
                    cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                    break
            elif noTerminal == "DEF_FUNCION":
                if q["first"]["cimaPila"] == noTerminal:
                    cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                    break
            elif noTerminal == "PARAMETROS":
                if entrada["Nombre"] != "tk_ParentesisC":
                    if q["first"]["cimaPila"] == noTerminal:
                        cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                        break
                else:
                    if q["first"]["cimaPila"] == noTerminal and q["last"]["insertoPila"] == "epsilon":
                        mostrarTrancicion(pila, q["string"])
                        pila.pop()
                        #print(pila.getItems()) estado de la pila
                        input()
                        break
            elif noTerminal == "PARAMETRO":
                if listaToknes[1]["Nombre"] == "tk_ParentesisC":
                    if q["first"]["cimaPila"] == noTerminal and q["last"]["insertoPila"] == "tk_Identificador":
                        cambioNT(pila, q["string"], q["last"]["insertoPila"], "P")
                        break
                if listaToknes[1]["Nombre"] == "tk_coma":
                    if q["first"]["cimaPila"] == noTerminal and type(q["last"]["insertoPila"]) == list:
                        cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                        break
            elif noTerminal == "LLAMADA_FUNCION":
                if q["first"]["cimaPila"] == noTerminal and type(q["last"]["insertoPila"]) == list:
                    cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                    break
            elif noTerminal == "PARAMETROS2":
                if entrada["Nombre"] == "tk_ParentesisC":
                    if q["first"]["cimaPila"] == noTerminal and q["last"]["insertoPila"] == "epsilon":
                        mostrarTrancicion(pila, q["string"])
                        pila.pop()
                        input()
                        break
                else:
                    if q["first"]["cimaPila"] == noTerminal and type(q["last"]["insertoPila"]) == list and entrada["Nombre"] != "tk_coma":
                        if entrada["Nombre"] == "tk_Identificador":
                            if q["last"]["insertoPila"][0] == "tk_Identificador":
                                cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                                break
                        else:
                            if q["last"]["insertoPila"][0] == "VALOR":
                                cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                                break
                    else:
                        if q["first"]["cimaPila"] == "PARAMETROS2" and q["last"]["insertoPila"][0] == "tk_coma":
                            cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                            break
            elif noTerminal == "POSIBLE_BREAK":
                if entrada["Nombre"] == "tk_Break":
                    if q["first"]["cimaPila"] == "POSIBLE_BREAK" and type(q["last"]["insertoPila"]) == list:
                        cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                        break
                else:
                    if q["first"]["cimaPila"] == "POSIBLE_BREAK" and q["last"]["insertoPila"] == "epsilon":
                        mostrarTrancicion(pila, q["string"])
                        pila.pop()
                        input()
                        break
            elif noTerminal == "DEFAULT":
                if q["first"]["cimaPila"] == noTerminal:
                    cambioNT(pila, q["string"], q["last"]["insertoPila"], "L")
                    break



def cambioNT(pila, cadenaTrans, cont, addListOrWord):
    if addListOrWord == "L":
        mostrarTrancicion(pila, cadenaTrans)
        pila.pop()
        pila.extend(cont)
        #print(pila.getItems()) estado de la pila
        input()
    elif addListOrWord == "P":
        mostrarTrancicion(pila, cadenaTrans)
        pila.pop()
        pila.push(cont)
        #print(pila.getItems()) estado de la pila
        input()

def mostrarTrancicion(pila, trancicion):
    #print(f"{pila.getItems()} ----- {trancicion}")
    cadEntrada = ""
    cadPL = []
    for tk in Memomry.reporteEntrada:
        cadEntrada += tk["Nombre"] + " , "
    cadPL = pila.getItems()
    #print(pila.getItems())

    dic = {"1": [pila.getPilaReporte()], "2": [cadEntrada], "3": [trancicion]}
    dic2 = {"PILA": [pila.getPilaReporte()], "ENTRADA": [cadEntrada], "TRANCICION": [trancicion]}
    print(tabulate(dic, tablefmt='fancy_grid'))
    Memomry.reporteAP.append(dic2)


def primeraTrancicion():
    dic = {"1": [".      PILA        ."], "2": [".     ENTRADA     ."], "3": [".     TRANCICION      ."]}
    print(tabulate(dic, tablefmt='fancy_grid'))
    #Memomry.reporteAP.append(dic)

def diagrama():
    print("CREANDO DIAGRAMA...\n")
    padres = Pila()
    contId = 0
    nodos = []
    temp = Memomry.lexemas
    nivel = 1
    listNivel = []
    parametros = False
    parametrosLlamada = False
    listParametros = []
    listParametrosLlamada = []
    foreachON = False
    ifOn = False
    whileOn = False
    switchOn = False
    contCase = 1
    saveNivSwitch = 0
    for i in range(len(temp)):
        if temp[i]["Nombre"] == 'tk_const' or temp[i]["Nombre"] == 'tk_var' or temp[i]["Nombre"] == 'tk_let':
            if temp[i+3]["Nombre"] == 'tk_ParentesisA':
                #print("decl funcion", temp[i]["Linea"])
                contId += 1
                valor = temp[i + 1]["Valor"]
                nodo = {}
                nodo["Nivel"] = nivel
                nodo["Contenido"] = f"Definicion: {valor}"
                nodo["Clave"] = str(contId)
                if nivel > 1:
                    nodo["Padre"] = nodos[len(nodos) - 1]["Clave"]
                nodos.append(nodo)
                nivel += 1
                sumNivel(nivel, listNivel)
                parametros = True
            else:
                contId += 1
                #print("variable", temp[i]["Linea"])
                valor = temp[i+1]["Valor"]
                nodo = {}
                nodo["Nivel"] = nivel
                nodo["Contenido"] = f"Asignacion: {valor}"
                nodo["Clave"] = str(contId)
                if nivel > 1:
                    nodo["Padre"] = nodos[len(nodos) - 1]["Clave"]
                nodos.append(nodo)
        elif temp[i]["Nombre"] == 'tk_if':
            #print("nivel if", nivel)
            contId += 1
            nodo = {}
            nodo["Nivel"] = nivel
            nodo["Contenido"] = f"Sentencia if"
            nodo["Clave"] = str(contId)
            if nivel > 1:
                nodo["Padre"] = nodos[len(nodos) - 1]["Clave"]
            nodos.append(nodo)
            nivel += 1
            sumNivel(nivel, listNivel)
            ifOn = True
        elif temp[i]["Nombre"] == 'tk_while':
            #print("nivel while",nivel)
            contId += 1
            nodo = {}
            nodo["Nivel"] = nivel
            nodo["Contenido"] = f"Sentencia while"
            nodo["Clave"] = str(contId)
            if nivel > 1:
                nodo["Padre"] = nodos[len(nodos) - 1]["Clave"]
            nodos.append(nodo)
            nivel += 1
            sumNivel(nivel, listNivel)
            #print("nivel final while", nivel)
            whileOn = True
        elif temp[i]["Nombre"] == 'tk_foreach':
            contId += 1
            nodo = {}
            nodo["Nivel"] = nivel
            nodo["Contenido"] = f"Sentencia foreach"
            nodo["Clave"] = str(contId)
            if nivel > 1:
                nodo["Padre"] = nodos[len(nodos) - 1]["Clave"]
            nodos.append(nodo)
            nivel += 1
            sumNivel(nivel, listNivel)
            foreachON = True
        elif temp[i]["Nombre"] == 'tk_Switch':
            saveNivSwitch = nivel
            contId += 1
            nodo = {}
            nodo["Nivel"] = nivel
            nodo["Contenido"] = f"Sentencia switch"
            nodo["Clave"] = str(contId)
            if nivel > 1:
                nodo["Padre"] = nodos[len(nodos) - 1]["Clave"]
            nodos.append(nodo)
            nivel += 1
            sumNivel(nivel, listNivel)
            switchOn = True
        elif temp[i]["Nombre"] == "tk_Identificador":
            if temp[i + 1]["Nombre"] == 'tk_ParentesisA' and parametros == False:
                contId += 1
                nodo = {}
                nodo["Nivel"] = nivel
                nodo["Contenido"] = f"Llamada {temp[i]['Valor']}"
                nodo["Clave"] = str(contId)
                if nivel > 1:
                    nodo["Padre"] = nodos[len(nodos) - 1]["Clave"]
                nodos.append(nodo)
                nivel += 1
                sumNivel(nivel, listNivel)
                parametros = True
                parametrosLlamada = True
            elif temp[i - 1]["Nombre"] == "tk_ParentesisA" and temp[i + 1]["Nombre"] == "tk_ParentesisC" and parametros == False and parametrosLlamada == False:
                contId += 1
                nodo = {}
                nodo["Nivel"] = nivel
                nodo["Contenido"] = f"Condicion: {temp[i]['Valor']}"
                nodo["Clave"] = str(contId)
                nodo["Padre"] = nodos[len(nodos)-1]["Clave"]
                nodos.append(nodo)
                ifOn = False #quitar si arruina toodo
                whileOn = False
            elif parametros == True or parametrosLlamada == True:
                listParametros.append(temp[i]["Valor"])

        elif temp[i]["Nombre"] == "tk_LlaveC":
            nivel = nivel - 1
            if switchOn:
                #print("nivel en switch: ", nivel)
                nivel = saveNivSwitch
                switchOn = False

        elif temp[i]["Nombre"] == "tk_PuntoYComa" and parametrosLlamada == True:
            nivel = nivel - 1
            parametrosLlamada = False
        elif temp[i]["Nombre"] == "tk_ParentesisC":
            if parametros:
                if parametrosLlamada:
                    listParametros = listParametros
                else:
                    listParametros.pop(0)
                parametrosStr = ""
                for j in range(len(listParametros)):
                    if j <= len(listParametros) - 2:
                        parametrosStr += listParametros[j] + ", "
                    else:
                        parametrosStr += listParametros[j]
                contId += 1
                nodo = {}
                nodo["Nivel"] = nivel
                nodo["Contenido"] = f"Parametros: {parametrosStr}"
                nodo["Clave"] = str(contId)
                nodo["Padre"] = nodos[len(nodos) - 1]["Clave"]
                nodos.append(nodo)
                parametros = False
                listParametros = []
                #parametrosLlamada = False
            elif foreachON:
                contId += 1
                nodo = {}
                nodo["Nivel"] = nivel
                nodo["Contenido"] = f"{temp[i - 3]['Valor']} in {temp[i - 1]['Valor']}"
                nodo["Clave"] = str(contId)
                nodo["Padre"] = nodos[len(nodos) - 1]["Clave"]
                nodos.append(nodo)
                foreachON = False

        elif temp[i]["Nombre"] == "tk_true" or temp[i]["Nombre"] == "tk_false":
            if ifOn == True and parametrosLlamada == False:
                contId += 1
                nodo = {}
                nodo["Nivel"] = nivel
                nodo["Contenido"] = f"Condicion: {temp[i]['Valor']}"
                nodo["Clave"] = str(contId)
                nodo["Padre"] = nodos[len(nodos) - 1]["Clave"]
                nodos.append(nodo)
                ifOn = False
            elif whileOn == True:
                contId += 1
                nodo = {}
                nodo["Nivel"] = nivel
                nodo["Contenido"] = f"Condicion: {temp[i]['Valor']}"
                nodo["Clave"] = str(contId)
                nodo["Padre"] = nodos[len(nodos) - 1]["Clave"]
                nodos.append(nodo)
                whileOn = False
            elif parametrosLlamada or parametros:
                listParametros.append(temp[i]["Valor"])
        elif temp[i]["Nombre"] == "tk_Numero":
            if parametrosLlamada or parametros:
                listParametros.append(temp[i]["Valor"])
        elif temp[i]["Nombre"] == "tk_Cadena":
            if parametrosLlamada or parametros:
                    if temp[i - 1]["Nombre"] != "tk_Case":
                        listParametros.append(temp[i]["Valor"])
                        #print("Entro a la caadena, ", contId)
        elif temp[i]["Nombre"] == "tk_Case":
            nivel += 1
            sumNivel(nivel, listNivel)
            contId += 1
            nodo = {}
            nodo["Nivel"] = nivel
            nodo["Contenido"] = f"Case {temp[i+1]['Valor']}"
            nodo["Clave"] = str(contId)
            nodo["Padre"] = nodos[len(nodos) - 1]["Clave"]
            nodos.append(nodo)
            #print("nivel case", nivel)
            contCase += 1
        elif temp[i]["Nombre"] == "tk_Default":
            nivel += 1
            sumNivel(nivel, listNivel)
            contId += 1
            nodo = {}
            nodo["Nivel"] = nivel
            nodo["Contenido"] = f"Default"
            nodo["Clave"] = str(contId)
            nodo["Padre"] = nodos[len(nodos) - 1]["Clave"]
            nodos.append(nodo)
        else:
            v = 0

    #print("nodos",nodo)
    dot = Digraph(filename="Prueba", format='png')
    dot.attr('node', shape='box', width='1.5', height='1.5')

    temp = []
    for nd in nodos:
        if nd["Nivel"] == 1:
            temp.append(nd)

    for i in range(len(temp)):
        with dot.subgraph() as niv:
            niv.attr(rank='same')
            niv.node(temp[i]["Clave"], temp[i]["Contenido"])
            #print("nivel", temp[i]["Nivel"])
            if i >= 0 and i <= len(temp) - 2:
                niv.edge(str(temp[i]["Clave"]), str(temp[i+1]["Clave"]))

    for numero in listNivel:
        for i in range(len(nodos)):
            if nodos[i]["Nivel"] == numero and numero != 1:
                #print("numerooo",numero)
                with dot.subgraph() as niv2:
                    niv2.attr(rank=f'{numero}')
                    niv2.node(nodos[i]["Clave"], nodos[i]["Contenido"])
                    try:
                        niv2.edge(nodos[i]["Padre"], nodos[i]["Clave"])
                    except:
                        v = 0
                    #print("nivel", nodos[i]["Nivel"])

    #print(dot.source)
    dot.render("Reportes/Prueba", view=True)

    # with dot.subgraph() as s:
    #     s.attr(rank='same')
    #     s.node("A", "King Arthur")
    #     s.node("B","Sir Bedever")
    #     s.node("C","Sir Lancelot")
    #
    # #dot.edges(["AB","AC"])
    # dot.edge('A', 'B')
    # dot.edge('B', 'C', constraint='true')
    #
    # for lx in Memomry.lexemas:
    #     dot.node(lx["Nombre"])
    # print(dot.source)
    # dot.render("Reportes/Prueba", view=True)

def sumNivel(num, list):
    if num not in list:
        list.append(num)


if __name__ == '__main__':
    main()
    # carg = CargarArchivo()
    # carg.cargarArchivo("entrada4.js")
    # AP()