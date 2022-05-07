import bd_vai_vuado, login_adm
import sys
print(sys.version)
bd = bd_vai_vuado.BD()
id_adm_empresa = 1

class Cadastrar():
    def __init__(self):
        self.opcao = []
    
    def exibirTela(self):
        self.opcao = input("""
            1. Confirmar
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
    
    def cadastrarProduto(self):
        nome = input("Informe o nome do produto: ")
        categoria = input("Informe a categoria do produto: ") 
        medidas = input("Informe as medidas do produto (peso - largura x altura x profundidade): ")
        imagem = input("Informe o link para imagem do produto: ")
        descricao = input("Informe uma descrição para o produto: ")

        # "validar produto"

        self.opcao = input("""
            1. Confirmar
            2. Limpar
            3. Cancelar
            4. Voltar
        """)

        match self.opcao:
            case "1": 
                bd.inserirProduto(id_adm_empresa, nome, categoria, medidas, imagem, descricao)
            case _: pass

if __name__ == "__main__":
    cadastrar = Cadastrar()
    cadastrar.cadastrarProduto()