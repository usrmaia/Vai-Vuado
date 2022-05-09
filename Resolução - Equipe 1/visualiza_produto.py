import bd_vai_vuado, util

class Visualiza():
    def __init__(self, id_adm_empresa, bd):
        self.nome = []
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa
        self.opcao = []

    def pesquisarProdutoPeloNome(self):

        self.nome = input("""

            0. Sair

        Informe um nome para pesquisar produtos: """)

        if self.nome == "0": self.opcao = "Sair"
    
    def visualizarProduto(self):

        produtos = util.retornarProdutosDoAdm(self.id_adm_empresa)

        for produto in produtos:

            nome_produto = produto[2]

            if self.nome in nome_produto:

                print(f"""

                    1. ID:          {produto[1]}
                    1. Nome:        {produto[2]}
                    2. Categoria:   {produto[3]}
                    3. Medidas:     {produto[4]}
                    4. Imagem:      {produto[5]}
                    5. Descrição:   {produto[6]}

                """)
    
if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    visualizar = Visualiza(id_adm_empresa, bd)
    visualizar.pesquisarProdutoPeloNome()