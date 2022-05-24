from BDVaiVuado import importarHistoricoDeColetas, resgatarProduto, resgatarAdministradorPorId
from SolicitarNovaColeta import SolicitarNovaColeta

def historicoDeColeta():
    print("HISTÓRICO DE COLETAS")
    op = input("1 - Exibir todas as coletas\n2 - Filtrar coletas por data ")
    op = int(op)

    data = ""

    if op == 2:
        data = input("Informe a data [DD/MM/AAAA]\n")
        ano = data[6:10]
        mes = data[3:6]
        dia = data[0:2]
        data = f"{ano}-{mes}-{dia}"

    historico = importarHistoricoDeColetas(data)

    if not historico:
        opNovaColeta = input("Não há pedidos, deseja solicitar uma nova coleta? [S/N]").upper()

        if opNovaColeta == "S":
            SolicitarNovaColeta()

        return

    for x in historico:
        produto = resgatarProduto(x[1])
        administrador = resgatarAdministradorPorId(x[2])

        print(f"""
        ID Coleta: {x[0]} | Produto: {produto} | Admistrador: {administrador} | 
        Número de rastreio: {x[3]} | End. Coleta: {x[4]} | End. Entrega: {x[5]} |
        Custo: R$ {x[9]} | Data de coleta: {x[6]} | Data de entrega: {x[7]} | Status: {x[8]}
        """)
    input("Pressione qualquer tecla para voltar ao menu.\n")
