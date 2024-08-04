# Collections

# Es un módulo que ofrece python para implementar colas de una manera más eficiente mediante deque
from collections import deque


class Cola:
    def __init__(self) -> None:
        self.lista = deque()

    def lista_vacia(self):
        return len(self.lista) == 0

    def agregar_elemento(self, elemento):
        self.lista.append(elemento)

    def quitar_elemento(self):
        if self.lista_vacia():
            return None
        return self.lista.popleft()


if __name__ == "__main__":
    cola = Cola()
    print(cola.lista)

    cola.agregar_elemento("Jani")
    cola.agregar_elemento("Fernando")
    cola.agregar_elemento("Javier")
    cola.agregar_elemento("Soledad")

    print(cola.lista)

    cola.quitar_elemento()

    print(cola.lista)
