import bd_vai_vuado

class Visualizar():
    def __init__(self, id_adm_empresa, bd):
        self.nome = []
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa

    def pesquisarProdutoPeloNome(self):
        while(True):
            self.nome = input("Busque por algum produto pelo nome: ")
            produtos = self.bd.visualizarProdutosDoAdm(self.id_adm_empresa)

            for produto in produtos:
                if self.nome in produto[2]:
                    print(f"""
                        1. ID:          {produto[1]}
                        1. Nome:        {produto[2]}
                        2. Categoria:   {produto[3]}
                        3. Medidas:     {produto[4]}
                        4. Imagem:      {produto[5]}
                        5. Descrição:   {produto[6]}
                    """)
            
            opcao = input("Pesquisar novamente? [s/n]")
            if not (opcao in "Ss"): break 
    
if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    visualizar = Visualizar(id_adm_empresa, bd)
    visualizar.pesquisarProdutoPeloNome()