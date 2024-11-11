#Escribir una función que convierta un número decimal en binario y otra que 
#convierta un número binario en decimal.


def binario_a_decimal():
    numero_binario = input("Introduzca un número binario: ")
    numero_decimal = int(numero_binario, 2)
    return numero_decimal

print(binario_a_decimal())

def decimal_a_binario():
    numero_decimal = int(input("Introduzca un número en decimal: "))
    numero_binario = bin(numero_decimal)[2:]
    return numero_binario

print(decimal_a_binario())

"""
Este código tiene dos funciones para convertir números de
binario a decimal y viceversa. La función binario_a_decimal() pide al usuario
un número binario pero esta estará como cadena asi que lo convierte en entero
y transforma el binario a decimal usando
int(numero_binario, 2). int lo conviente en entero la variable numero_binario
y el dos hace que este en base 2 

La función decimal_a_binario() pide al usuario un número decimal, lo
convierte a binario usando bin(numero_decimal)[2:]  y para eliminar el
el 0b  que añade la función bin() y da el número binario
como cadena.

Al final se imprime el resultado de cada conversión con las
funciones y mostrando los valores convertidos.
"""


























"""
otro método 
def binario_a_decimal(binario):
    
    digitos = [int(d) for d in binario]
    decimal = 0
    longitud = len(digitos)
    for i in range(longitud):
        digito = digitos[i]
        potencia = longitud - i - 1
        valor = digito * (2 ** potencia)
        decimal += valor
    return decimal
binario = input("Introduce un número binario: ")

"""