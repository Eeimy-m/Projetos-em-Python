A = int(input("Dê valor ao lado A de um triângulo:"))
B = int(input("Dê valor ao lado B de um triângulo:"))
C = int(input("Dê valor ao lado C de um triângulo:"))
if A + B < C:
    print("Esse triângulo não existe!")
elif A + C < B:
    print("Esse triângulo não existe!")
elif B + C < A:
    print("Esse triângulo não existe!")
else: 
    if A == B:
        if B == C:
            print("O triângulo escolhido é equilátero.")
        if B != C:
            print("O triângulo escolhido é isósceles.")
    else:
        print("O triângulo escolhido é escaleno.")
