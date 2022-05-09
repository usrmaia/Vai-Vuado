import bd_vai_vuado, visualizar_produto, util

class Excluir():
    def __init__(self, id_adm_empresa, bd):
        self.id_produto = []
        self.senha = []
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa

    def excluirProduto(self):
        util.visualizarProdutosDoAdm(self.id_adm_empresa)
        #aplicar pesquisa
        self.id_produto = input("Informe o ID de um produto para exclusão ou 0 para cancelar/voltar: ")

        if self.id_produto != "0":
            
            produto = self.bd.visualizarProduto(self.id_produto, id_adm_empresa)
            nome = produto[0][2]
            categoria = produto[0][3]
            medidas = produto[0][4]
            imagem = produto[0][5]
            descricao = produto[0][6]

            util.exibirInformacoesDeProduto([nome, categoria, medidas, imagem, descricao], "")
            
            self.senha = input("Para confirmar exclusão, informe sua senha: ")
            if bd.confirmarSenha(self.id_adm_empresa, self.senha):
                bd.deletarProduto(self.id_produto, id_adm_empresa)
    
if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    excluir = Excluir(id_adm_empresa, bd)
    excluir.excluirProduto()