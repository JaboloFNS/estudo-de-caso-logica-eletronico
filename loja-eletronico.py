import os

estoque = { "1":{ "SKU":"TE001", "Descrição":  "Teclado Mecânico Preto Switch Azul RGB", "Preço (R$)": 190.00, "Quantidade": 37},
            "2":{ "SKU":"TE002", "Descrição":  "Teclado Mecânico Branco Switch Azul RGB", "Preço (R$)": 205.00, "Quantidade": 14},
            "3":{ "SKU":"TE003", "Descrição":  "Teclado Mecânico Branco Switch Marrom RGB", "Preço (R$)": 155.00, "Quantidade": 48},
            "4":{ "SKU":"TE004", "Descrição":  "Teclado Mecânico Preto Switch Marrom RGB", "Preço (R$)": 140.00, "Quantidade": 9},
            "5":{ "SKU":"MOS01", "Descrição":  "Mouse RGB Gamer 12 Botões Preto 20000 DPI", "Preço (R$)": 90.00, "Quantidade": 112},
            "6":{ "SKU":"MOS02", "Descrição":  "Mouse RGB Gamer 12 Botões Preto 20000 DPI", "Preço (R$)": 90.00, "Quantidade": 112}
}


def limpar_tela():
    os.system ("cls" if os.name == "nt" else "clear")

def pause():
    input("Aperte Enter para voltar")

def acessar_estoque():
    for id, produto in estoque.items():
        print("-------------------------------------------------------------------------------")
        print(f"ID: {id}")
        for topico, valor_topico in produto.items():
            print (f"{topico}: {valor_topico}")
    

def menu_selecionado(opcao_selecionada):
    if opcao_selecionada == 1:
        limpar_tela()
        print("-------------------------------------")
        print("--- Acessando Estoque Disponível ----")
        print("-------------------------------------")
        acessar_estoque()
        pause()
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
        pause()


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

