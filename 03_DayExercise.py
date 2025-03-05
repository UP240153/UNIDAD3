age = int(18)
height = float(1.83)
Triangle_area = complex(100 + 100j)


base=int (input('ingrese la base del triangulo'))
alto=int (input('Ingrese la altura del triangulo'))
area= float (base * alto * 0.5)
print('El area del triangulo es:', area)

lado1= int (input('ingrese el primer lado'))
lado2= int (input('ingrese el segundo lado'))
lado3= int (input('ingrese el tercer lado'))
perimetro= float (lado1 + lado2 + lado3)
print('El perimetro del triangulo es:', perimetro)

largo= int(input('ingrese el largo'))
ancho= int(input('ingrese el ancho'))
area2= float(largo + ancho)
perimetro2= float(area2 * 2)
print('El area del rectangulo es:', area2)
print('El perimetro del rectangulo es:', perimetro2)


pi= float(3.14)
radio= float(input('Ingrese el radio'))
area3= float(pi * radio * radio)
cir= float(2 * pi * radio)
print('El area del circulo es:', area3)
print('La circunferencia es:', cir)

X1= float(input('ingrese las coordenadas x del primer punto'))
X2= float(input('ingrese las coordenadas x del segundo punto'))
Y1= 2*X1-2
Y2= 2*X2-2
m= (Y2-Y1)/(X2-X1)
print('La pendiente es igual a:',m)

X1_2= float(input('ingrese las coordenadas x del primer punto'))
X2_2= float(input('ingrese las coordenadas x del segundo punto'))
Y1_2= float(input('ingrese las coordenadas y del primer punto'))
Y2_2= float(input('ingrese las coordenadas y del segundo punto'))
m_2= (Y2_2-Y1_2)/(X2_2-X1_2)
d= ((X2_2-X1_2)**2)+((Y2_2-Y1_2)**2)**0.5
print('La pendiente es igual a:',m_2)
print('La distancia euclidiana entre los dos puntos es:',d)

print('La pendiente del primer vector es:',m)
print('Mientras que el segundo es:',m_2)

x= float(input('Ingresa el valor de x'))
y = x**2 + (6*x) + 9
print('El valor de y es:',y)
print('y es igual a 0 cuando x es igual a -3')

print(len('python') != len('dragon'))

print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon')

print('There is no ON in both dragon and python')

print(str(float(len('python'))))

nn=(float(input('Ingrese su numero:')))
ss=float(nn)%2
if ss == 0: 
    print('El numero es par')
else:
    print('El numero es impar')
    
print(7//3 == 2.7)

print(type('10') == type(10))

print(int(9.8) == 10)

H= float(input('Ingrese sus horas de trabajo'))
TH= float(input('Ingrese su tarifa por hora'))
Sa = H*TH
print('Su salario es de:', Sa)

Y= float(input('Ingrese los años que ha vivido'))
S=(float(Y*31536000))
print('Usted ha vivido:', S, 'segundos')

print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')