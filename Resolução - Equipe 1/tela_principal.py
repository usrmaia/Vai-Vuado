class Menu():
    def __init__(self):
        self.opcao = []

    def exibirMenuPrincipal(self):
        self.opcao = input("""
            1. Manter Produto
            2. Outras Coisas
            0. Sair
        """)

    def retornarOpcao(self):
        try:
            self.opcao = int(self.opcao)
        except:
            self.opcao = -1
            
        return self.opcao

if __name__ == "__main__": 
    menu = Menu()
    menu.exibirMenuPrincipal()
    print(menu.retornarOpcao())