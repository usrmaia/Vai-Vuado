from BDVaiVuado import statusDeEntrega, resgatarProduto

def rastrearEntrega():
    num = input(f"Insira o número de rastreio da coleta: ")

    while not num.isdigit():
        print("Insira somente números!")
        num = input(f"Insira o número de rastreio da coleta: ")

    num = int(num)

    while(num != 0):
        status, idProduto = statusDeEntrega(num)

        if(status != None):
            print(f"""
                Produto: {resgatarProduto(idProduto)}
                Status do pedido: {OrdemCronologica(status)}

                0 - Voltar ao menu principal.
            """)
        else:
            print(f"""
                Número de rastreio inválido ou inexistente, tente novamente.

                0 - Voltar ao menu principal.
            """)
        num = int(input(f"Insira o número de rastreio da coleta: "))
    return

def OrdemCronologica(estagio):
    estagio = estagio.upper()
    status = ['ACEITO', 'COLETADO', 'EM TRANSITO', 'ENTREGUE']
    temp = ""

    if estagio == "NEGADO":
        return "NEGADO"

    for x in status:
        if x == estagio.upper():
            temp += f"{x}"
            return temp
        temp += f"{x} -> "