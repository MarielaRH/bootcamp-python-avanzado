from decorators import authenticated_class, validate_password


@authenticated_class
class Myclass:
    # El init method nos ayuda a inicilizar los valores de la clase (constructor)
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    # El self nos ayuda a mantener la referencia de los atributos (objetos) que están dentro de la misma clase
    # Self siempre será el primer parámetro de los métodos que definamos dentro de una clase, para poder hacer referencia a los
    # atributos de la clase
    def say_hello(self):
        print(f"Hello {self.username}, welcome to our system")

    @validate_password
    def show_password(self):
        print(
            f"Hi {self.username}, your password starts by: {self.password[:4]}{len(self.password[4:])* '*'}"
        )


# buscar sobre black y flek8, precommit, actions to format code

# conda es para manejar entornos virtuales, buscar más sobre eso
my_class = Myclass("mariela", "1234556789")
print(my_class.password)
my_class.say_hello()
my_class.show_password()

# buscar acerca de los slicing
# buscar sobre ki
# buscar como agregar typing a los decoradores
