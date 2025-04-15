num = int(input("Escolha um número inteiro:"))
quant_sub = 1
num_para_rep = num
fatorial = num - quant_sub
if num == 0:
    print("O fatorial de 0 é 1.")
elif num > 0:
    while fatorial > 0:
            num_para_rep = num_para_rep * fatorial
            quant_sub+=1
            fatorial = num - quant_sub
    print(f"{num}! = {num_para_rep}")
else:
     print("Fatoriais não são definidos para números negativos!")