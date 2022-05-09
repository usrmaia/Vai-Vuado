import bd_vai_vuado, login_adm, tela_principal

if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    login = login_adm.Login(bd)

    if login.realizarLogin():
        home = tela_principal.Menu(login.retornarID(), bd, login.retornarEndereco())
        home.exibirMenu()
    
    bd.fechar()