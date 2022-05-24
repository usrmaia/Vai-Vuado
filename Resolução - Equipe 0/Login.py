from BDVaiVuado import confirmarLogin

def logar():
    op = 'S'

    while(op == 'S'):
        print("LOGIN \n")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        adm = confirmarLogin(email, senha)

        if not adm:
            print("Email ou senha inválidos!")
            op = input("Deseja realizar o login novamente? [S/N] ").upper()[0]
        else:
            print("Login realizado com sucesso!")
            op = 'N'
            return True
    return False