from Menu import menu
from Login import logar

adm = logar()

if adm:
    menu()
else:
    print("O administrador precisa está logado para utilizar o sistema!")