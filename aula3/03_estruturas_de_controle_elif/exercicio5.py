#Exercício5
#Crie um programa que peça ao usuário para digitar duas palavras (strings) e compare-as 
#em ordem alfabética. Exiba qual palavra vem primeiro na ordem alfabética.
palavra1 = input("Digite a primeira palavra: ").strip()
palavra2 = input("Digite a segunda palavra: ").strip()
if palavra1.lower < palavra2.lower:
    print(f"A palavra '{palavra1}' vem primeiro na ordem alfabética. ")
elif palavra1.lower < palavra2.lower:
    print(f"A palavra '{palavra2}' vem primeiro na ordem alfabética. ")
else:
    print("As duas palavras são iguais na ordem alfabética")