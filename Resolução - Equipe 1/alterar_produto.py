import bd_vai_vuado, util

def validarIDProduto(id_produto, id_adm_empresa):
    produtos = util.retornarProdutosDoAdm(id_adm_empresa)

    for produto in produtos:

        if id_produto == str(produto[0]):

            return True
    
    return False

def visualizarMenuDeAlteracaoProdutoDoAdm(id_produto, id_adm_empresa, bd):

    dados = bd.visualizarProduto(id_produto, id_adm_empresa)
    dados = dados[0]

    print(f"""
            
             . ID:          {dados[0]}
            1. Nome:        {dados[2]}
            2. Categoria:   {dados[3]}
            3. Medidas:     {dados[4]}
            4. Imagem:      {dados[5]}
            5. Descrição:   {dados[6]}
            0. Voltar
        
    """)

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
    
    def selecionarProdutos(self):
        util.visualizarProdutosDoAdm(self.id_adm_empresa)

        self.id_produto = input("Digite o ID do produto que deseja alterar ou 0 para sair: ")

        if self.id_produto == "0": return False

        return validarIDProduto(self.id_produto, self.id_adm_empresa)
    
    def alterarProduto(self):

        produto = util.retornarProdutoDoAdm(self.id_produto, self.id_adm_empresa)
        self.nome = produto[0][2]
        self.categoria = produto[0][3]
        self.medidas = produto[0][4]
        self.imagem = produto[0][5]
        self.descricao = produto[0][6]
        
        while(True):

            util.exibirInformacoesDeProduto([self.nome, self.categoria, self.medidas, self.imagem, self.descricao], "0. Voltar")
            opcao = input("Informe o que deseja alterar: ")

            match opcao:
                case "1": self.nome = input("Informe um novo nome: ")
                case "2": self.categoria = input("Informe uma nova categoria: ")
                case "3": self.medidas = input("Informe uma nova medida: ")
                case "4": self.imagem = input("Informe uma nova imagem: ")
                case "5": self.descricao = input("Informe uma nova descrição: ")
                case _: break
            
        opcao = input("Confirmar alteração(ões)?[s/n] ")

        if opcao in "Ss":
            # Altenticar dados inseridos
            self.bd.editarProduto(self.id_produto, self.id_adm_empresa, self.nome, self.categoria, self.medidas, self.imagem, self.descricao)
        
        opcao = input("Deseja continuar alterando? [s/n] ")

        if opcao in "Ss":
            return True
        
        return False



if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    alterar = Alterar(id_adm_empresa, bd)
    alterar.selecionarProdutos()
    alterar.alterarProduto()