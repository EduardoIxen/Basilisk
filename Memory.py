class Memomry:
    createReport = False
    content_script = []
    lexemas = []
    lista_tk = [
        {
            'Nombre': 'tk_let',
            'Valor': 'let',
            'Descripcion': 'Palabra reservada para declarar una variable'
        },
        {
            'Nombre': 'tk_var',
            'Valor': 'var',
            'Descripcion': 'Palabra reservada para declarar una variable'
        },
        {
            'Nombre': 'tk_const',
            'Valor': 'const',
            'Descripcion': 'Palabra reservada para declarar una variable'
        },
        {
            'Nombre': 'tk_true',
            'Valor': 'true',
            'Descripcion': 'Booleano verdadero'
        },
        {
            'Nombre': 'tk_false',
            'Valor': 'false',
            'Descripcion': 'Booleano falso'
        },
        {
            'Nombre': 'tk_if',
            'Valor': 'if',
            'Descripcion': 'Sentencia de control if'
        },
        {
            'Nombre': 'tk_while',
            'Valor': 'while',
            'Descripcion': 'Sentencia de ciclo con condicion'
        },
        {
            'Nombre': 'tk_foreach',
            'Valor': 'foreach',
            'Descripcion': 'Sentencia de ciclo repetitivo'
        },
        {
            'Nombre': 'tk_in',
            'Valor': 'in',
            'Descripcion': 'Palabra reservada para condiciones de foreach'
        },
        {
            'Nombre': 'tk_PrarentesisA',
            'Valor': '(',
            'Descripcion': 'Indica el inicio del espacio para parametros de una funcion o sentencia'
        },
        {
            'Nombre': 'tk_PrarentesisC',
            'Valor': ')',
            'Descripcion': 'Indica el final del espacio para parametros de una funcion o sentencia'
        },
        {
            'Nombre': 'tk_Case',
            'Valor': 'case',
            'Descripcion': 'Casos diferentes para switch'
        },
        {
            'Nombre': 'tk_Switch',
            'Valor': 'switch',
            'Descripcion': 'Sentencia para evaluar casos diferentes'
        },
        {
            'Nombre': 'tk_Break',
            'Valor': 'break',
            'Descripcion': 'Indica el final de un caso de switch'
        },
        {
            'Nombre': 'tk_Default',
            'Valor': 'default',
            'Descripcion': 'Operacion por defecto para un switch'
        }
                ]
    transitions = [
        {
            "first": {
                "estado": 0,
                "entrada": "epsilon",
                "cimaPila": "epsilon"
            },
            "last": {
                "estadoFinal": 1,
                "insertoPila": "#"
            },

            "string": "0,epsilon,epsilon;1,#"
        },
        {
            "first": {
                "estado": 1,
                "entrada": "epsilon",
                "cimaPila": "epsilon"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "S"
            },

            "string": "1,epsilon,epsilon;2,S"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "S"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["DECLARACION_VARIABLE", "S"]
            },

            "string": "2,epsilon,S;2, [DECLARACION_VARIABLE, S]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "S"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["SENTENCIA_IF", "S"]
            },

            "string": "2,epsilon,S;2, [SENTENCIA_IF, S]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "S"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["SENTENCIA_WHILE", "S"]
            },

            "string": "2,epsilon,S;2, [SENTENCIA_WHILE, S]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "S"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["SENTENCIA_FOREACH", "S"]
            },

            "string": "2,epsilon,S;2, [SENTENCIA_FOREACH, S]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "S"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["SENTENCIA_SWITCH", "S"]
            },

            "string": "2,epsilon,S;2, [SENTENCIA_SWITCH, S]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "S"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["DEF_FUNCION", "S"]
            },

            "string": "2,epsilon,S;2, [DEF_FUNCION, S]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "S"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["LLAMADA_FUNCION", "S"]
            },

            "string": "2,epsilon,S;2, [LLAMADA_FUNCION, S]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "S"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,epsilon,S;2,epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "CONTENIDO"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["DECLARACION_VARIABLE", "CONTENIDO"]
            },

            "string": "2,epsilon,CONTENIDO; 2, [DECLARACION_VARIABLE, CONTENIDO]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "CONTENIDO"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["SENTENCIA_IF", "CONTENIDO"]
            },

            "string": "2,epsilon,CONTENIDO; 2, [SENTENCIA_IF, CONTENIDO]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "CONTENIDO"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["SENTENCIA_WHILE", "CONTENIDO"]
            },

            "string": "2,epsilon,CONTENIDO; 2, [SENTENCIA_WHILE, CONTENIDO]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "CONTENIDO"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["SENTENCIA_FOREACH", "CONTENIDO"]
            },

            "string": "2,epsilon,CONTENIDO; 2, [SENTENCIA_FOREACH, CONTENIDO]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "CONTENIDO"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["SENTENCIA_SWITCH", "CONTENIDO"]
            },

            "string": "2,epsilon,CONTENIDO; 2, [SENTENCIA_SWITCH, CONTENIDO]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "CONTENIDO"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["DEF_FUNCION", "CONTENIDO"]
            },

            "string": "2,epsilon,CONTENIDO; 2, [DEF_FUNCION, CONTENIDO]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "CONTENIDO"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["LLAMADA_FUNCION", "CONTENIDO"]
            },

            "string": "2,epsilon,CONTENIDO; 2, [LLAMADA_FUNCION, CONTENIDO]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "CONTENIDO"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2, epsilon, CONTENIDO; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "TIPO_VARIABLE"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_const"
            },

            "string": "2,epsilon,TIPO_VARIABLE;2,tk_const"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "TIPO_VARIABLE"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_var"
            },

            "string": "2, epsilon, TIPO_VARIABLE ; 2, tk_var"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "TIPO_VARIABLE"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_let"
            },

            "string": "2, epsilon, TIPO_VARIABLE; 2, tk_let"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "VALOR"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_Numero"
            },

            "string": "2, epsilon, VALOR; 2, tk_Numero"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "VALOR"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_Cadena"
            },

            "string": "2, epsilon, VALOR; 2, tk_Cadena"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "VALOR"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "BOOLEANO"
            },

            "string": "2, epsilon, valor; 2, BOOLEANO"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "BOOLEANO"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_true"
            },

            "string": "2, epsilon, BOOLEANO; 2, tk_true"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "BOOLEANO"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_false"
            },

            "string": "2, epsilon, BOOLEANO; 2, tk_false"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "CONDICION"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "BOOLEANO"
            },

            "string": "2, epsilon, CONDICION; 2, BOOLEANO"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "CONDICION"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_Identificador"
            },

            "string": "2, epsilon, CONDICION; 2, tk_Identificador"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "DECLARACION_VARIABLE"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["TIPO_VARIABLE", "tk_Identificador", "tk_Igual", "VALOR", "tk_PuntoYComa"]
            },

            "string": "2,epsilon,DECLARACION_VARIABLE;  [2, TIPO_VARIABLE, tk_Identificador, tk_Igual, VALOR, tk_PuntoYComa]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "SENTENCIA_IF"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["tk_if", "tk_ParentesisA", "CONDICION", "tk_ParentesisC", "tk_LlaveA", "CONTENIDO", "tk_LlaveC"]
            },

            "string": "2,epsilon, SENTENCIA_IF;2, [tk_if, tk_ParentesisA, CONDICION, tk_ParentesisC, tk_LlaveA, CONTENIDO, tk_LlaveC]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "SENTENCIA_WHILE"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["tk_while", "tk_ParentesisA", "CONDICION", "tk_ParentesisC", "tk_LlaveA", "CONTENIDO", "tk_LlaveC"]
            },

            "string": "2,epsilon, SENTENCIA_WHILE;2, [tk_while,  tk_ParentesisA,  CONDICION  ,   tk_ParentesisC,   tk_LlaveA,  CONTENIDO  , tk_LlaveC]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "SENTENCIA_FOREACH"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["tk_foreach", "tk_ParentesisA", "tk_Identificador", "tk_in", "tk_Identificador", "tk_ParentesisC", "tk_LlaveA", "CONTENIDO", "tk_LlaveC"]
            },

            "string": "2,epsilon, SENTENCIA_FOREACH; 2, [tk_foreach,  tk_ParentesisA,  tk_Identificador  , tk_in,   tk_Identificador,   tk_ParentesisC,   tk_LlaveA,  CONTENIDO  , tk_LlaveC]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "SENTENCIA_SWITCH"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["tk_Switch", "tk_ParentesisA", "tk_Identificador", "tk_ParentesisC", "tk_LlaveA", "CASES", "tk_LlaveC"]
            },

            "string": "2,epsilon, SENTENCIA_SWITCH; 2, [tk_foreach,  tk_ParentesisA,  tk_Identificador  , tk_in,   tk_Identificador,   tk_ParentesisC,   tk_LlaveA,  CONTENIDO  , tk_LlaveC]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "CASES"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["CASE", "CASES"]
            },

            "string": "2,epsilon, CASES; 2, [CASE, CASES]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "CASES"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "DEFAULT"
            },

            "string": "2,epsilon, CASES; 2, DEFAULT"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "CASES"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,epsilon, CASES; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "CASE"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["tk_Case", "VALOR", "tk_DosPuntos", "CONTENIDO", "POSIBLE_BREAK"]
            },

            "string": "2,epsilon, CASE; 2, [tk_Case, VALOR, tk_DosPuntos, CONTENIDO , POSIBLE_BREAK]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "DEFAULT"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["tk_Default", "tk_DosPuntos", "CONTENIDO", "POSIBLE_BREAK"]
            },

            "string": "2,epsilon, DEFAULT; 2, [tk_Default ,   tk_DosPuntos ,  CONTENIDO ,  POSIBLE_BREAK]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "POSIBLE_BREAK"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["tk_Break", "tk_PuntoYComa"]
            },

            "string": "2,epsilon, POSIBLE_BREAK; 2, [tk_Break , tk_PuntoYComa]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "POSIBLE_BREAK"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,epsilon, POSIBLE_BREAK; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "DEF_FUNCION"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["TIPO_VARIABLE", "tk_Identificador", "tk_Igual", "tk_ParentesisA", "PARAMETROS2", "tk_ParentesisC", "tk_Flecha", "tk_LlaveA", "CONTENIDO", "tk_LlaveC"]
            },

            "string": "2,epsilon, DEF_FUNCION; 2, [TIPO_VARIABLE ,  tk_Identificador  ,  tk_Igual  ,  tk_ParentesisA  ,  PARAMETROS  ,  tk_ParentesisC  ,  tk_Flecha  ,  tk_LlaveA  , CONTENIDO , tk_LlaveC]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "PARAMETROS"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["PARAMETRO", "PARAMETROS"]
            },

            "string": "2,epsilon, PARAMETROS; 2, [PARAMETRO,  PARAMETROS]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "PARAMETROS"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,epsilon, PARAMETROS; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "PARAMETRO"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["tk_Identificador", "tk_coma"]
            },

            "string": "2,epsilon, PARAMETRO; 2, [tk_Identificador,  tk_coma]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "PARAMETRO"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_Identificador"
            },

            "string": "2,epsilon, PARAMETRO; 2, tk_Identificador"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "LLAMADA_FUNCION"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["tk_Identificador", "tk_ParentesisA", "PARAMETROS2", "tk_ParentesisC", "tk_PuntoYComa"]
            },

            "string": "2,epsilon, LLAMADA_FUNCION; 2, [tk_Identificador  , tk_ParentesisA,  PARAMETROS2,  tk_ParentesisC  , tk_PuntoYComa]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "PARAMETROS2"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["VALOR", "PARAMETROS2"]
            },

            "string": "2,epsilon, PARAMETROS2; 2, [VALOR, PARAMETROS2]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "PARAMETROS2"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["tk_coma", "PARAMETROS2"]
            },

            "string": "2,epsilon, PARAMETROS2; 2, [tk_coma, PARAMETROS2]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "PARAMETROS2"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["tk_Identificador", "PARAMETROS2"]
            },

            "string": "2,epsilon, PARAMETROS2; 2, [tk_Identificador, PARAMETROS2]"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "PARAMETROS2"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,epsilon, PARAMETROS2; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_const",
                "cimaPila": "tk_const"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_const,tk_const;2,epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_var",
                "cimaPila": "tk_var"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_var,tk_var;2,epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_let",
                "cimaPila": "tk_let"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_let,tk_let;2,epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_Identificador",
                "cimaPila": "tk_Identificador"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_Identificador,tk_Identificador;2,epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_Igual",
                "cimaPila": "tk_Igual"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_Igual,tk_Igual;2,epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_PuntoYComa",
                "cimaPila": "tk_PuntoYComa"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_PuntoYComa,tk_PuntoYComa;2,epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_true",
                "cimaPila": "tk_true"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_true,tk_true;2,epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_false",
                "cimaPila": "tk_false"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_false,tk_false;2,epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_Numero",
                "cimaPila": "tk_Numero"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_Numero,tk_Numero;2,epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_Cadena",
                "cimaPila": "tk_Cadena"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_Cadena,tk_Cadena;2,epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_if",
                "cimaPila": "tk_if"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_if, tk_if; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_ParentesisA",
                "cimaPila": "tk_ParentesisA"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_ParentesisA, tk_ParentesisA; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_ParentesisC",
                "cimaPila": "tk_ParentesisC"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_ParentesisC, tk_ParentesisC; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_LlaveA",
                "cimaPila": "tk_LlaveA"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_LlaveA, tk_LlaveA; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_LlaveC",
                "cimaPila": "tk_LlaveC"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2,tk_LlaveC, tk_LlaveC; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_while",
                "cimaPila": "tk_while"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2, tk_while, tk_while; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_foreach",
                "cimaPila": "tk_foreach"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2, tk_foreach, tk_foreach; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_in",
                "cimaPila": "tk_in"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2, tk_in, tk_in; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_Switch",
                "cimaPila": "tk_Switch"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2, tk_Switch, tk_Switch; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_Case",
                "cimaPila": "tk_Case"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2, tk_Case, tk_Case; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_DosPuntos",
                "cimaPila": "tk_DosPuntos"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2, tk_DosPuntos, tk_DosPuntos; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_Default",
                "cimaPila": "tk_Default"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2, tk_Default, tk_Default; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_Break",
                "cimaPila": "tk_Break"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2, tk_Break, tk_Break; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_Flecha",
                "cimaPila": "tk_Flecha"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2, tk_Flecha, tk_Flecha; 2, epsilon"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "tk_coma",
                "cimaPila": "tk_coma"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "epsilon"
            },

            "string": "2, tk_coma, tk_coma; 2, epsilon"
        }
    ]

    noTerminales = ["S", "DECLARACION_VARIABLE", "SENTENCIA_WHILE", "SENTENCIA_FOREACH", "SENTENCIA_SWITCH", "DEF_FUNCION",
                    "LLAMADA_FUNCION", "TIPO_VARIABLE", "VALOR", "BOOLEANO", "SENTENCIA_IF", "CONDICION", "CONTENIDO", "CASES",
                    "CASE", "DEFAULT", "POSIBLE_BREAK", "PARAMETROS", "PARAMETRO", "PARAMETROS2"]

    terminales = ["tk_Identificador", "tk_Igual", "tk_PuntoYComa", "tk_true", "tk_false", "tk_Cadena", "tk_Numero", "tk_if",
                  "tk_ParentesisA", "tk_let", "tk_const", "tk_var", "tk_ParentesisA",  "tk_ParentesisC", "tk_LlaveA",
                  "tk_LlaveC", "tk_while", "tk_foreach", "tk_in", "tk_Switch", "tk_Case", "tk_DosPuntos", "tk_Default",
                  "tk_Break", "tk_Flecha", "tk_coma"]
