#Faça um programa que crie uma lista com 10 números inteirosfornecidos pelo usuário. Após criar a lista, o programa deveráimprimir:
# O maior elemento da lista
# O menor elemento da lista
# A soma de todos os elementos da lista
# Os elementos ímpares
# Os elementos maiores do que 18


lista_original = []
i = 0
soma = 0 
print("Digite 10 valores inteiros seguidos:") 
while i <= 9: 
    lista_usuario = int(input())
    lista_original.append(lista_usuario)
    soma += lista_usuario
    i+=1

i = 0
print("Lista original:" , end=' ')
while i < len(lista_original):
    print(lista_original[i], end=' ') 
    i+=1

i = 0
maior = lista_original[0]
while i < len(lista_original): 
    if lista_original[i] > maior:
        maior = lista_original[i]
    i+=1
print() 
print(f"Maior elemento da lista = {maior}")

i = 0
menor = lista_original[0]
while i <len(lista_original):
    if lista_original[i] < menor:
        menor = lista_original[i]
    i+=1
print(f"Menor elemento da lista = {menor}")

print(f"A soma de todos os elementos dessa lista resulta em = {soma}")

i = 0
print("Imprimindo os elementos ímpares:")
while i < len(lista_original):
    if lista_original[i] % 2 != 0:
         print(lista_original[i], end=' ')
    i+=1

i = 0
print()
print("Imprimindo os números maiores que 18:")
while i <= 9:     
    if lista_original[i] > 18:
        print(lista_original[i], end=' ')
    i+=1
