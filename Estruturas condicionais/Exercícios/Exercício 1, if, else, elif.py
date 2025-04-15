n1 = int(input("Escolha um número:"))
n2 = int(input("Escolha um número:"))
n3 = int(input("Escolha um número:"))
n4 = int(input("Escolha um número:"))
n5 = int(input("Escolha um número:"))
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print(f"{n1} é o maior número entre os esclhidos.")
elif n2 > n3 and n2 > n4 and n2 > n5:
    print(f"{n2} é o maior número entre os escolhidos.")
elif n3 > n4 and n3 > n5:
    print(f"{n3} é o maior número entre os escolhidos.")
elif n4 > n5:
    print(f"{n4} é o maior número entre os escolhidos.")
else:
    print(f"{n5} é o maior número entre os escolhidos.")
    