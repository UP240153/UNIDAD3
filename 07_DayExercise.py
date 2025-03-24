it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print('El tamaño de it_companies es:',len(it_companies))
it_companies.add('Twitter')

it_companies.add('youtube')
it_companies.add('firefox')
it_companies.add('yahoo')
it_companies.add('linux')

it_companies.remove('Apple')

print('Ambos se encargan de quitar un elemento de una lista. \nRemover puede generar un error si el elemento no existe. \ndescartar no puede generar este error.')

print(A.union(B))
print(A.intersection(B))  
print(A.issubset(B),',A si es un sibconjunto de B')
print(A.isdisjoint(B),',A y B no son conjuntos disjuntos')

print(A.union(B))
print(B.union(A))

print('A tiene',len(A),'Numero de datos y B tiene',len(B),'numero de datos.')
del(A)
del(B)

ages2=set(age)
print(len(age),len(ages2))
print('La lista es mas larga que el conjunto')

print('Cadena:Es un conjunto de caracteres que no se pueden modificar. \nLista: Es una colección ordenada y modificable de elementos. \nTupla: Es como una lista, pero no se puede modificar. \nConjunto: Es una colección desordenada de elementos únicos.')

oracion = "I am a teacher and I love to inspire and teach people."
palabras = oracion.replace(".", "").split()
palabras_unicas = set(palabras)
num_palabras_unicas = len(palabras_unicas)
print("Número de palabras únicas:", num_palabras_unicas)