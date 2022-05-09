import cadastrar_produto, bd_vai_vuado

class Cadastro():
    def __init__(self, id_adm_empresa, bd):
        self.id_adm_empresa = id_adm_empresa
        self.bd = bd
        self.cadastro = cadastrar_produto.Cadastro(self.id_adm_empresa, self.bd)
    
    def cadastrarProduto(self):
        while(True):
            self.cadastro.inserirInformacoesDoProduto()
            if self.cadastro.validarCadastroDeProduto():
                resposta = self.cadastro.confirmarCadastro()
                if resposta != "Limpar Dados": break
            else: break

if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    cadastro = Cadastro(id_adm_empresa, bd)
    cadastro.cadastrarProduto()