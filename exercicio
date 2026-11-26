print(".: Sistema de Notas :.")

notas=[] #atribui vetor a variavel notas

nome = input("Digite o nome do aluno:") # ler valor através do console

for i in range(4): #laço de repetição de 4 voltas
    #variavel nota recebe valor decimal 
    nota = float(input(f"Digite a {i+1}ª nota:"))
    notas.append(nota) #add nota ao final do vetor notas

freq = float(input("Digite a freq. do aluno:"))

#sum soma notas e len pega o tamanho do vetor
media = sum(notas) / len(notas) 

# avaliar resultado final com média e freq.
if media >= 7 and freq >= 75:
    resultado = "aprovado"
elif freq < 75:
    resultado = "reprovado por falta"
else:
    resultado = "reprovado por nota"

print("\n--- Resultado Final ---")
print(f"Aluno: {nome}")
print(f"Média: {media:.2f}")
print(f"Frequência: {freq:.1f}%")
print(f"Situação final: {resultado}")