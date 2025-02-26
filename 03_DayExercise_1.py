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