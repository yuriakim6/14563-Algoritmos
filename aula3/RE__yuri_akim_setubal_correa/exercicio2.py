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
