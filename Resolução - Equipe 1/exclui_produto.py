import bd_vai_vuado, util

class Exclui():

    def __init__(self, id_adm_empresa, bd):
        self.id_produto = []
        self.senha = []
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa
        self.opcao = []
    
    def selecionarProduto(self):

        util.visualizarProdutosDoAdm(self.id_adm_empresa)
        #aplicar pesquisa
        self.id_produto = input("""

            0. Sair     
            
            Informe o ID de um produto para exclusão: """)
        
        if self.id_produto == "0": self.opcao = "Sair"

    def visualizarProdutoParaExclusao(self):

        produto = self.bd.visualizarProduto(self.id_produto, id_adm_empresa)
        nome = produto[0][2]
        categoria = produto[0][3]
        medidas = produto[0][4]
        imagem = produto[0][5]
        descricao = produto[0][6]

        util.exibirInformacoesDeProduto([nome, categoria, medidas, imagem, descricao], "")
        
    def confirmarSenhaParaExclusao(self):
        self.senha = input("Para confirmar exclusão, informe sua senha: ")
        return bd.confirmarSenha(self.id_adm_empresa, self.senha)

    def excluirProduto(self):
        bd.deletarProduto(self.id_produto, id_adm_empresa)
    
if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    excluir = Excluir(id_adm_empresa, bd)
    excluir.excluirProduto()