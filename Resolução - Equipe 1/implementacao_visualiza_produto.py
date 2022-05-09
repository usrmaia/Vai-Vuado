import visualiza_produto

class Visualiza():
    def __init__(self, id_adm_empresa, bd):
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa
        self.visualiza = visualiza_produto.Visualiza(self.id_adm_empresa, self.bd)
    
    def visualizarProduto(self):

        while(True):
    
            self.visualiza.pesquisarProdutoPeloNome()

            if not self.visualiza.opcao == "Sair":

                self.visualiza.visualizarProduto()
            
            else: break