a = int(input("Escolha um valor inteiro para a variável: "))
b = int(input("Escolha um valor inteiro para a variável: "))
c = int(input("Escolha um valor inteiro para a variável: "))
delta = (b**2) - (4*a*c)

if delta < 0:
    print("As raízes dessa equação não existem.")
elif delta > 0:
    x1 = (- b + (delta**0.5)) / (2*a)
    x2 = (- b - (delta**0.5)) / (2*a)
    x1_arredondado = round(x1, 2)
    x2_arredondado = round(x2, 2)
    print(f"As raízes da função são: X1 = {x1_arredondado} e X2 = {x2_arredondado}")
else:
    x = (- b + (delta**0.5)) / (2*a)
    x_arredondado = round(x, 2)
    print(f"A raiz da função é x = {x_arredondado}")
