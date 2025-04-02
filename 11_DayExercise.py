def suma_dos_numeros():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    return a + b
print(suma_dos_numeros())

def area_del_circulo():
    r = float(input("Ingrese el radio del círculo: "))
    pi = 3.14159 
    return pi * r ** 2
print(area_del_circulo())

def suma_todos_numeros():
    numeros = list(map(float, input("Ingrese números separados por espacio: ").split()))
    return sum(numeros)
print(suma_todos_numeros())

def convertir_celsius_a_fahrenheit():
    c = float(input("Ingrese la temperatura en Celsius: "))
    return (c * 9/5) + 32
print(convertir_celsius_a_fahrenheit())

def verificar_estacion():
    mes = input("Ingrese un mes: ")
    estaciones = {
        'Invierno': ['Diciembre', 'Enero', 'Febrero'],
        'Primavera': ['Marzo', 'Abril', 'Mayo'],
        'Verano': ['Junio', 'Julio', 'Agosto'],
        'Otoño': ['Septiembre', 'Octubre', 'Noviembre']
    }
    for estacion, meses in estaciones.items():
        if mes.capitalize() in meses:
            return estacion
    return "Mes inválido"
print(verificar_estacion())

def calcular_pendiente():
    x1 = float(input("Ingrese x1: "))
    y1 = float(input("Ingrese y1: "))
    x2 = float(input("Ingrese x2: "))
    y2 = float(input("Ingrese y2: "))
    if x2 == x1:
        return "Pendiente indefinida"
    return (y2 - y1) / (x2 - x1)
print(calcular_pendiente())

def resolver_ecuacion_cuadratica():
    a = float(input("Ingrese a: "))
    b = float(input("Ingrese b: "))
    c = float(input("Ingrese c: "))
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales"
    elif discriminante == 0:
        return -b / (2*a)
    
    raiz1 = (-b + (discriminante ** 0.5)) / (2*a)
    raiz2 = (-b - (discriminante ** 0.5)) / (2*a)
    return raiz1, raiz2
print(resolver_ecuacion_cuadratica())

def calcular_media():
    numeros = list(map(float, input("Ingrese números separados por espacio: ").split()))
    if not numeros:
        return "Lista vacía"
    return sum(numeros) / len(numeros)
print(calcular_media())

def calcular_mediana():
    numeros = list(map(float, input("Ingrese números separados por espacio: ").split()))
    if not numeros:
        return "Lista vacía"
    numeros.sort()
    n = len(numeros)
    medio = n // 2
    return numeros[medio] if n % 2 != 0 else (numeros[medio - 1] + numeros[medio]) / 2
print(calcular_mediana())

def calcular_moda():
    numeros = list(map(int, input("Ingrese números separados por espacio: ").split()))
    if not numeros:
        return "Lista vacía"
    
    frecuencia = {}
    for num in numeros:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1
    
    max_frecuencia = max(frecuencia.values())
    modas = [k for k, v in frecuencia.items() if v == max_frecuencia]
    return modas if len(modas) > 1 else modas[0]
print(calcular_moda())

def calcular_varianza():
    numeros = list(map(float, input("Ingrese números separados por espacio: ").split()))
    if len(numeros) < 2:
        return "Se requiere al menos dos elementos"
    media = sum(numeros) / len(numeros)
    return sum((x - media) ** 2 for x in numeros) / len(numeros)
print(calcular_varianza())

def calcular_desviacion_std():
    varianza = calcular_varianza()

    return varianza ** 0.5
print(calcular_desviacion_std())

def es_primo():
    n = int(input("Ingrese un número: "))
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True
print(es_primo())

def todos_unicos():
    elementos = input("Ingrese elementos separados por espacio: ").split()
    return len(elementos) == len(set(elementos))
print(todos_unicos())

def mismo_tipo():
    elementos = input("Ingrese elementos separados por espacio: ").split()
    return all(isinstance(item, type(elementos[0])) for item in elementos) if elementos else False
print(mismo_tipo())

def es_variable_valida():
    var = input("Ingrese el nombre de la variable: ")
    return var.isidentifier()
print(es_variable_valida())