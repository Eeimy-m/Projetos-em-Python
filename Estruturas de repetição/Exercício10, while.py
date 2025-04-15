n = int(input("Informe a quantidade de termos da série:"))
num = 1 
denom = 1 
soma = 0 #variável acumuladora 
while num <= n:
    if num < n:
        print(f'{num}/{denom} + ', end= '')
    else:
        print(f'{num}/{denom} = ' , end='')
    soma += num/denom
    num+=1
    denom+=2
print(soma)