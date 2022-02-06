pesos = input("Ingresa cuantos pesos mexicanos tienes: ")
pesos = float(pesos)
valor_dolar = 20.31
dolares = round(pesos / valor_dolar,3)
conversion_dolar = str(dolares)
print("Tienes: " + conversion_dolar + " dolares.")