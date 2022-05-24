from RastrearEntrega import rastrearEntrega
from HistoricoDeColeta import historicoDeColeta
from BDVaiVuado import sair
from SolicitarNovaColeta import SolicitarNovaColeta

def menu():
    op = -1

    while(op != 0):
        print(f"""
            VAI VUADO
            1 - Rastrear entrega
            2 - Historico de coletas
            --------------------------
            3 - Solicitar nova coleta
            4 - Manter produtos
            --------------------------
            0 - Sair
        """)

        op = int(input())

        if op == 1:
            rastrearEntrega()
        elif op == 2:
            historicoDeColeta()
        elif op == 3:
            SolicitarNovaColeta()
        elif op == 0:
            sair()
            op = 0
        else:
            print("Opção invalida, tente novamente!")