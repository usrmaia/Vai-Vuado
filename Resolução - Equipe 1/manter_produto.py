import cadastrar_produto, alterar_produto, visualizar_produto, excluir_produto

class Manter():
    def __init__(self, id_adm_empresa, bd):
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa
        self.opcao = []
    
    def exibirMenu(self):
        self.opcao = input("""
            1. Cadastrar
            2. Alterar
            3. Visualizar
            4. Excluir
            0. Voltar
        """)

        match self.opcao:
            case "1":
                cadastrar = cadastrar_produto.Cadastrar(self.id_adm_empresa, self.bd)
                cadastrar.cadastrarProduto()
            case "2": 
                alterar = alterar_produto.Alterar(self.id_adm_empresa, self.bd)
                alterar.exibirProdutos()
                alterar.alterarProduto()
            case "3": 
                visualizar = visualizar_produto.Visualizar(self.id_adm_empresa, self.bd)
                visualizar.pesquisarProdutoPeloNome()
            case "4": 
                excluir = excluir_produto.Excluir(self.id_adm_empresa, self.bd)
                excluir.excluirProduto()
            case _: pass

if __name__ == "__main__": 
    pass