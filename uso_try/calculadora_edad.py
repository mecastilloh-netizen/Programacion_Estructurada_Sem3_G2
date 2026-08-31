#CALCULAR EDAD DE UNA PERSONA Y DECIR SI ES MAYOR O MENOR DE EDAD
from datetime import date
from colorama import Fore, Style

try:
    año_nac = int(input("Dime en año en el que naciste: "))
    edad = date.today().year - año_nac
    if edad >= 18:
        print("Usted es mayor de edad.")
    else:
        print("Eres menor de edad.")

except ValueError:
    print(Fore.RED + "Ingrese un valor numerico." + Style.RESET_ALL)