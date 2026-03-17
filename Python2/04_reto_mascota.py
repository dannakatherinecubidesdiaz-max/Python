# 04_reto_mascota.py . Crea una clase MascotaVirtual. Su constructor debe recibir un 
# nombre: str y arrancar con un atributo energia: int = 10. Crea un método 
# jugar (self) -> None que reste 3 de energía y un método dormir (self) -> None que 
# sume 5 de energía. Ambos métodos deben imprimir el estado actual. Instancia una 
# mascota y hazla jugar y dormir. El instructor evaluará tu correcta comprensión del 
# modificador self. 

class MascotaVirtual:
    def __init__(self, nombre:str, energia: int = 10):
      self.nombre:str=nombre
      self.energia:int=energia

    def jugar(self) -> None:
        self.energia -= 3
        print(f"{self.nombre} ha jugado. Energia actual: {self.energia}")

    def dormir(self) -> None:
        self.energia += 5
        print(f"{self.nombre} ha dormido. Energia actual: {self.energia}")


# Ejemplo de uso
mascota = MascotaVirtual("Firulais")
mascota.jugar()   # Resta 3 de energía
mascota.dormir()  # Suma 5 de energía
