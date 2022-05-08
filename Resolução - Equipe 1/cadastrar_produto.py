import bd_vai_vuado, util

class Cadastrar():
    def __init__(self, id_adm_empresa, bd):
        self.nome = []
        self.categoria = []
        self.medidas = []
        self.imagem = []
        self.descricao = []
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa
        self.opcao = []
    
    def cadastrarProduto(self):
        while(True):

            util.exibirInformacoesDeProduto([self.nome, self.categoria, self.medidas, self.imagem, self.descricao], "0. Voltar")
            self.opcao = input("Selecione uma opção: ")

            match self.opcao:
                case "1": self.nome = input("Informe o nome do produto: ")
                case "2": self.categoria = input("Informe a categoria do produto: ") 
                case "3": self.medidas = input("Informe as medidas do produto (peso - largura x altura x profundidade): ")
                case "4": self.imagem = input("Informe o link para imagem do produto: ")
                case "5": self.descricao = input("Informe uma descrição para o produto: ")
                case _: break

        # "validar produto"

        self.opcao = input("""
                1. Confirmar
                2. Limpar Dados
                3. Cancelar
                0. Voltar

        """)

        match self.opcao:
            case "1": 
                self.bd.inserirProduto(self.id_adm_empresa, self.nome, self.categoria, self.medidas, self.imagem, self.descricao)
            case "2":
                self.nome = []
                self.categoria = []
                self.medidas = []
                self.imagem = []
                self.descricao = []
            case "3": pass
            case _: pass

if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    cadastrar = Cadastrar(id_adm_empresa, bd)
    cadastrar.cadastrarProduto()