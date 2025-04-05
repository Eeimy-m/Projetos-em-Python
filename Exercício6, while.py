n1 = int(input("Escolha um número que represente a base de uma potência:"))
n2 = int(input("Escolha um número que represente o expoente:"))
exp = 1
base = n1
while exp <= n2:
    base = base * n1
    exp+=1
print(f"{n1}**{n2} = {base}")