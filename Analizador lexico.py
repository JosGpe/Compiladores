def analizador_lexico(codigo_fuente):
    tokens = []
    estado_actual = 0
    buffer = ""

    def agregar_token(simbolo, tipo, valor):
        tokens.append((simbolo, tipo, valor))

    try:
        for caracter in codigo_fuente:
            if estado_actual == 0:
                if caracter.isalpha():
                    estado_actual = 1
                    buffer += caracter
                elif caracter.isdigit():
                    estado_actual = 2
                    buffer += caracter
                elif caracter.isspace():
                    continue
                else:
                    raise ValueError(f"Caracter inesperado: {caracter}")

            elif estado_actual == 1:  # Estado para identificadores
                if caracter.isalnum():
                    buffer += caracter
                else:
                    agregar_token("Identificador", "0", buffer)
                    buffer = ""
                    estado_actual = 0

            elif estado_actual == 2:  # Estado para números
                if caracter.isdigit():
                    buffer += caracter
                elif caracter == '.':
                    estado_actual = 3
                    buffer += caracter
                else:
                    agregar_token("Entero", "1", int(buffer))
                    buffer = ""
                    estado_actual = 0

            elif estado_actual == 3:  # Estado para números reales
                if caracter.isdigit():
                    buffer += caracter
                else:
                    agregar_token("Real", "2", float(buffer))
                    buffer = ""
                    estado_actual = 0

        # Manejar el caso cuando el código fuente termina en un estado no final
        if estado_actual == 1:
            agregar_token("Identificador", "0", buffer)
        elif estado_actual == 2:
            agregar_token("Entero", "1", int(buffer))
        elif estado_actual == 3:
            agregar_token("Real", "2", float(buffer))
    except ValueError as e:
        print(f"Error: {e}")
    
    return tokens

codigo = "Hola2 21.23 678 +"
tokens_codigo = analizador_lexico(codigo)
print(tokens_codigo)
