#Exercício1
#Crie um programa que peça ao usuário para digitar dois números.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"{numero1} é maior que {numero2}")
elif numero1 == numero2:
    print(f"{numero1} é igual a {numero2}")
elif numero1 < numero2:
    print(f"{numero1} é menor que {numero2}")
elif numero1 >= numero2:
    print(f"{numero1} é maior e igual a {numero2}")
elif numero1 <= numero2:
    print(f"{numero1} é menor e igual a {numero2}")
elif numero1 != numero2:
    print(f"{numero1} é diferente e igual a {numero2}")
else:
    print(f"{numero1} é menor que {numero2}")
print("-" * 30)

#Exercício2
#Crie um programa que peça ao usuário para digitar duas palavras (string)
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

if palavra1 > palavra2:
    print(f"{palavra1} é maior que {palavra2}")
elif palavra1 < palavra2:
    print(f"{palavra1} é menor que {palavra2}")
elif palavra1 == palavra2:
    print(f"{palavra1} é igual a {palavra2}")
elif palavra1 != palavra2:
    print(f"{palavra1} é diferente e igual a {palavra2}")
else:
    print(f"{palavra1} é menor que {palavra2}")
print("-" * 30)

#Exercício3
#Crie um programa que peça ao usuário para digitar um número e uma palavra (string).
numero = int(input("Digite um numero: "))
palavra = input("Divigite uma palavra: ")
numeroToString =  str(numero)
if numeroToString== palavra:
    print("Numero e palavra são iguais!")
else:
    print("São diferentes!")