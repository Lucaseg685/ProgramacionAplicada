#CALCULANDO EL FACTORIAL DE UN NÚMERO ("n").

#FUNCIÓN PARA CALCULAR EL FACTORIAL.

def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*factorial(n-1)
   return resultado

#CALCULAMOS EL FACTORIAL DE 5.
numero=int(input("Numero:"))
fact=factorial(numero)

#VISUALIZAMOS RESULTADO.
print(fact)