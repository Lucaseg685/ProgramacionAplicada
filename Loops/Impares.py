# Solicita al usuario un número de repeticiones
times = input("Ingresa un número de repeticiones: ")
times = float(times)  # Convierte la entrada a un número decimal
times = int(times)    # Convierte el número decimal a un número entero

# Imprime el tipo y el valor de la variable times
print("Tipo de times:", type(times))
print("Valor de times:", times)

# Verifica si times es igual a cero
if times == 0:
    print("No hacer nada")
else:
    # Realiza un bucle que cuenta desde 1 hasta el valor de times
    for i in range(1, times + 1):
        print("i =", i)
