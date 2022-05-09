from random import randrange
import bd_vai_vuado, util

class Coleta():
    def __init__(self, id_adm_empresa, bd, endereco_adm):
        self.bd = bd
        self.id_adm_empresa = id_adm_empresa
        self.id_produto = []
        self.numero_de_rastreio = []
        self.endereco_de_coleta = endereco_adm
        self.endereco_de_entrega = []
        self.data_coleta = []
        self.data_entrega = []
        self.status_entrega = []
        self.custo = []
        self.opcao = []

    def visualizarProdutosDoAdm(self):
        util.visualizarProdutosDoAdm(self.id_adm_empresa)
    
    def editarColetaSimples(self):
        while(True):
            self.opcao = input(f"""
            Dados da Pré-Coleta:

                1. ID do Produto: {self.id_produto}
                2. Endereço de Entrega: {self.endereco_de_entrega}
                3. Data de Coleta: {self.data_coleta}
                4. Data de Entrega: {self.data_entrega}
                0. Voltar  5. Confirmar

                Selecione uma opção: 

            """)

            match self.opcao:
                case "1": self.id_produto = input("Informe o ID de um produto para coleta: ")
                case "2": self.endereco_de_entrega = input("Informe o endereço de entrega: ")
                case "3": self.data_coleta = input("Informe a data de coleta: ") 
                case "4": self.data_entrega = input("Informe a data de entrega: ")
                case _: break
    
    def validarIdProduto(self):
        produtos_validos = util.retornarProdutosDoAdm(self.id_adm_empresa)

        for produto in produtos_validos:
            id_produto_valida = str(produto[0])
            if(self.id_produto == id_produto_valida):
                return True

        print("ID do produto inválida!")
        return False
    
    def calcularNumeroDeRastreioCusto(self):
        self.numero_de_rastreio = randrange(1, 9999)
        self.custo = randrange(0, 50)
        
    def exibirMenuDePreColetaCompleto(self):
        self.opcao = input(f"""
            Dados da Pré-Coleta:

                1. ID do Produto: {self.id_produto}
                . Número de Rasterio: {self.numero_de_rastreio}
                . Endereço de Coleta: {self.endereco_de_coleta}
                2. Endereço de Entrega: {self.endereco_de_entrega}
                3. Data de Coleta: {self.data_coleta}
                4. Data de Entrega: {self.data_entrega}
                . Status: []
                . Custo: {self.custo}

                0. Cancelar 5. Editar 6. Confirmar Coleta

                Selecione uma opção: 

        """)
    
    def editarMenuPreColeta(self):
        self.opcao = input("Selecione uma opção: ")
        
        match self.opcao:
            case "1": self.id_produto = input("Informe o ID de um produto para coleta: ")
            case "2": self.endereco_de_entrega = input("Informe o endereço de entrega: ")
            case "3": self.data_coleta = input("Informe a data de coleta: ") 
            case "4": self.data_entrega = input("Informe a data de entrega: ")
            case _: pass
        
    def obterStatusDoVaiVuado(self):
        self.status_entrega = "Aceito" if randrange(0, 2) == 1 else "Negado"

    def solicitarColeta(self):
        if self.status_entrega == "Aceito":
            self.bd.enviarProdutoParaColeta(self.id_produto, self.id_adm_empresa, self.numero_de_rastreio, self.endereco_de_coleta, self.endereco_de_entrega, self.data_coleta, self.data_entrega, self.status_entrega, self.custo)
            print("Pedido aceito! ;)")
            return True
        else:
            print("Lamentamos, pedido não aceito!")
            return False

    def repetirColeta(self):
        self.opcao = input("Deseja repetir coleta? [s/n] ")
        if self.opcao in "Ss": return True
        else: return False
    
    def redefinirVariaveis(self):
        self.id_produto = self.endereco_de_coleta = self.endereco_de_entrega = self.data_coleta = self.data_entrega = []
    
if __name__ == "__main__": 
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    #print(validarIdProduto("2", id_adm_empresa))
    #print(calcularNumeroDeRastreioCusto())
    coleta = Coleta(id_adm_empresa, bd, "Rua T - 58")
    coleta.redefinirVariaveis()