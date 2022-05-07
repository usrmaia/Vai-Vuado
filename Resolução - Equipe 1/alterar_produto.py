from ast import match_case
from math import prod
from operator import truediv
import bd_vai_vuado, login_adm

bd = bd_vai_vuado.BD()
id_adm_empresa = 1

class Alterar():
    def __init__(self):
        self.opcao = []
        self.id_produto = []
        self.nome = []
        self.categoria = []
        self.medidas = []
        self.imagem = []
        self.descricao = []

    
    def exibirTela(self):
        self.opcao = input("""
            1. Alterar
            2. Limpar Dados
            3. Cancelar
            4. Voltar
        """)
    
    def retornarOpcao(self):
        try:
            self.opcao = int(self.opcao)
        except:
            self.opcao = -1
            
        return self.opcao
    
    def exibirProdutos(self):
        produtos = bd.visualizarProdutosDoAdm(id_adm_empresa)

        for produto in produtos:
            print(f"1. ID do produto: {produto[0]}")
            print(f"2. Nome do produto: {produto[2]}")
            print(f"3. Categoria do produto: {produto[3]}")
            print(f"4. Medidas do produto: {produto[4]}")
            print(f"5. Imagem do produto: {produto[5]}")
            print(f"6. Descrição do produto: {produto[6]}")
            print("")
        
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
            print(f"1. Nome do produto: {self.nome}")
            print(f"2. Categoria do produto: {self.categoria}")
            print(f"3. Medidas do produto: {self.medidas}")
            print(f"4. Imagem do produto: {self.imagem}")
            print(f"5. Descrição do produto: {self.descricao}")
            print(f"0. Sair")

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
    alterar = Alterar()
    alterar.exibirProdutos()
    alterar.alterarProduto()