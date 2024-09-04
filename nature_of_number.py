# Define función para evaluar si el numero es par o impar, y si es positivo o negativo
def nature_of_number(number):
    if number % 2 == 0:
        if number > 0:
            print(f"El numero {number} par y es positivo")
        elif number < 0:
            print(f"El numero {number} par y es negativo")
        else:
            print(f"El numero {number} es par")
    else: 
        if number > 0:
            print(f"El numero {number} impar y es positivo")
        elif number < 0:
            print(f"El numero {number} impar y es negativo")
        else:
            print(f"El numero {number} es impar")

# Muestra opción al usuario para permitirle ingresar un número.
# Si no ingresa un entero o flotate advertirá el error y pedirá nuevamente el número
def input_prompt():
    try:
        number = float(input("Ingrese un número para evaluar: "))
        nature_of_number(number)
    except Exception:
        print("Ingresó una entrada no valida, por favor indique un número para evaluar")
        input_prompt()

# Añade convención
if __name__ == "__main__":
    input_prompt()
