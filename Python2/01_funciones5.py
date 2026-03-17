def es_mayor_de_edad(edad: int) -> bool:
    """Retorna True si la edad es >= 18, de lo contrario False"""
    return edad >= 18

# Probando la función dentro de un if
edad = int(input("Ingresa tu edad: "))

if es_mayor_de_edad(edad):
    print("Es mayor de edad")
else:
    print("Es menor de edad")
