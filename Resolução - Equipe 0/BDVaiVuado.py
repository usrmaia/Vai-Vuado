import sqlite3

conn = sqlite3.connect("bd_vai_vuado")
cursor = conn.cursor()
    
def executarComando(comando):
    try:
        cursor.execute(f"UPDATE coletas SET status_entrega = 'Entregue' WHERE id_coleta = 4")
        conn.commit()
    except sqlite3.Error as erro:
        print(f"Error: {erro}")

def statusDeEntrega(numero):
    try:
        cursor.execute(f"SELECT status_entrega, id_produto FROM coletas where numero_de_rastreio = '{numero}'")
        status = cursor.fetchall()
        if not status or len(status) < 1:
            return None, None

        return status[0][0], status[0][1]
    except sqlite3.Error as erro:
        print(f"Operação não realizada com sucesso!\nErro: {erro}")
        return None

def importarHistoricoDeColetas(data):
    try:
        if len(data) < 1:
            cursor.execute(f"SELECT * FROM coletas")
        else:
            cursor.execute(f"SELECT * FROM coletas WHERE data_coleta = '{data}'")
        coletas = cursor.fetchall()
        if not coletas or len(coletas) < 1:
            return None

        return coletas
    except sqlite3.Error as erro:
        print(f"Operação não realizada com sucesso!\nErro: {erro}")
        return None

def resgatarProduto(idProduto):
    try:
        cursor.execute(f"SELECT nome FROM produtos WHERE id_produto = '{idProduto}'")
        produto = cursor.fetchone()
        if not produto or len(produto) < 1:
            return None

        return produto[0]
    except sqlite3.Error as erro:
        print(f"Operação não realizada com sucesso!\nErro: {erro}")
        return None

def resgatarAdministradorPorId(idAdm):
    try:
        cursor.execute(f"SELECT nome FROM adm_empresa_contratante WHERE id_adm_empresa = '{idAdm}'")
        administrador = cursor.fetchone()
        if not administrador or len(administrador) < 1:
            return None

        return administrador[0]
    except sqlite3.Error as erro:
        print(f"Operação não realizada com sucesso!\nErro: {erro}")
        return None

def confirmarLogin(email, senha):
    try:
        cursor.execute(f"SELECT email, senha, nome FROM adm_empresa_contratante WHERE email = '{email}'")
        administrador = cursor.fetchone()

        if not administrador or len(administrador) < 1:
            return None
        if(senha == administrador[1]):
            return administrador
        return False
    except sqlite3.Error as erro:
        print(f"Operação não realizada com sucesso!\nErro: {erro}")
        return None

def sair():
    conn.close()