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
                "insertoPila": "declaracionVariable"
            },

            "string": "2,epsilon,S;2,declaracionVariable"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "S"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "if"
            },

            "string": "2,epsilon,S;2,if"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "S"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "while"
            },

            "string": "2,epsilon,S;2,while"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "S"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "foreach"
            },

            "string": "2,epsilon,S;2,foreach"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "S"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "switch"
            },

            "string": "2,epsilon,S;2,switch"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "S"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "def_func"
            },

            "string": "2,epsilon,S;2,def_func"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "S"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "call_func"
            },

            "string": "2,epsilon,S;2,call_func"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "declaracionVariable"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": ["tipoVariable", "tk_Identificador", "tk_Igual", "valor", "tk_PuntoYComa"]
            },

            "string": "2,epsilon,declaracionVariable;2,tipoVariable tk_Identificador tk_Igual valor tk_PuntoYComa"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "tipoVariable"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_const"
            },

            "string": "2,epsilon,tipoVariable;2,tk_const"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "tipoVariable"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_var"
            },

            "string": "2,epsilon,tipoVariable;2,tk_var"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "tipoVariable"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_let"
            },

            "string": "2,epsilon,tipoVariable;2,tk_let"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "valor"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_Numero"
            },

            "string": "2,epsilon,valor;2,tk_Numero"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "valor"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_Cadena"
            },

            "string": "2,epsilon,valor;2,tk_Cadena"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "valor"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "booleano"
            },

            "string": "2,epsilon,valor;2,booleano"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "booleano"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_true"
            },

            "string": "2,epsilon,booleano;2,tk_true"
        },
        {
            "first": {
                "estado": 2,
                "entrada": "epsilon",
                "cimaPila": "booleano"
            },
            "last": {
                "estadoFinal": 2,
                "insertoPila": "tk_false"
            },

            "string": "2,epsilon,booleano;2,tk_false"
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
        }
    ]

    noTerminales = ["S","declaracionVariable", "tipoVariable", "valor", "booleano"]