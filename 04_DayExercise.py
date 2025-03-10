T='Thirty'
D='Days'
l='Of'
H='Python'
space=' '
print(T+space+D+space+l+space+H)

c='Coding'
J='For'
A='All'
print(c+space+J+space+A)

company=c+space+J+space+A
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

pto= company[6:14]
print(pto)

print(company.index(c))

print(company.replace('Coding','Python'))

X=(company.replace('Coding','Python'))
Y=X.replace('All','Everyone')
print(Y)

print(company.split())

S="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(S.split(','))

print(company.index(c))
print('"For" es el carácter en el índice 0')
print(company.index(A))
print('"All" es el carácter en el ultimo indice')
print(company.index(J))
print('No existe un caracter con indice 10 en  "Coding For All"')

Python='P'
For='F'
Everyone='E'
P_F_E=Python+space+For+space+Everyone
print(P_F_E)

coding='C'
For='F'
All='A'
C_F_A=coding+space+For+space+All
print(C_F_A)

print(C_F_A.index('C'))
print(C_F_A.index('F'))
print(C_F_A.rfind('l'))

sup='You cannot end a sentence with because because because is a conjunction'
print(sup.index('because'))
print(sup.rindex('because'))
sac=sup[0:30]
lap=sup[55:90]
print(sac+space+lap)

print('"Coding For All" no comienza con una subcadena')
print('"Coding For All" no termina con una subcadena')
hat='   Coding For All      '
print(hat[3:19])

YU='30DaysOfPython'
YA='thirty_days_of_python'
print(YU.isidentifier())
print(YA.isidentifier())
print('La variable thirty_days_of_python se vuelbe verdadera')

DOC=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
DAC=' '.join(DOC)
print(DAC)

XNG='I am enjoying this challenge \nI just wonder what is next'
print(XNG)

print('Name    \tAge\tCountry \tCity')
print('Asabeneh\t250\tFinland \tHelsinki')

radius = 10
area = 3.14 * radius ** 2
Total= 'The area of a circle with radius %s is %s meters square.'%(radius, area)
print(Total)

a = 8
b = 6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')