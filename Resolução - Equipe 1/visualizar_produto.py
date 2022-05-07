import bd_vai_vuado, login_adm

bd = bd_vai_vuado.BD()
id_adm_empresa = 1

class Visualizar():
    def __init__(self):
        self.nome = []

    def pesquisarProduto(self):
        self.nome = input("Busque por algum produto pelo nome: ")
        produtos = bd.visualizarProdutosDoAdm(id_adm_empresa)

        for produto in produtos:
            if self.nome in produto[2]:
                print(produto)

    
    
if __name__ == "__main__":
    visualizar = Visualizar()
    visualizar.pesquisarProduto()