# Basilisk


    S => DECLARACION_VARIABLE, S
    |SENTENCIA_IF, S
    |SENTENCIA_WHILE, S
    |SENTENCIA_FOREACH, S
    |SENTENCIA_SWITCH, S
    |DEF_FUNCIONES, S
    |LLAMADA_FUNCION, S
    |epsilon


    CONTENIDO => DECLARACION_VARIABLE, CONTENIDO
            |SENTENCIA_IF, CONTENIDO
            |SENTENCIA_WHILE, CONTENIDO
            |SENTENCIA_FOREACH, CONTENIDO
            |SENTENCIA_SWITCH, CONTENIDO
            |DEF_FUNCIONES, CONTENIDO
            |LLAMADA_FUNCION, CONTENIDO
            |epsilon

    DECLARACION_VARIABLE => TIPO_VARIABLE, indentificador, token_= , VALOR , token_;

    TIPO_VARIABLE => let
                |var
                |const

    VALOR => numero
        | cadena
        | BOOLEANO

    BOOLEANO => true
            |false

    CONDICION => BOOLEANO
            | identificador

    SENTENCIA_IF => token_if, tk_(, CONDICION , tk_), tk_{, CONTENIDO, tk_}

    SENTENCIA_WHILE => token_while, tk_(, booleano | identificador , tk_), tk_{, contenido, tk_}

    SENTENCIA_FOREACH => tk_foreach, identificador, tk_in, identificador, tk_), tk_{, contenido, tk_}

    SENTENCIA_SWITCH => tk_switch, tk_(, identificador, tk_), tk_{, cases , tk_}

    CASES => case, cases
        |DEFAULT
        |epsilon

    case => tk_case, valor, tk_:, contenido, posible_break

    default => tk_default, tk_:, contenido, posible_break

    posible_break => tk_break, tk_;
                | vacio

    def_funciones => tipoVariable, identificador, tk_=, tk_(, parametros, tk_), tk_=>, tk_{, contenido, tk_}

    parametros => parametro, parametros
            | vacio

    parametro => identificador, tk_,
            |identificador

    llamada_funcion => identificador, tk_(, parametros2, tk_), tk_;

    parametros2 => valor2, parametros2
            |vacio

    valor2 => numero
        |cadena
        | booleano
        |,
