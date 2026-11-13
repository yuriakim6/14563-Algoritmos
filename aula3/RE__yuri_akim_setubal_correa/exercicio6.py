#Exercício6
#Crie um programa que peça ao usuário para digitar três palavras. O programa deve exibir 
#as palavras ordenadas em ordem alfabética crescente.
palavra1 = input("Digite a primeira palavra: ").strip().lower()
palavra2 = input("Digite a segunda palavra: ").strip().lower()
palavra3 = input("Digite a terceira palavra: ").strip().lower()
if palavra1 < palavra2 and palavra1 < palavra3:
    print(palavra1, palavra2, palavra3)
elif palavra2 < palavra1 and palavra2 < palavra3:
        print(palavra2, palavra1, palavra3)
elif palavra3 < palavra1 and palavra3 < palavra2:
        print(palavra3, palavra2, palavra1)
elif palavra3 < palavra2 and palavra3 < palavra1:
        print(palavra2, palavra3, palavra1)
elif palavra3 < palavra1 and palavra1 < palavra2:
        print(palavra3, palavra1, palavra2)
else:
        print(palavra3, palavra2, palavra1)