import bd_vai_vuado, util

class Altera():
    
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

    def visualizarProdutosDoAdm(self):
        util.visualizarProdutosDoAdm(self.id_adm_empresa)

    def selecionarIDDoProduto(self):

        self.id_produto = input("Digite o ID do produto que deseja alterar ou 0 para sair: ")
        if self.id_produto == "0": return False

        return True
    
    def validarIDDoProduto(self):

        produtos = util.retornarProdutosDoAdm(self.id_adm_empresa)

        for produto in produtos:
            
            id_produto_valido = str(produto[0])
            if self.id_produto == id_produto_valido:
                return True
        
        print("ID do produto não é válida! Tente novamente ")
        return False

    def exibirMenuDeAlteracao(self):

        produto = util.retornarProdutoDoAdm(self.id_produto, self.id_adm_empresa)
        self.nome = produto[0][2]
        self.categoria = produto[0][3]
        self.medidas = produto[0][4]
        self.imagem = produto[0][5]
        self.descricao = produto[0][6]
        
        while(True):

            util.exibirInformacoesDeProduto([self.nome, self.categoria, self.medidas, self.imagem, self.descricao], "0. Voltar 6. Confirmar")
            self.opcao = input("Informe o que deseja alterar: ")

            match self.opcao:
                case "1": self.nome = input("Informe um novo nome: ")
                case "2": self.categoria = input("Informe uma nova categoria: ")
                case "3": self.medidas = input("Informe uma nova medida: ")
                case "4": self.imagem = input("Informe uma nova imagem: ")
                case "5": self.descricao = input("Informe uma nova descrição: ")
                case "6": 
                    self.opcao = "Confirmar" 
                    break
                case "0": 
                    self.opcao = "Voltar"
                    break
                case _: pass
    
    def alterarProduto(self):

        # Altenticar dados inseridos
        self.bd.editarProduto(self.id_produto, self.id_adm_empresa, self.nome, self.categoria, self.medidas, self.imagem, self.descricao)
        
        self.opcao = input("Deseja continuar alterando? [s/n] ")
        if self.opcao in "Ss": self.opcao = "Continuar alterando"
        else: self.opcao = "Continuar alterando"
        
if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    alterar = Altera(id_adm_empresa, bd)
