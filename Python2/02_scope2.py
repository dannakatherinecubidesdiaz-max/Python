#Si el usuario no envio el paràmetro 'moneda', usamos "COP" por defecto
def convertir_moneda(cantidad: float, moneda: str = "COP") ->None:
    print(f"Procesando transacciòn:{cantidad} en moneda {moneda}")

convertir_moneda(5000.0, "USD") #Reemplazo el valor por defecto
convertir_moneda(150000.0)  #Como no enviamos moneda, usa "COP"