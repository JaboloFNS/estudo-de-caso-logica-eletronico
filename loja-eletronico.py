import os

def limpar_tela():
    os.system ("cls" if os.name == "nt" else "clear")
    

def menu_selecionado(opcao_selecionada):
    if opcao_selecionada == 1:
        print("-------------------------------------")
        print("--- Acessando Estoque Disponível ----")
        print("-------------------------------------")
    elif opcao_selecionada == 2:
        print("-------------------------------------")
        print("--------- Adicionar Produto ---------")
        print("-------------------------------------")
    elif opcao_selecionada == 3:
        print("-------------------------------------")
        print("---- Atualizar Produto Existente ----")
        print("-------------------------------------")
    elif opcao_selecionada == 4:
        print("-------------------------------------")
        print("---------- Excluir Produto ----------")
        print("-------------------------------------")
    elif opcao_selecionada == 0:
        print("-------------------------------------")
        print("-------- Operação Encerrada ---------")
        print("-------------------------------------")
        exit(0)
    else:
        print("-------------------------------------")
        print("--------- Operação inválida ---------")
        print("---------- Tente Novamente ----------")


def exibir_menu():
    print("-------------------------------------")
    print("----- Eletrohits Amazing Store ------")
    print("-------------------------------------")
    print("------------ Estoque ----------------")
    print("1 - Visualizar estoque")
    print("2 - Adicionar Produto")
    print("3 - Atualizar Produto Existente")
    print("4 - Excluir Produto")
    print("0 - Sair do Sistema")
    opcao_selecionada = int(input("Digite o código da opção desejada:"))
    limpar_tela()
    menu_selecionado(opcao_selecionada)
    exibir_menu()

exibir_menu()

