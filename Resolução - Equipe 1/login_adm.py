class Login():
    def __init__(self, bd):
        self.email = []
        self.senha = []
        self.bd = bd
        self.id_adm_empresa = []

    def realizarLogin(self):
        print("Realizar login do Administrador da Empresa: ")
        self.email = input("Informe seu email: ")
        self.senha = input("Informe sua senha: ")

        if self.bd.verificarLogin(self.email, self.senha):
            print("Login realizado! :) ")
            self.id_adm_empresa = self.bd.retornarIdAdmEmpresa(self.email, self.senha)
            return True
        
        print("Erro ao realizar login! :( ")
        return False

    def retornarID(self):
        return self.id_adm_empresa    

if __name__ == "__main__":    
    login = Login()
    login.realizarLogin()
    print(login.retornarID())