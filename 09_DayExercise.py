age = int(input('Introdusca su edad: '))
if age >= 18:
    print("Tu puedes conducir.")
else:
    print("necesitas esperar", 18 - age, "años.")

my_age = 18

if age == my_age:
    print("tenemos la misma edad")
elif age > my_age:
    print("tu tienes", age - my_age, "años menos que yo")
else:
    print("yo tengo", my_age - age, "años mas que tu")

# 3
a = int(input("Introdusca su numeror: "))
b = int(input("Introdusca su numeror: "))
if a > b:
    print(a, "es mayor que", b)
elif a < b:
    print(a, "es menor que", b)
else:
    print("Ambos numeros son iguales")

score = int(input("Enter score: "))

grades = {}
for i in range(90, 101):
    grades[i] = 'A'
for i in range(70, 90):
    grades[i] = 'B'
for i in range(60, 70):
    grades[i] = 'C'
for i in range(50, 60):
    grades[i] = 'D'
for i in range(0, 50):
    grades[i] = 'F'

print("Calificacion:", grades[score])

month = input('Introdusca  un mes: ').title()
if month in ["Septiembre", "Octubre", "Noviembre"]:
    print("Es otoño")
if month in ["Diciembre", "Enero", "Febrero"]:
    print("Es invierno")
if month in ["Marso", "Abril", "Mayo"]:
    print("Es primavera")   
else: print("Summer")

fruits = ['banana', 'naranja', 'mango', 'limon']
fruit = input('introdusca una fruta: ')
print('Esa fruta existe en la lista' if fruit in fruits else fruits.append(fruit))
print(fruits)

person = {
    'Nombre': 'Santiago',
    'Apellido': 'Mendoza lopez',
    'edad': 18,
    'paiz': 'Mexico',
    'casado': False,
    'abilidades': ['japones', 'editar videos', 'matematicas', 'conducir motosicletas', 'Python'],
    'direccion': {
        'calle': 'cerro viejo',
        'numero de casa': '504'
    }
}

if person['abilidades']:
    print(person['abilidades'][len(person['abilidades']) // 2])
    print("Python" in person['abilidades'])
    if ['Javascript', 'React'] == person['abilidades']:
        print('Front End Developer')
    elif ['Node', 'MongoDB', 'React'] == person['abilidades']:
        print('Full Stack Developer')
    else:
        print("titulo desconocido")

if person['casado']:
    print(person['Nombre'], person['Apellido'], "vive en", person['paiz'], ". Esta casado")
else:
    print(person['Nombre'], person['Apellido'], "vive en", person['paiz'], ". Esta soltero")