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