import bd_vai_vuado, util

class Alterar():
    def __init__(self, id_adm_empresa, bd):
        self.id_produto = []
        self.nome = []
        self.categoria = []
        self.medidas = []
        self.imagem = []
        self.descricao = []
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa
        self.opcao = []

    
    def exibirTela(self):
        self.opcao = input("""
            1. Alterar
            2. Limpar Dados
            3. Cancelar
            4. Voltar
        """)
    
    def exibirProdutos(self):
        util.visualizarProdutosDoAdm(self.id_adm_empresa)
        
        self.id_produto = input("Digite o ID do produto que deseja alterar: ")
        # Aplicar tratamento em self.id_produto (id existente)
    
    def alterarProduto(self):
        produto = bd.visualizarProduto(int(self.id_produto), id_adm_empresa)
        self.nome = produto[0][2]
        self.categoria = produto[0][3]
        self.medidas = produto[0][4]
        self.imagem = produto[0][5]
        self.descricao = produto[0][6]

        while(True):
            util.exibirInformacoesDeProduto([self.nome, self.categoria, self.medidas, self.imagem, self.descricao] , "0. Voltar")
            self.opcao = input("Informe o que deseja alterar: ")

            match self.opcao:
                case "1": self.nome = input("Informe um novo nome: ")
                case "2": self.categoria = input("Informe uma nova categoria: ")
                case "3": self.medidas = input("Informe uma nova medida: ")
                case "4": self.imagem = input("Informe uma nova imagem: ")
                case "5": self.descricao = input("Informe uma nova descrição: ")
                case _: break
            
        self.opcao = input("Confirmar alteração(ões)?[s/n] ")

        if self.opcao in "Ss":
            # Altenticar dados inseridos
            bd.editarProduto(self.id_produto, id_adm_empresa, self.nome, self.categoria, self.medidas, self.imagem, self.descricao)


if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    alterar = Alterar(id_adm_empresa, bd)
    alterar.exibirProdutos()
    alterar.alterarProduto()