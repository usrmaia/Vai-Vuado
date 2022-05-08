import bd_vai_vuado

bd = bd_vai_vuado.BD()
id_adm_empresa = 1

def visualizarProdutosDoAdm(id_adm_empresa):
    produtos = bd.visualizarProdutosDoAdm(id_adm_empresa)

    for produto in produtos:
            print(f"1. ID: {produto[0]}")
            print(f"2. {produto[2]}")
            print(f"3. {produto[3]}")
            print(f"4. {produto[4]}")
            print(f"5. {produto[5]}")
            print(f"6. {produto[6]}")
            print("")

def exibirInformacoesDeProduto(produto, mensagem):
    print(f"""
        1. {produto[0]}
        2. {produto[1]}
        3. {produto[2]}
        4. {produto[3]}
        5. {produto[4]}
        {mensagem}
    """)