import bd_vai_vuado, util

class Cadastro():
    
    def __init__(self, id_adm_empresa, bd):
        self.nome = []
        self.categoria = []
        self.medidas = []
        self.imagem = []
        self.descricao = []
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa
        self.opcao = []
    
    def inserirInformacoesDoProduto(self):

        while(True):

            util.exibirInformacoesDeProduto([self.nome, self.categoria, self.medidas, self.imagem, self.descricao], "0. Sair 6. Confirmar")
            self.opcao = input("Selecione uma opção: ")

            match self.opcao:
                case "1": self.nome = input("Informe o nome do produto: ")
                case "2": self.categoria = input("Informe a categoria do produto: ") 
                case "3": self.medidas = input("Informe as medidas do produto (peso - largura x altura x profundidade): ")
                case "4": self.imagem = input("Informe o link para imagem do produto: ")
                case "5": self.descricao = input("Informe uma descrição para o produto: ")
                case "6": 
                    self.opcao = "Confirmar"
                    break
                case "0":
                    self.opcao = "Sair"
                    break
                case _: pass
    
    def validarCadastroDeProduto(self):

        dados = [self.nome, self.categoria, self.medidas, self.imagem, self.descricao]
        
        for dado in dados:

            if len(dado) == 0: 

                print("Há dado(s) não cadastrado(s)!")

                return False
        
        return True
    
    def confirmarCadastro(self):

        while(True):

            self.opcao = input("""

                            1. Confirmar
                            2. Limpar Dados / Cancelar
                            0. Sair

                            Selecione uma opção: 

                    """)

            match self.opcao:

                case "1": 
                    self.bd.inserirProduto(self.id_adm_empresa, self.nome, self.categoria, self.medidas, self.imagem, self.descricao)
                    break
                case "2": break
                case "0": 
                    self.opcao = "Sair"
                    break 
                case _: pass

    def redefinirDados(self):
        self.nome = self.categoria = self.medidas = self.imagem = self.descricao = []
                
if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    cadastro = Cadastro(id_adm_empresa, bd)
    cadastro.cadastrarProduto()