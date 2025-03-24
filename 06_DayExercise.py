empty_tuple = tuple()

hermanas=('María Mendoza','Sofía Mendoza','Camila Mendoza','Valentina Mendoza')
hermanos=('Juan Mendoza','Pedro Mendoza','Carlos Mendoza','Andrés Mendoza','Felipe Mendoza')
HERMANOS=hermanas+hermanos
tuple(HERMANOS)
print('Tengo',len(HERMANOS),'Hermanos y Hermanas')

Padres=('Patricia López','Juan Mendoza')

Familia=HERMANOS+Padres
tuple(Familia)
print('Mi Familia está completa es',Familia)

Familia=0
hermanas=('María Mendoza','Sofía Mendoza','Camila Mendoza','Valentina Mendoza')
hermanos=('Juan Mendoza','Pedro Mendoza','Carlos Mendoza','Andrés Mendoza','Felipe Mendoza')
Padres=('Patricia López','Juan Mendoza')

frutas = ("manzana", "plátano", "naranja", "uva", "mango")
vegetales = ("zanahoria", "brócoli", "espinaca", "tomate", "papa")
productos_animales = ("leche", "huevo", "queso", "mantequilla", "yogur")

comida_tp = frutas + vegetales + productos_animales

print(comida_tp)
print(tuple(comida_tp))

comida_it= comida_tp
(tuple(comida_it))

Medio=(comida_tp[7:8])
print(Medio)

primeros_tres=(comida_tp[0:3])
print(primeros_tres)
ultimos_tres=(comida_tp[12:])
print(ultimos_tres)

del(comida_tp)
print(comida_it)

paises_nordicos = ('Dinamarca', 'Finlandia', 'Islandia', 'Noruega', 'Suecia')
tuple(paises_nordicos)
print("Estonia" in paises_nordicos) 
print("Islandia" in paises_nordicos)