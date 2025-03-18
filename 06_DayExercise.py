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