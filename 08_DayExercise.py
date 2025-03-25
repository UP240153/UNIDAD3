perro = {}

perro['nombre'] = 'Jillo'
perro['color'] = 'Blanco'
perro['raza'] = 'Cocker spaniel'
perro['patas'] = 4
perro['edad en años'] = 13 

print("Diccionario perro:", perro)

estudiante = {
    'nombre': 'Santiago',
    'apellido': 'Mendoza lópez',
    'género': 'Masculino',
    'edad': 18,
    'estado_civil': 'Soltero',
    'habilidades': ['Python', 'Japones'],
    'país': 'Mexico',
    'ciudad': 'Encarnacion de diaz',
    'dirección': 'Cerro viejo #504'
}
longitud_estudiante = len(estudiante)
print("Longitud del diccionario estudiante:", longitud_estudiante)

tipo_habilidades = type(estudiante['habilidades'])
print("Tipo de dato de habilidades:", tipo_habilidades)

estudiante['habilidades'].append('Matematicas')
estudiante['habilidades'].append('Edicion de videos')
print("Habilidades actualizadas:", estudiante['habilidades'])

claves_estudiante = list(estudiante.keys())
print("Claves del diccionario estudiante:", claves_estudiante)

valores_estudiante = list(estudiante.values())
print("Valores del diccionario estudiante:", valores_estudiante)

tuplas_estudiante = list(estudiante.items())
print("Diccionario como lista de tuplas:", tuplas_estudiante)

estudiante.pop('estado_civil')
print("Diccionario estudiante después de eliminar estado civil:", estudiante)

del perro
print("Diccionario perro eliminado.")