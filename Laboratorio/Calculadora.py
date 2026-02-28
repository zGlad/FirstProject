"""
Calculadora Clásica en Python
Descripción: Programa de consola que realiza operaciones matemáticas básicas,
potencias, raíces, factoriales y promedios.
"""

# ==========================================
# DEFINICIÓN DE FUNCIONES (Lógica Matemática)
# ==========================================

def sumar(a, b):
    """Retorna la suma de dos números."""
    return a + b

def restar(a, b):
    """Retorna la diferencia entre dos números."""
    return a - b

def multiplicar(a, b):
    """Retorna el producto de dos números."""
    return a * b

def dividir(a, b):
    """Retorna el cociente. Nota: Puede lanzar ZeroDivisionError si b es 0."""
    return a / b

def elevar(a, b):
    """Retorna el primer número elevado a la potencia del segundo."""
    return a ** b

def raiz_cuadrada(a):
    """Calcula la raíz cuadrada usando el exponente 0.5."""
    return a ** 0.5

def raiz_cubica(a):
    """Calcula la raíz cúbica usando el exponente 1/3."""
    return a ** (1/3)

def porcentaje(a, b):
    """Calcula el b% de un número a."""
    return (a * b) / 100

def factorial(a):
    """Calcula el factorial de un número de forma recursiva."""
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)
    
def calcular_promedio(numeros):
    """Recibe una lista de números y retorna su promedio simple."""
    return sum(numeros) / len(numeros)


# ==========================================
# PROGRAMA PRINCIPAL (Interfaz de Usuario)
# ==========================================

def mostrar_menu():
    """Muestra las opciones disponibles en la consola."""
    print("\n" + "="*25)
    print("   CALCULADORA CLÁSICA")
    print("="*25)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Elevar")
    print("6. Raiz Cuadrada")
    print("7. Raiz Cubica")
    print("8. Porcentaje")
    print("9. Factorial")
    print("10. Calcular Promedio")
    print("0. Salir")

# Inicio del flujo
mostrar_menu()
opcion = int(input("\nSeleccione una opcion: "))

# Bucle de control: se mantiene activo mientras la opción esté en el rango [1, 10]
while 1 <= opcion <= 10:
    match opcion: 
        case 1: 
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("El resultado es: ", sumar(a, b))
        case 2:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("El resultado es: ", restar(a, b))
        case 3: 
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            print("El resultado es: ", multiplicar(a, b))
        case 4:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
            # Manejo básico de error por división entre cero
            if b != 0:
                print("El resultado es: ", dividir(a, b))
            else:
                print("Error: No se puede dividir entre cero.")
        case 5:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el número de potencia10: "))
            print("El resultado es: ", elevar(a, b))
        case 6:
            a = float(input("Ingrese el numero: "))
            print("El resultado es: ", raiz_cuadrada(a))
        case 7:
            a = float(input("Ingrese el numero: "))
            print("El resultado es: ", raiz_cubica(a))
        case 8:
            a = float(input("Ingrese el numero: "))
            b = float(input("Ingrese el porcentaje: "))
            print("El resultado es: ", porcentaje(a, b))
        case 9:
            a = int(input("Ingrese el numero: "))
            print("El resultado es: ", factorial(a))
        case 10:
            # Convierte la cadena de entrada en una lista de números flotantes
            entrada = input("Ingrese los numeros separados por espacios: ")
            numeros = list(map(float, entrada.split()))
            if numeros: # Verifica que la lista no esté vacía
                print("El promedio es: ", calcular_promedio(numeros))
            else:
                print("No se ingresaron números.")
        case _:
            print("Opcion no valida")
    
    # Actualización de la variable de control para evitar bucle infinito
    opcion = int(input("\nSeleccione una nueva opción (o 0 para salir): "))

print("\nGracias por usar la calculadora. ¡Hasta luego!")