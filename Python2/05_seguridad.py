class SistemaSeguridad:
    def __init__(self, pin_acceso: int):
        self.usuario: str ="Admin" #Pùblico
        #Atributo Privado (Fuerte) usando doble guion bajo
        self.__pin_secreto: int = pin_acceso
        self._alarma_activada: bool = True 
    # Método "Setter" (Puerta de acceso controlada) 
    def desactivar_alarma (self, intento_pin: int) -> None: 
        if intento_pin == self.__pin_secreto: 
           self.__alarma_activada = False
           print("Alarma desactivada.")
        else: 
           print("INTRUSO DETECTADO. Llamando a la policía.") 
casa_central = SistemaSeguridad (1234) 
# print(casa_central.__pin_secreto) -> ESTO ARROJARÁ UN ERROR DE ATRIBUTO 
casa_central.desactivar_alarma (9999) # Rechazado por la lógica del método 
casa_central.desactivar_alarma (1234) # Aceptado 
