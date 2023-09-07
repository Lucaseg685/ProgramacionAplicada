def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

while True:
    detector_primos = int(input('Ingrese un valor para saber si es primo: '))
    
    if es_primo(detector_primos):
        print(f'{detector_primos} efectivamente es un número primo.\n')
    else:
        print(f'{detector_primos} lastimosamente no es un número primo.\n')
    
    respuesta = input('¿Deseas averiguar si otro número es primo? Escribe "si" para afirmativo, de lo contrario, presiona Enter: ')
    if respuesta.lower() != 'si':
        break
