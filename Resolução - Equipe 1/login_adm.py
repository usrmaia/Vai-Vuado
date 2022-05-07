import bd_vai_vuado

bd = bd_vai_vuado.BD()

class Login():
    def __init__(self):
        self.email = []
        self.senha = []
        self.id_adm_empresa = []

    def realizarLogin(self):
        print("Realizar login do Administrador da Empresa: ")
        self.email = input("Informe seu email: ")
        self.senha = input("Informe sua senha: ")

        if bd.verificarLogin(self.email, self.senha):
            print("Login realizado! :) ")
            self.id_adm_empresa = bd.retornarIdAdmEmpresa(self.email, self.senha)
            return True
        
        print("Erro ao realizar login! :( ")
        return False

    def retornarID(self):
        return self.id_adm_empresa    

if __name__ == "__main__":    
    login = Login()
    login.realizarLogin()
    print(login.retornarID())