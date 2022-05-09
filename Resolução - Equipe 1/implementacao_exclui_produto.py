import bd_vai_vuado, exclui_produto

class Exclui():

    def __init__(self, id_adm_empresa, bd):
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa
        self.exclui = exclui_produto.Exclui(self.id_adm_empresa, self.bd)
    
    def excluirProduto(self):

        while(True):

            self.exclui.selecionarProduto()

            if not self.exclui.opcao == "Sair":
                
                self.exclui.visualizarProdutoParaExclusao()

                if self.exclui.confirmarSenhaParaExclusao():

                    self.exclui.excluirProduto()

            else: break


