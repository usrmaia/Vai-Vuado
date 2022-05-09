import manter_produto, implementacao_solicita_coleta

class Menu():
    def __init__(self, id_adm_empresa, bd, endereco):
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa
        self.endereco = endereco

    def exibirMenu(self):
        while(True):
            opcao = input("""

            VAI VUADO

                1. Manter Produto
                2. Solicitar Coleta
                3. Outras Opções
                0. Sair/Fechar

                Selecione uma opção: 

            """)

            match opcao:
                case "1":
                    manter = manter_produto.Manter(self.id_adm_empresa, self.bd)
                    manter.exibirMenu()
                case "2":
                    coleta = implementacao_solicita_coleta.Coleta(self.id_adm_empresa, self.bd, self.endereco)
                    coleta.solicitarColeta()
                case _: break

    
if __name__ == "__main__": 
    menu = Menu()
    menu.exibirMenuPrincipal()
    print(menu.retornarOpcao())