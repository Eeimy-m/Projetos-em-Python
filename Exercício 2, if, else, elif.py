Idade = int(input("Indique aqui a sua idade:"))
if Idade < 16:
    print("Você ainda não é apto a votar.")
elif Idade <= 17:
    print("Seu voto é facultativo.")
elif Idade >= 18 and Idade <= 65:
    print("Seu voto é obrigatório!")
else:
    print("Você está dispensado.")