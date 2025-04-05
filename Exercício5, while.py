'''Definir se o valor escolhido é primo ou não.'''

num = int(input("Escolha um valor inteiro maior que um:"))
divisor = 2
primo = True
while divisor < num:
    if num % divisor == 0:
        primo = False
    divisor+=1
if primo == True:
    print("Número primo.")
else:
    print("Número não primo.")