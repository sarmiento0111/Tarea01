#Ejercicio 01
#Ejercicio 02
#Ejercicio 03
#Ejercicio 04
def factorialRecursivo(n):
    if n==0:
        rsp=1
    else:
        rsp=n*factorialRecursivo(n-1)
    return rsp
print("El factorial es: ",factorialRecursivo(4))
print("***********************")

#Ejercicio 05
def fibonacci(n):
    if n == 0:
        rsp=0
    else:
      if n == 1:
        rsp=1
      else:
        rsp=fibonacci(n-1) + fibonacci(n-2)
    return rsp
print("La sucecion de Fibonacci es : ",fibonacci(6))
print("***********************")

#Ejercicio 06
#Ejercicio 07
#Ejercicio 08
def potencia(base,potencia):
    if potencia==0:
        rpt=1
    else:
        rpt=base**potencia
    return rpt
print("El resultado de la operacion es: ",potencia(3,2))
print("***********************")

#Ejercicio 09
def sumaRecursivo(a,b):
    #suma=0
    for i in range(b):
        a+=1
    return a
print("La suma es de: ",sumaRecursivo(4,3))
print("***********************")

#Ejercicio 10
print("¿Cuáles son las principales ventajas \n de la programación recursiva en Python?")
print("""
-No es necesario definir la secuencia de pasos exacta para resolver el problema.
-Una tarea compleja se puede dividir en subproblemas más simples mediante la recursividad.
-La generación de secuencias es más fácil con la recursividad que con algunas iteraciones anidadas.
""")