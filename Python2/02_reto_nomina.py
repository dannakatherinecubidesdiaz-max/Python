# Calculadora de Nómina Tipada: Crea un script 
# 02_reto_nomina.py . Escribe una función calcular_salario_neto(salario_base: 
# float, bonificacion: float = 0.0) -> float que calcule el salario final restando un 
# 8% de salud y pensión, y sumando la bonificación. La bonificación debe ser cero por 
# defecto. El instructor validará en vivo tu comprensión del 'return', el tipado y el scope local.


def calcular_salario_neto(salario_base: float, bonificacion: float = 0.0) -> float:
    # 8% de salud y pensión
    descuento: float = salario_base * 0.08
    
    # cálculo del salario neto
    salario_final: float = salario_base - descuento + bonificacion
    
    return salario_final

# Ejemplo de uso
salario = calcular_salario_neto(3000000.0, 350000.0)
print(f"Salario neto: {salario}")
