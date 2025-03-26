numeros = [0,1,2,3, 4, 5,6,7,8,9,10]
for numeros in numeros: 
    print(numeros)  

contar = 0
while contar < 11:
    print(contar)
    contar = contar + 1

numeros2 = [10,9,8,7,6,5,4,3,2,1,0]
for numeros2 in numeros2: 
    print(numeros2)  

contar2 = 10
while contar2 > -1:
    print(contar2)
    contar2 = contar2 - 1

for corchetes in range(1, 8):
    print("#" * corchetes)

for ejeX in range(8):
    for ejeY in range(8): 
        print("#", end=" ") 
    print() 

a=0
b=0
while a < 11:
    R = a * b
    print(a,'x',b,'=',R)
    a = a + 1
    b = b + 1

Lista1= ['Python', 'Numpy','Pandas','Django', 'Flask']
for Lista1 in Lista1: 
    print(Lista1)  

for Lista2 in range(0, 101): 
    if Lista2 % 2 == 0:  
        print(Lista2)

for Lista3 in range(0, 101): 
    if Lista3 % 2 == 1:  
        print(Lista3)

total = 0
for Lista4 in range(1, 101): 
    print(Lista4) 
    total = total + Lista4 
print("La suma de todos los números es:", total)

total2 = 0
for Lista2_ in range(0, 101): 
    if Lista2_ % 2 == 0:  
        total2 = total2 + Lista2_
print("La suma de todos los números pares es:", total2)

total3 = 0
for Lista_3 in range(0, 101): 
    if Lista_3 % 2 == 1:  
        total3 = total3 + Lista_3
print("La suma de todos los números pares es:", total3)