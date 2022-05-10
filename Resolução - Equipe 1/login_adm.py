import bd_vai_vuado
from os import _exit

def inserirEmailSenha(email = [], senha = []):
    while(True):

        opcao = input(f""" 

            1. Email: {email}
            2. Senha: {senha}
            0. Sair 3. Confirmar

        Selecione uma opção: 
        """)

        match opcao:
            case "1": email = input("Informe seu email: ")
            case "2": senha = input("Informe sua senha: ")
            case "3": break
            case "0": _exit(1)
            case _: pass

    return email, senha

class Login():
    def __init__(self, bd):
        self.email = []
        self.senha = []
        self.endereco = []
        self.bd = bd
        self.id_adm_empresa = []

    def realizarLogin(self):
        print("Realizar login do Administrador da Empresa: ")

        self.email, self.senha = inserirEmailSenha()

        if self.bd.verificarLogin(self.email, self.senha):
            print("Login realizado! :) ")

            self.id_adm_empresa = self.bd.retornarIdAdmEmpresa(self.email, self.senha)
            self.endereco = self.bd.retornarEnderecoAdmEmpresa(self.id_adm_empresa)

            return True
        
        print("Erro ao realizar login! :( ")

        return False

    def retornarID(self):
        return self.id_adm_empresa 

    def retornarEndereco(self):
        return self.endereco    

if __name__ == "__main__":    
    bd = bd_vai_vuado.BD()

    login = Login(bd)
    login.realizarLogin()

    print(login.retornarEndereco())
    print(login.retornarID())