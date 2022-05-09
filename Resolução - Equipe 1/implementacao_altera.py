import bd_vai_vuado, util, alterar_produto

class Altera():
    def __init__(self, id_adm_empresa, bd):
        self.id_adm_empresa = id_adm_empresa
        self.bd = bd
        self.altera = alterar_produto.Alterar(self.id_adm_empresa, self.bd)
    
    def alterarProduto(self):
        while(True):
            if self.altera.selecionarProdutos():
                if self.altera.alterarProduto():
                    pass
                else: break
            else: break
            
if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    altera = Altera(id_adm_empresa, bd)
    altera.alterarProduto()