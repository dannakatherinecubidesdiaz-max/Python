class CuentaBancaria:
    def __init__(self, titular:str, saldo_inicial:float):
      self.titular:str = titular
      self.saldo_inicial:float = saldo_inicial

    #METODO: Una acciòn. Nota còmo recibe 'self' y luego los paràmetros ùtiles.
    def depositar(self, cantidad: float)-> None:
       self.saldo_inicial += cantidad
       print(f"Dèposito exitoso. Nuevo saldo de {self.titular}: {self.saldo}")

    def retirar(self, cantidad:float)->None:
       if cantidad > self.saldo:
          print(f"Error {self.titular} no tiene fondos suficientes.") 
       else:
          self.saldo -= cantidad
          print(f"Retiro exitoso. Saldo restante: ${self.saldo}")

#Creando y manipulando objetos
cuenta_ana = CuentaBancaria("Ana Lòpes",5000.0)

cuenta_ana.depositar(20000.0)
cuenta_ana.retirar(100000.0) #Deberia arrojar el error de fondos
cuenta_ana.retirar(15000.0)
