numero = int(input("Escolha um número:"))
x = 0
y = numero*x
while y <= numero*9:
    print(f"{numero} x {x} = {y}")
    x = x + 1
    y = numero*x
