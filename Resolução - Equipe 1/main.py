import bd_vai_vuado, login_adm, tela_principal

if __name__ == "__main__":
    bd = bd_vai_vuado.BD()
    login = login_adm.Login()
    menu = tela_principal.Menu()

    while True:
        if login.realizarLogin():
            menu.exibirMenuPrincipal()
            match menu.retornarOpcao():
                case 1: manter_produto()
                case _: pass 
    
    bd.fechar()