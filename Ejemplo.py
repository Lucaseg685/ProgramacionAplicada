# Definimos una lista llamada "lista" con varios colores
colores = ["Rojo", "Azul", "Amarillo", "Naranja", "Violeta", "Verde"]

# Imprimimos la lista, su tipo y el elemento en la posición 2
print(colores)
print("Tipo de la lista:", type(colores))
print("Elemento en la posición 2:", colores[2])

# Imprimimos la cantidad de elementos en la lista y una porción de la lista
print("Mi lista tiene un total de", len(colores), "elementos")
print("Elementos desde la posición 0 hasta 2:", colores[0:3])
print("Elementos desde el inicio hasta la posición 1:", colores[:2])

# Añadimos elementos a la lista y luego imprimimos la lista actualizada
colores.append("Blanco")
colores.insert(3, "Negro")
print("Lista después de añadir y insertar elementos:", colores)

# Extendemos la lista con más colores y eliminamos un color específico
colores.extend(['Marron', 'Gris'])
colores.remove("Marron")
print("Lista extendida y después de eliminar 'Marron':", colores)

# Insertamos 'Marron' en una posición específica y guardamos su longitud en "size"
colores.insert(8, "Marron")
size = len(colores)

# Creamos una nueva lista que contiene tres copias de la lista original
lista_nueva = colores * 3
print("Nueva lista creada a partir de tres copias de la lista original:", lista_nueva)

# Ordenamos la lista original de menor a mayor y de mayor a menor
colores.sort()
print("Lista ordenada de menor a mayor:", colores)
colores.sort(reverse=True)
print("Lista ordenada de mayor a menor:", colores)

# Creamos una lista de números y la ordenamos
numeros = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Lista de números sin ordenar:", numeros)
numeros.sort()
print("Lista de números ordenada de menor a mayor:", numeros)
numeros.sort(reverse=True)
print("Lista de números ordenada de mayor a menor:", numeros)
