nota = 0
acmed = 0
rec = 0
rep = 0
med = 0
positivo = True

while positivo == True:
        nota = float(input("Informe a sua nota da avaliação:"))
        if nota < 0:
                positivo = False
        elif nota >= 0:
            if nota >= 6 and nota < 10: #O nota < 10 deve ser inserido para limitar notas maiores que 10
                acmed+=1
            elif nota >= 4 and nota < 6:
                rec+=1
            elif nota < 4:
                rep+=1
            med = med + nota
        else:
             print("Essa nota é inválida.") #Para que notas a cima de 10 não sejam consideradas na média final 

medfin = med/(acmed + rec + rep)
print(f"Pessoas com notas maiores ou iguais a 6: {acmed}")
print(f"Pessoas com notas entre 4 e 6: {rec}")
print(f"Pessoas com notas a baixo de 4: {rep}")
print(f"A média final das notas fornecidas é {medfin}")