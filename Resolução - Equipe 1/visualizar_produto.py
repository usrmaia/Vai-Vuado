import bd_vai_vuado

class Visualizar():
    def __init__(self, id_adm_empresa, bd):
        self.nome = []
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa

    def pesquisarProdutoPeloNome(self):
        self.nome = input("Busque por algum produto pelo nome: ")
        produtos = self.bd.visualizarProdutosDoAdm(self.id_adm_empresa)

        for produto in produtos:
            if self.nome in produto[2]:
                print(f"""
                    1. ID: {produto[1]}
                    2. {produto[2]}
                    3. {produto[3]}
                    4. {produto[4]}
                    5. {produto[5]}
                    6. {produto[6]}
                """)
    
if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    visualizar = Visualizar(id_adm_empresa, bd)
    visualizar.pesquisarProdutoPeloNome()