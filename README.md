# Gramatica Basilisk


    S => DECLARACION_VARIABLE, S
        |SENTENCIA_IF, S
        |SENTENCIA_WHILE, S
        |SENTENCIA_FOREACH, S
        |SENTENCIA_SWITCH, S
        |DEF_FUNCION, S
        |LLAMADA_FUNCION, S
        |epsilon

    CONTENIDO => DECLARACION_VARIABLE, CONTENIDO
            |SENTENCIA_IF, CONTENIDO
            |SENTENCIA_WHILE, CONTENIDO
            |SENTENCIA_FOREACH, CONTENIDO
            |SENTENCIA_SWITCH, CONTENIDO
            |DEF_FUNCION, CONTENIDO
            |LLAMADA_FUNCION, CONTENIDO
            |epsilon

    TIPO_VARIABLE => tk_let
                |tk_var
                |tk_const

    VALOR => numero
            | cadena
            | BOOLEANO

    BOOLEANO => true
               |false

    CONDICION => BOOLEANO
               | identificador

    DECLARACION_VARIABLE => TIPO_VARIABLE, tk_Indentificador, tk_Igual , VALOR , token_;

    SENTENCIA_IF => tk_if, tk_(, CONDICION , tk_), tk_{, CONTENIDO, tk_}

    SENTENCIA_WHILE => tk_while, tk_(, CONDICION , tk_), tk_{, CONTENIDO, tk_}

    SENTENCIA_FOREACH => tk_foreach, tk_( identificador, tk_in, identificador, tk_), tk_{, CONTENIDO, tk_}

    SENTENCIA_SWITCH => tk_switch, tk_(, identificador, tk_), tk_{, CASES , tk_}

    CASES => CASE, CASES
            |DEFAULT
            |epsilon

    CASE => tk_case, VALOR, tk_:, CONTENIDO, POSIBLE_BREAK

    DEFAULT => tk_default, tk_:, CONTENIDO, POSIBLE_BREAK

    POSIBLE_BREAK => tk_break, tk_;
                   | epsilon

    DEF_FUNCION => TIPO_VARIABLE, identificador, tk_=, tk_(, PARAMETROS2, tk_), tk_=>, tk_{, CONTENIDO, tk_}

    LLAMADA_FUNCION => [identificador, tk_(, PARAMETROS2, tk_), tk_;]

    PARAMETROS2 => [VALOR, PARAMETROS2]
            | [tk_, PARAMETROS2]
            | [tk_Identificador, PARAMETROS2]
            |epsilon
        
