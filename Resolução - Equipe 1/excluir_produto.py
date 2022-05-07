from http.client import OK
import bd_vai_vuado, visualizar_produto, util

bd = bd_vai_vuado.BD()
id_adm_empresa = 1

class Excluir():
    def __init__(self):
        self.id_produto = []
        self.senha = []
        self.visualizar = visualizar_produto.Visualizar()

    def excluirProduto(self):
        util.visualizarProdutosDoAdm(id_adm_empresa)
        #aplicar pesquisa
        self.id_produto = input("Informe o ID de um produto para exclusão ou 0 para cancelar/voltar: ")
        if self.id_produto != "0":
            produto = bd.visualizarProduto(self.id_produto, id_adm_empresa)
            print(produto)
            self.senha = input("Para confirmar exclusão, informe sua senha: ")
            if bd.confirmarSenha(id_adm_empresa, self.senha):
                bd.deletarProduto(self.id_produto, id_adm_empresa)
        

    
    
if __name__ == "__main__":
    excluir = Excluir()
    excluir.excluirProduto()