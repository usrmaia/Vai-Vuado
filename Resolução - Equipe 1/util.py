import bd_vai_vuado

bd = bd_vai_vuado.BD()
id_adm_empresa = 1

def retornarProdutosDoAdm(id_adm_empresa):
    return bd.visualizarProdutosDoAdm(id_adm_empresa)

def retornarProdutoDoAdm(id_produto, id_adm_empresa):
    return bd.visualizarProduto(id_produto, id_adm_empresa)

def visualizarProdutosDoAdm(id_adm_empresa):

    produtos = bd.visualizarProdutosDoAdm(id_adm_empresa)

    print("Meus Produtos: ")
    for produto in produtos:
        print(f"""
                
                1. ID:          {produto[0]}
                2. Nome:        {produto[2]}
                3. Categoria:   {produto[3]}
                4. Medidas:     {produto[4]}
                5. Imagem:      {produto[5]}
                6. Descrição:   {produto[6]}
            
        """)

def visualizarProdutoDoAdm(id_produto):

    dados = bd.visualizarProduto(id_produto)
    dados = dados[0]

    print(f"""
            
            1. ID:          {dados[0]}
            2. Nome:        {dados[2]}
            3. Categoria:   {dados[3]}
            4. Medidas:     {dados[4]}
            5. Imagem:      {dados[5]}
            6. Descrição:   {dados[6]}
            0. Voltar
        
    """)

def exibirInformacoesDeProduto(produto, mensagem):
    print(f"""

                1. Nome:        {produto[0]}
                2. Categoria:   {produto[1]}
                3. Medidas:     {produto[2]}
                4. Imagem:      {produto[3]}
                5. Descrição:   {produto[4]}
                {mensagem}
                
    """)

def exibirMenuDeProdutoSimples(nome, categoria, medidas, imagem, descricao):
    print(f"""

                1. Nome:        {nome}
                2. Categoria:   {categoria}
                3. Medidas:     {medidas}
                4. Imagem:      {imagem}
                5. Descrição:   {descricao}
                0. Voltar

    """)

def exibirMenuDeProdutoCompleto(id_adm_empresa):

    print(f"""

                1. Nome:        {nome}
                2. Categoria:   {categoria}
                3. Medidas:     {medidas}
                4. Imagem:      {imagem}
                5. Descrição:   {descricao}
                0. Voltar

    """)

if __name__ == "__main__":
    visualizarProdutosDoAdm(1)