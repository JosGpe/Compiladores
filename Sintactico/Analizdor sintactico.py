from tabulate import tabulate

class Constantes:
    ERROR = -1
    IDENTIFICADOR = 0
    SIMBOLO = 1
    SIGNOPESOS = 2
    E = 3
    INICIAL = 5

class Stack:
    def __init__(self):
        self.items = []
        self.push(Constantes.SIGNOPESOS)
        self.push(Constantes.IDENTIFICADOR)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def mostrar_pila(self):
        return [str(dato) for dato in self.items]

def imprimir_tabla(datos):
    headers = ["Pila", "Entrada", "Salida"]
    print(tabulate(datos, headers=headers, tablefmt="grid"))

def primer_ejercicio(texto):
    datos = []
    pila = Stack()

    estado = Constantes.INICIAL
    d = 2
    lexema = ""

    i = 0
    while i < len(texto):
        c = texto[i]
        if estado == Constantes.INICIAL:
            if es_Letra(c) or c == '_':
                estado = Constantes.IDENTIFICADOR
                lexema += c
            elif c == '+':
                pila.push(Constantes.SIMBOLO)
                pila.push(d)
                d += 1
                estado = Constantes.INICIAL
                lexema = ""
                datos.append([pila.mostrar_pila(), texto[i:], pila.peek()])
            elif c == '$':
                pila.clear()
                nuevaPila = Stack()
                nuevaPila.push(Constantes.E)
                nuevaPila.push(1)
                datos.append([nuevaPila.mostrar_pila(), "$", nuevaPila.peek()])
            else:
                print("ERROR")
        elif estado == Constantes.IDENTIFICADOR:
            if es_Letra(c) or isReal(c) or c == '_':
                estado = Constantes.IDENTIFICADOR
                lexema += c
            else:
                pila.push(Constantes.IDENTIFICADOR)
                pila.push(d)
                d += 1
                estado = Constantes.INICIAL
                lexema = ""
                i -= 1
                datos.append([pila.mostrar_pila(), texto[i:], pila.peek()])
        i += 1

    return datos

def segundo_ejercicio(texto):
    datos = []
    pila = Stack()

    estado = Constantes.INICIAL
    d2 = 2
    d3 = 3
    lexema = ""

    i = 0
    while i < len(texto):
        c = texto[i]
        if estado == Constantes.INICIAL:
            if es_Letra(c) or c == '_':
                estado = Constantes.IDENTIFICADOR
                lexema += c
            elif c == '+':
                pila.push(Constantes.SIMBOLO)
                pila.push(d3)
                estado = Constantes.INICIAL
                lexema = ""
                datos.append([pila.mostrar_pila(), texto[i:], pila.peek()])
            elif c == '$':
                pila.clear()
                nuevaPila = Stack()
                nuevaPila.push(Constantes.E)
                nuevaPila.push(1)
                datos.append([nuevaPila.mostrar_pila(), "$", nuevaPila.peek()])
            else:
                print("ERROR")
        elif estado == Constantes.IDENTIFICADOR:
            if es_Letra(c) or isReal(c) or c == '_':
                estado = Constantes.IDENTIFICADOR
                lexema += c
            else:
                pila.push(Constantes.IDENTIFICADOR)
                pila.push(d2)
                estado = Constantes.INICIAL
                lexema = ""
                i -= 1
                datos.append([pila.mostrar_pila(), texto[i:], pila.peek()])
        i += 1

    return datos

def isReal(c):
    if 48 <= ord(c) <= 57:
        return True
    else:
        return False

def es_Letra(c):
    if (65 <= ord(c) <= 90 or ord(c) == 95) or (97 <= ord(c) <= 122 or ord(c) == 95):
        return True
    else:
        return False

def main():
    print("    Primer Ejercicio    ")
    dt_primer_ejercicio = primer_ejercicio("hola+mundo$")
    imprimir_tabla(dt_primer_ejercicio)

    print("    Segundo Ejercicio   ")
    dt_segundo_ejercicio = segundo_ejercicio("a+b+c+d+e+f$")
    imprimir_tabla(dt_segundo_ejercicio)

if __name__ == "__main__":
    main()