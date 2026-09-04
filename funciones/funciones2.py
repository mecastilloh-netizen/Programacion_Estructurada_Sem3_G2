#Sumar 2 Numeros
def sumar(num1, num2):
    return num1 + num2

def restar(num1 = 0, num2 = 0):
    return num1 - num2
def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "El segundo valor debe ser mayor que 0"


#suma
suma = sumar(15, 17)
print(suma)

#resta
resta = restar(num1 = 6, num2 = 2)
print(resta)

resta = restar(8)
print(resta)

multiplicacion = multiplicar(5, 2)
print(multiplicacion)

division = dividir(10, 2)
print(division)