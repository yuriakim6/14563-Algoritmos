# Desenvolva um programa em Python que receba o nome de um produto e armazene em uma lista as quantidades vendidas nos últimos 4 meses.

# O programa deve:

# Solicitar o nome do produto.
# Receber as quantidades vendidas em cada um dos 4 meses e armazená-las em uma lista.
# Calcular a média de vendas do período.
# Receber a quantidade atual em estoque.
# Exibir o nome do produto, a média de vendas e o estoque atual.
# Classificar a situação do estoque de acordo com as regras:
# Estoque Adequado: média de vendas ≤ estoque atual.
# Estoque Baixo: média de vendas > estoque atual e estoque atual > 0.
# Produto Esgotado: estoque atual = 0.
# Apresentar a situação final do produto.

produto = input("Digite o nome do produto: ")#O comando input() captura o nome do produto.
vendas = []
for i in range (4):#um loop for repete
    venda = int(input(f"Digite a quantidade vendida no mês {i +1}: "))
    vendas.append(venda)#append adiciona o valor ao final do vetor

media_vendas = sum(vendas) / len(vendas)#sum(vendas) soma todos os elementos da lista e len(vendas)quantidade de valor e ( / ) divide pela quantidade
estoque = int(input("Digite a quantidade atual do estoque: "))
#if-elif-else verifica as regras de negócio
if estoque == 0:#Verifica primeiro se o estoque é exatamente zero
    resultado = "Produto Esgotado"
elif media_vendas <= estoque:#operador <= verifica se a média de vendas é menor ou igual ao estoque
    resultado = "Estoque Adequado"
else:#significa que o estoque é maior que zero, mas é menor do que a média de vendas.
    resultado = "Estoque Baixo"

print("\n--- Relatório do Produto ---")#\n (Quebra de linha),No código, ele é usado para pular uma linha antes de exibir o título do relatório
print(f"Nome do Produto: {produto}")
print(f"Média de Vendas: {media_vendas:.2f}")#:.2f (Formatação decimal), Ele formata o número para que seja exibido sempre com duas casas após a vírgula (por exemplo, transformando o número 15 em 15.00)
print(f"Estoque Atual: {estoque}")
print(f"Situação do Estoque: {resultado}")