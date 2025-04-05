Valor = float(input("Indique o valor do produto: "))
if Valor < 0:
    print("O valor indicado não é válido! Tente novamente.")
else:
    if Valor < 100:
        print(f"O valor a ser pago é R${Valor * 95/100}")
    elif Valor > 100 and Valor < 200:
        print(f"O valor a ser pago é R${Valor * 90/100}")
    elif Valor > 200:
        print(f"O valor a ser pago é R${Valor * 80/100}")