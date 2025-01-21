import os

estoque = { "1":{ "SKU":"TE001", "Descrição":  "Teclado Mecânico Preto Switch Azul RGB", "Preço (R$)": 190.00, "Quantidade": 37},
            "2":{ "SKU":"TE002", "Descrição":  "Teclado Mecânico Branco Switch Azul RGB", "Preço (R$)": 205.00, "Quantidade": 14},
            "3":{ "SKU":"TE003", "Descrição":  "Teclado Mecânico Branco Switch Marrom RGB", "Preço (R$)": 155.00, "Quantidade": 48},
            "4":{ "SKU":"TE004", "Descrição":  "Teclado Mecânico Preto Switch Marrom RGB", "Preço (R$)": 140.00, "Quantidade": 9},
            "5":{ "SKU":"MOS01", "Descrição":  "Mouse RGB Gamer 12 Botões Preto 20000 DPI", "Preço (R$)": 90.00, "Quantidade": 112},
            "6":{ "SKU":"MOS02", "Descrição":  "Mouse RGB Gamer 12 Botões Branco 20000 DPI", "Preço (R$)": 110.00, "Quantidade": 25}
}
contador_de_ids = len(estoque) + 1

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

def adicionar_produto():
    global contador_de_ids
    print ("Vamos adicionar um novo produto ao estoque, para isso ensira algumas informações:")
    sku_novo = str(input("Ensira o código interno do produto (SKU): "))
    descricao_novo = str(input("Ensira a descrição detalhada de seu produto: "))
    preco_novo = float(input("Ensira o preço padrão do Produto (R$): "))
    quantidade_novo = int(input("Ensira a quantidade que estará disponível em estoque: "))

    produto_novo = {"SKU": sku_novo, "Descrição": descricao_novo, "Preço (R$)": preco_novo, "Quantidade": quantidade_novo}

    estoque [ str(contador_de_ids)] = produto_novo
    if estoque [ str(contador_de_ids)] == produto_novo:
        print ("Produto adicionado com sucesso")
        contador_de_ids += 1
    else:
        print ("Houve um erro, tente novamente mais tarde")
    pause()

def atualizar_produto():
    id_para_alterar = input("Qual o ID do produto que deseja alterar?")
    if id_para_alterar in estoque:
        produto_para_alterar = estoque[id_para_alterar]
        print("-----------------------------------------------------------------")
        print("Produto Selecionado:")
        print(f"ID: {id_para_alterar}")
        for chave, valor in produto_para_alterar.items():  
            print(f"{chave}:{valor}")
        print ("O que deseja alterar?")
        print ("1 - SKU")
        print ("2 - Descrição")
        print ("3 - Preço")
        print ("4 - Quantidade")
        print ("0 - Sair")
        opcao_alterar = int(input("Digite a opção desejada aqui: "))
        if opcao_alterar == 1:
            valor_novo = str(input("Digite a nova SKU: "))
            estoque[id_para_alterar]["SKU"] = valor_novo
        elif opcao_alterar == 2:
            valor_novo = str(input("Digite a nova Descrição: "))
            estoque[id_para_alterar]["Descrição"] = valor_novo
        elif opcao_alterar == 3:
            valor_novo = float(input("Digite o novo preço (R$): "))
            estoque[id_para_alterar]["Preço"] = valor_novo
        elif opcao_alterar == 4:
            valor_novo = str(input("Digite o valor novo da SKU:"))
            estoque[id_para_alterar]["Quantidade"] = valor_novo
        elif opcao_alterar == 0:
            limpar_tela()
            menu_selecionado()
    else:
        print("Produto não encontrado. ID inexistente.")

    

def excluir_produto():
    produto_excluir = str(input("Digite a ID do produto que deseja excluir: "))
    del estoque[produto_excluir]
    produto_check = False
    for chave in estoque:
        if chave == produto_excluir:
            produto_check = True
            break
    if produto_check == True:
        print ("Houve um erro ao excluir o produto. Tente novamente mais tarde!")
    else:
        print (f"ID: {produto_excluir} - excluído com sucesso")

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
        acessar_estoque()
        adicionar_produto()
    elif opcao_selecionada == 3:
        print("-------------------------------------")
        print("---- Atualizar Produto Existente ----")
        print("-------------------------------------")
        acessar_estoque()
        atualizar_produto()
        pause()
        limpar_tela()
    elif opcao_selecionada == 4:
        print("-------------------------------------")
        print("---------- Excluir Produto ----------")
        print("-------------------------------------")
        acessar_estoque()
        excluir_produto()
        resposta = input ("Visualizar estoque atualizado? [s/n] ")
        if resposta.lower() == 's':
            acessar_estoque()
        pause()
        limpar_tela()

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

