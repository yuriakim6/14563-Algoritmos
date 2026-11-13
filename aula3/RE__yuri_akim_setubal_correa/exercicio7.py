#Exercício7
#Crie um programa que compare duas palavras em relação à sua ordem lexicográfica e 
#informe se a primeira palavra é maior ou menor que a segunda.
palavra1 = input("Informe a primeira palavra: ")
palavra2 = input("Informe a segunda palavra: ")
if palavra1 < palavra2:
    print(f"{palavra1} é maior que {palavra2}")
else:
    print(f"{palavra1} é menor que {palavra2}")