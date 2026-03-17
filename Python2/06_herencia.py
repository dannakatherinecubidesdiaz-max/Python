#1. CLASE PADRE (Superclase)
class Empleado:
    def __init__(self, nombre:str, salario:float):
        self.nombre: str = nombre
        self.salario: float = salario
    def trabajar(self)-> None:
        print(f"{self.nombre} està cumpliendo su horario regular.")

#2. CLASE HIJO (subclase) - hereda todo de empleado pasandolo por parentesis
class Desarrollador(Empleado):
    def programar(self)->None:
        print(f"{self.nombre} està escribiendo còdigo Python.")

#3. CLASE HIJO CON POLIMORFISMO
class Gerente(Empleado):        
    #Sobrescribir el metodo del Padre
    def trabajar(self)->None:
        print(f"{self.nombre} esta en una reunion estrategica.")

#Pruebas de campo 
dev = Desarrollador("Carlos",3500.0)
jefe = Gerente("Ana",6000.0)

dev.trabajar() #Sube a RAM y usa el metodo del Padre
dev.programar() #Usa su mètodo propio

jefe.trabajar() # Usa su propio mètodo sobrescrito (Polimorfismo)