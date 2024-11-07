#!/usr/bin/env python
print(""" $$$$$$\   $$$$$$\  $$\       $$$$$$\  $$\   $$\ $$\        $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  
$$  __$$\ $$  __$$\ $$ |     $$  __$$\ $$ |  $$ |$$ |      $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$ /  \__|$$ /  $$ |$$ |     $$ /  \__|$$ |  $$ |$$ |      $$ /  $$ |$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ /  $$ |
$$ |      $$$$$$$$ |$$ |     $$ |      $$ |  $$ |$$ |      $$$$$$$$ |$$ |  $$ |$$ |  $$ |$$$$$$$  |$$$$$$$$ |
$$ |      $$  __$$ |$$ |     $$ |      $$ |  $$ |$$ |      $$  __$$ |$$ |  $$ |$$ |  $$ |$$  __$$< $$  __$$ |
$$ |  $$\ $$ |  $$ |$$ |     $$ |  $$\ $$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
\$$$$$$  |$$ |  $$ |$$$$$$$$\\$$$$$$  |\$$$$$$  |$$$$$$$$\ $$ |  $$ |$$$$$$$  | $$$$$$  |$$ |  $$ |$$ |  $$ |
 \______/ \__|  \__|\________|\______/  \______/ \________|\__|  \__|\_______/  \______/ \__|  \__|\__|  \__|
                                                                                                             
                                                                                                             
                                                                                                             
""")

def calculator():
    print("Bienvenido a la Calculadora de Python")
    print("Selecciona la operación a realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    choice = input("Ingresa el número de la operación (1/2/3/4): ")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if choice == '1':
        result = num1 + num2
        print(f"El resultado de {num1} + {num2} es: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"El resultado de {num1} - {num2} es: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"El resultado de {num1} * {num2} es: {result}")
    elif choice == '4':
        if num2 == 0:
            print("Error: No se puede dividir por cero")
        else:
            result = num1 / num2
            print(f"El resultado de {num1} / {num2} es: {result}")
    else:
        print("Opción inválida. Por favor, selecciona una operación válida.")

if __name__ == "__main__":
    calculator()
