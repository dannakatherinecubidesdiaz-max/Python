class CajeroAutomatico:
    def __init__(self):
        self.efectivo_disponible: float = 10000.0

    def solicitar_retiro(self)->None:
        print("---Bienvenido al Cajero---")
        #Bloque TRY: "Intenta hacer esto, para esta alerta"
        try:
            monto_str:str=input("Ingresa la cantidad a retirar (solo numeros)")
            #Si el usuario ingresa letras, esta conversiòn generarà un ValueError
            monto:float=float(monto_str)

            #Si el usuario lanza cero, lanzaremos nuestra propia excepciòn logica
            if monto == 0:
                raise ValueError("No puede retirar cero pesos.")

            #Operacion matemàtica (riesgo de dividir por cero, etc.)
            self.efectivo_disponible -= monto
            print(f"Retiro exitoso. Quedan {self.efectivo_disponible} en el cajero")

        #Bloque EXCEPT: "Si ocurre este error especifico, no te apagues has esto"
        except ValueError as e:
            print(f"ERROR DE FORMATO: Usted ingreso caracteres invalidos. {self.efectivo_disponible}")
            
        #Un Exception general captura cualquier otro error inesperado (como un f)
        except Exception as e:
            print(f"ERROR CRITICO DESCONOCIDO: Contacte soporte. Detalles: {self.efectivo_disponible}")
        #Bloque FINALLY:"Se ejecuta SIEMPRE, haya ocurrido un error o no"    
        finally:
            print("Expulsando tarjeta...Gracias por utilizar nuestra red./n")

#Prueba
mi_cajero= CajeroAutomatico()
#Intento ingresar letras como "Hola" en vez de numeros para probar la resiliencia            
mi_cajero.solicitar_retiro()