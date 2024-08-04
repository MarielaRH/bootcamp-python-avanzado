class Pila:
    def __init__(self):
        self.lista = []

    def lista_vacia(self):
        return len(self.lista) == 0

    def obtener_top(self):
        if self.lista():
            return None
        # Retorna el ultimo elemento de la lista
        return self.lista[-1]

    def agregar_elemento(self, elemento):
        self.lista.append(elemento)

    def quitar_elemento(self):
        return self.lista.pop()


if __name__ == "__main__":
    pila = Pila()
    print(pila.lista_vacia())
    pila.agregar_elemento("1")
    pila.agregar_elemento("2")
    pila.agregar_elemento("3")
    pila.agregar_elemento("4")

    print(pila.lista)
    print(pila.quitar_elemento())
    print(pila.lista)
