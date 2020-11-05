class Pila():
    def __init__(self):
        self.pila = []

    def isEmpty(self):
        return self.pila == []

    def push(self, item):
        self.pila.append(item)

    def pop(self):
        if len(self.pila) > 0:
            return self.pila.pop()
        else:
            return "Esta vacia"

    def obtenerUltimoAgregado(self):
        if len(self.pila) > 0:
            return self.pila[len(self.pila) - 1]
        else:
            return "Esta vacia"

    def getLength(self):
        return len(self.pila)

    def getItems(self):
        return self.pila

    def extend(self, parametro):
        aux =parametro[::-1]
        for i in aux:
            self.pila.append(i)