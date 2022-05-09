import bd_vai_vuado, altera_produto

class Altera():
    def __init__(self, id_adm_empresa, bd):
        self.id_adm_empresa = id_adm_empresa
        self.bd = bd
        self.altera = altera_produto.Altera(self.id_adm_empresa, self.bd)
    
    def alterarProduto(self):
        while(True):

            self.altera.visualizarProdutosDoAdm()

            if self.altera.selecionarIDDoProduto():

                if self.altera.validarIDDoProduto():

                    self.altera.exibirMenuDeAlteracao()

                    if self.altera.opcao == "Confirmar":

                        self.altera.alterarProduto()

                        if not self.altera.opcao == "Continuar alterando": break

            else: break
            
if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    altera = Altera(id_adm_empresa, bd)
    altera.alterarProduto()