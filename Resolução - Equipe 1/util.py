import bd_vai_vuado

bd = bd_vai_vuado.BD()
id_adm_empresa = 1

def visualizarProdutosDoAdm(id_adm_empresa):
    produtos = bd.visualizarProdutosDoAdm(id_adm_empresa)

    for produto in produtos:
            print(f"1. ID do produto: {produto[0]}")
            print(f"2. Nome do produto: {produto[2]}")
            print(f"3. Categoria do produto: {produto[3]}")
            print(f"4. Medidas do produto: {produto[4]}")
            print(f"5. Imagem do produto: {produto[5]}")
            print(f"6. Descrição do produto: {produto[6]}")
            print("")