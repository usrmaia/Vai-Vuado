import manter_produto

class Menu():
    def __init__(self, id_adm_empresa, bd):
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa
        self.opcao = []

    def exibirMenu(self):
        self.opcao = input("""
            1. Manter Produto
            2. Outras Coisas
            0. Sair
        """)

        match self.opcao:
            case "1":
                manter = manter_produto.Manter(self.id_adm_empresa, self.bd)
                manter.exibirMenu()
            case _:
                pass

    
if __name__ == "__main__": 
    menu = Menu()
    menu.exibirMenuPrincipal()
    print(menu.retornarOpcao())