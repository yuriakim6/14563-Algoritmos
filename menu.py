#criar menu de sistema que só encerra a app quando o usuário escolher

while (True):# (while(true))Cria um loop infinito que só para com 'break'
    print(" Menu")# (print)Exibe a opção
    print("1 - Cadrastrar")
    print("2 - Editar")
    print("3 - Deletar")
    print("4 - Exibir")
    print("9 - Sair")
    try:#(try) faz parte do sistema de tratamento de exceções (erros)
        op_menu = int(input("Digite a opção desejada: "))# (int(input))Lê a entrada do usuário e converte para número inteiro
    except ValueError:#(except)Se acontecer um erro no try, o programa não fecha; ele cai direto aqui para tratar o erro de forma amigável.
        print("Erro: opção inválida! Tente novamnete!" )
        continue

    if op_menu > 4 and op_menu < 9 or op_menu > 9 or op_menu < 1:
        print("Erro: opção de menu inválida! Tente novamente! ")
        continue

#o comando (match) e o (case) formam uma estrutura de correspondência de padrões
    match op_menu:# (match)Estrutura que escolhe uma ação baseada na variável
        case 1:
            print("Iniciar Cadastro")
        case 2:
            print("Iniciar Edição")
        case 3:
            print("Deletar Cadastro")
        case 4:
            print("listar Cadastro")

    if op_menu != 9:# (!=)Verifica se a opção digitada é diferente de 9
        continue# Pula de volta para o início do loop se não for 9
    else:# Se a opção for 9 (Sair)
        print("\nApp encerrada pelo ususário!\n")
        break# Encerra o loop e finaliza o programa