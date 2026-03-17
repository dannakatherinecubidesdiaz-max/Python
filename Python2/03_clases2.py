#Crea una clase Vehiculo
class Vehiculo:
    def __init__(self, marca: str, modelo: str, año: int):
        self.marca = marca
        self.modelo = modelo
        self.año = año

 #Crea dos objetos diferentes e imprime sus datos

vehiculo1 = Vehiculo("Toyota", "Corolla", 2020)
vehiculo2 = Vehiculo("Ford", "Lamborgini", 2023)

# Imprimir sus datos
print(f"Vehículo 1: {vehiculo1.marca}, {vehiculo1.modelo}, {vehiculo1.anio}")
print(f"Vehículo 2: {vehiculo2.marca}, {vehiculo2.modelo}, {vehiculo2.anio}")
