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
    
    def inserirInformacoesDoProduto(self):

        while(True):

            util.exibirMenuDeProdutoSimples(self.nome, self.categoria, self.medidas, self.imagem, self.descricao)
            opcao = input("Selecione uma opção: ")

            match opcao:
                case "1": self.nome = input("Informe o nome do produto: ")
                case "2": self.categoria = input("Informe a categoria do produto: ") 
                case "3": self.medidas = input("Informe as medidas do produto (peso - largura x altura x profundidade): ")
                case "4": self.imagem = input("Informe o link para imagem do produto: ")
                case "5": self.descricao = input("Informe uma descrição para o produto: ")
                case _: break
    
    def validarCadastroDeProduto(self):

        dados = [self.nome, self.categoria, self.medidas, self.imagem, self.descricao]
        
        for dado in dados:

            if len(dado) == 0: 
                print("Há dado(s) não cadastrado(s)!")

                return False
        
        return True
    
    def confirmarCadastro(self):
        opcao = input("""

                        1. Confirmar
                        2. Limpar Dados
                        3. Cancelar
                        0. Voltar

                        Selecione uma opção: 

                """)

        match opcao:
            case "1": 
                self.bd.inserirProduto(self.id_adm_empresa, self.nome, self.categoria, self.medidas, self.imagem, self.descricao)
            case "2":
                self.nome = self.categoria = self.medidas = self.imagem = self.descricao = []
                return "Limpar Dados"
            case _: pass
            
if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    cadastro = Cadastro(id_adm_empresa, bd)
    cadastro.cadastrarProduto()