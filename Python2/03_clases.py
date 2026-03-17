#1. EL MOLDE:La Clase(Por convenciòn, empieza con Mayùscula)
class Servidor:

    #2.EL CONSTRUCTOR: Se ejecuta automàticamente al instanciar.
    def __init__(self, nombre:str, ip:str, ram_gb:int):
        #3. ATRIBUTOS: Variables que le pertenecen solo a este objeto en la RAM
        self.nombre:str = nombre
        self.ip:str = ip
        self.ram:int = ram_gb
        self.estado:str = "Apagado" #Valor inicial por defecto

#4. INSTANCIACIÒN: Construyendo los objetos fisicos en RAM
server_ventas = Servidor("Ventas-01","192.168.1.10",16)
server_bd = Servidor("Database-Main","10.0.0.5",64)

#5. Accediendo a la informacion especifica usando el puntero del objeto
print(f"El servidor {server_ventas.nombre} tiene {server_ventas.ram}GB de RAM.")
print(f"El servidor {server_bd.nombre} actualmente està: {server_bd.estado}") 