class Producto:
    def __init__(self, nombre:str, precio:float, stock:int):
        self.nombre:str=nombre
        self.precio:float=precio
        self.stock:int=stock

    def vender(self, cantidad:int)-> None:
        try:
         if cantidad > self.stock:
                # Lanzamos un error intencional si no hay suficiente stock

            raise ValueError ("stock insuficiente")
            self.stock -= cantidad
            print(f"Venta exitosa: {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}")
        except ValueError as e:
            print(f"Advertencia{e}")

#Clase Heredada
class ProductoPerecedero(Producto):
    def __init__(self, nombre: str, precio: float, stock: int, dias_vencimiento: int) -> None:
        super().__init__(nombre, precio, stock)  # Llamada al constructor de Producto
        self.dias_vencimiento = dias_vencimiento


# Ejemplo de uso
tomate = Producto("Tomate", 2.5, 12)
tomate.vender(10)
tomate.vender(4)

leche = ProductoPerecedero("Leche", 3.0, 20, 7)
print(f"{leche.nombre} vence en {leche.dias_vencimiento} días")
leche.vender(5)

