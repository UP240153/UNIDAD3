import random
import string

def id_usuario_aleatorio():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

print(id_usuario_aleatorio())

def generar_ids_por_usuario():
    num_caracteres = int(input("Ingrese el número de caracteres: "))
    num_ids = int(input("Ingrese el número de IDs: "))
    return [''.join(random.choices(string.ascii_letters + string.digits, k=num_caracteres)) for _ in range(num_ids)]

print(generar_ids_por_usuario())

def generar_color_rgb():
    return f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})"

print(generar_color_rgb())

def lista_colores_hexadecimales(n):
    return ["#" + ''.join(random.choices("0123456789abcdef", k=6)) for _ in range(n)]

print(lista_colores_hexadecimales(3))

def lista_colores_rgb(n):
    return [generar_color_rgb() for _ in range(n)]

print(lista_colores_rgb(3))

def generar_colores(tipo_color, n):
    if tipo_color == 'hexa':
        return lista_colores_hexadecimales(n)
    elif tipo_color == 'rgb':
        return lista_colores_rgb(n)
    else:
        return "Tipo de color no válido"

print(generar_colores('hexa', 3))
print(generar_colores('rgb', 3))

def mezclar_lista(lista):
    random.shuffle(lista)
    return lista

print(mezclar_lista([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def numeros_aleatorios_unicos():
    return random.sample(range(10), 7)

print(numeros_aleatorios_unicos())