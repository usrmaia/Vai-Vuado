import implementacao_cadastro, implementacao_altera, implementacao_visualiza_produto, implementacao_exclui_produto

class Manter():
    def __init__(self, id_adm_empresa, bd):
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa
    
    def exibirMenu(self):
        while(True):

            opcao = input("""

            Manter Produto: 

                1. Cadastrar
                2. Alterar
                3. Visualizar
                4. Excluir
                0. Voltar

                Selecione uma opção: 

            """)

            match opcao:
                case "1":
                    cadastro = implementacao_cadastro.Cadastro(self.id_adm_empresa, self.bd)
                    cadastro.cadastrarProduto()
                case "2": 
                    altera = implementacao_altera.Altera(self.id_adm_empresa, self.bd)
                    altera.alterarProduto()
                case "3": 
                    visualiza = implementacao_visualiza_produto.Visualiza(self.id_adm_empresa, self.bd)
                    visualiza.visualizarProduto()
                case "4": 
                    exclui = implementacao_exclui_produto.Exclui(self.id_adm_empresa, self.bd)
                    exclui.excluirProduto()
                case "0": break
                case _: pass

if __name__ == "__main__": 
    pass