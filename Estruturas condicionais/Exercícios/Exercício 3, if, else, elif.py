n1 = int(input("Escolha um número:"))
n2 = int(input("Escolha um número distinto do anterior:"))
n3 = int(input("Digite um número diferente dos anteriormente escolhidos:"))
if n1 > n2:
    if n2 > n3:
        print(n3,n2,n1)
    if n3 > n1:
        print(n2,n1,n3) 
elif n2 > n1:
    if n1 > n3:
        print(n3,n1,n2) 
    if n2 < n3:
        print(n1,n2,n3)
elif n3 > n1:
    if n2 > n3:
        print(n1,n3,n2)
else:
    print(n2,n3,n1)