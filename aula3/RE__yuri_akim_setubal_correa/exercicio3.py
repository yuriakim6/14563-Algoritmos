#Exercício3
#Crie um programa que peça ao usuário para digitar um número e uma palavra (string).
numero = int(input("Digite um numero: "))
palavra = input("Divigite uma palavra: ")
numeroToString =  str(numero)
if numeroToString== palavra:
    print("Numero e palavra são iguais!")
else:
    print("São diferentes!")