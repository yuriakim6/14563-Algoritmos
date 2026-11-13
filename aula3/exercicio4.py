#Exercício
#Crie um programa que peça ao usuário para digitar duas palavras. O programa deve 
#comparar o comprimento das duas palavras e dizer qual delas tem mais caracteres ou se 
#elas têm o mesmo número de caracteres.
palavra1 = input("Digite a primeira palavra: ").strip()
palavra2 = input("Digite a segunda palavra: ").strip()
if len (palavra1) > len (palavra2):
    print(F"A palavra '{palavra1}' é maior em caracteres")
elif len (palavra1) > len (palavra2):
    print(F"A palavra '{palavra2}' é maior em caracteres")
else:
    print("As dua palavras são iguais em número de caracteres.")