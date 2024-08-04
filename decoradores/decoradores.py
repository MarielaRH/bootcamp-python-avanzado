"""
QUE ES UN DECORADOR EN PYTHON

Un decorador es un patrón de diseño en python que permite agregar funcionalidades a un objeto existente (funciones o clases),
sin modificar su estructura.

Estos permiten ejecutar funcionalidades extras después o antes de ejecutar un objeto (clase o función).

@example_decorator
def  test_function()
    return "output"

En desarrollo web los decoradores son usados comúnmente en autenticación, cacheo de respuestas, validación de datos.


!Datos informativos sobre las funciones
Las funciones pueden ser asignadas a una variable y luego ser invocadas desde la misma variable:

def plus_one(number):
    return number + 1

add_one = plus_one
add_one(5)

!Decoradores
Los decoradores son funciones que reciben una función como parámetro para ejecutarla luego, muy parecido a los callback de JS

def my_decorator(func):
    def wrapper():
        print('Something is happening before the funtion is called')
        funt()
        print('Something is happening after the funtion is called')
    return wrapper

@my_decorator
def say_hi():
    print('hi')

say_hi();

output: 
    Something is happening before the funtion is called
    hi
    Something is happening after the funtion is called

------------------- Internamente lo que el decorador hace es lo siguiente -------------------

def my_decorator(func):
    def wrapper():
        print('Something is happening before the funtion is called')
        funt()
        print('Something is happening after the funtion is called')
    return wrapper

def say_hi():
    print('hi')

say_hi = my_decorator(say_hi)
say_hi()

output: 
    Something is happening before the funtion is called
    hi
    Something is happening after the funtion is called



"""

# Definicion de decoradores

# def uppercase_decorator(func):
#     def wrapper():
#         fun = func()
#         print(fun)
#         make_uppercase = fun.upper()
#         return make_uppercase

#     return wrapper


# def split_decorator(func):
#     def wrapper():
#         fun = func()
#         # Acá ya no se recibe el valor inicial definido en la función say_hi, si no
#         # que se recibe el valor que devolvió el primer decorador
#         print(fun)
#         splitted_string = fun.split()
#         return splitted_string

#     return wrapper


# @split_decorator
# @uppercase_decorator
# def say_hi():
#     return "hello world"


# print(say_hi())

# -----------------------------------------------------------------


# Decoradores con parámetros


# def decorador_con_parametros(func):
#     # En la función wrapper se reciben los parámetros que son requeridos
#     # para la función a la que se le aplica el decorador
#     def wrapper(name, lastname):
#         print("Hi ,")
#         func(name, lastname)

#     return wrapper


# @decorador_con_parametros
# def say_hi(name, lastname):
#     print(name, lastname)


# say_hi(name="Mariela", lastname="Rivas")


# ARGS -----------------------------------------------------------------
# def say_hi(*args):
#     print(type(args))
#     # Los args pueden ser recorrigos ya que estos se reciben en una tupla
#     for arg in args:
#         print(f"Hi {arg}")


# say_hi("Mariela", "Lucía")  # se pasan paramentros de forma posicional


# kwARGS -----------------------------------------------------------------
# def say_hi(**kwargs):
#     print(type(kwargs))  # dict
#     # Los args pueden ser recorrigos ya que estos se reciben en una tupla
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")


# kwargs = {"name": "Mariela", "lastname": "Rivas"}

# print(kwargs)  # diccionario completo
# a, b = kwargs
# print(a, b)  # se obtienen únicamente las llaves del diccionario

# say_hi(
#     **kwargs
# )  # debemos colocar ** para desestructurar el objeto, de lo contrario obtendríamos un error


# DECORATOR WITH ARGUMENTS ----------------------------------------------
# def decorator_with_arguments(param1, param2, param3):
#     def decorator(
#         func,
#     ):  # esta función es la encargada de recibir la función que está siendo decorada
#         def wrapper(
#             func_param1, func_param2
#         ):  # obtiene los parámetros de la función que está siendo decorada
#             print(param1, param2, param3)
#             print(func_param1, func_param2)
#             return func(func_param1, func_param2)

#         return wrapper

#     return decorator


# @decorator_with_arguments(
#     "decorator1", "decorator2", "decorator3"
# )  # le pasamos parámetros al decorador
# def my_function(func_param1, func_param2):  # pasamos parámetros a la función
#     print(f"my_funtion {func_param1} {func_param2}")


# my_function("Hola", "Mundo")

# EJERCICIO PRACTICO ----------------------------------------------
# Validar si dos numeros son enteros


def validate_int_number(my_function):
    def wrapper(first_number, second_number):
        if isinstance(first_number, int) and isinstance(second_number, int):
            print("Ambos números son enteros")
            return my_function(first_number, second_number)
        else:
            raise TypeError("Ambos parámetros deben ser números enteros")

    return wrapper


@validate_int_number
def sum_int_numbers(first_number, second_number):
    return first_number + second_number


sum_int_numbers(1, 2.3)
