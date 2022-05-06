from multiprocessing.reduction import send_handle
import sqlite3

class BD:
    def __init__(self):
        self.conn = sqlite3.connect("bd_vai_vuado")
        self.cursor = self.conn.cursor()
    
    def executarComando(self, comando):
        try:
            self.cursor.execute(comando)
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")
    
    def inserirProdutos(self, id_adm_empresa, nome, categoria, medidas, imagem, descricao):
        try:
            self.cursor.execute(f"insert into produtos (id_adm_empresa, nome, categoria, medidas, imagem, descricao) values ('{id_adm_empresa}', '{nome}', '{categoria}', '{medidas}', '{imagem}', '{descricao}')")
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")

    def visualizarProduto(self, id_produto, id_adm_empresa):
        try:
            self.cursor.execute(f"select * from produtos where id_produto = '{id_produto}' and id_adm_empresa = {id_adm_empresa}")
            return self.cursor.fetchall()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")
    
    def visualizarProdutos(self):
        try:
            self.cursor.execute(f"select * from produtos")
            return self.cursor.fetchall()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")

    def editarProdutos(self, id_produto, id_adm_empresa, nome, categoria, medidas, imagem, descricao):
        try:
            self.cursor.execute(f"update produtos set nome = '{nome}', categoria = '{categoria}', medidas = '{medidas}', imagem = '{imagem}', descricao = '{descricao}' where id_produto = '{id_produto}' and id_adm_empresa = '{id_adm_empresa}'")
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")
        
    def deletarProdutos(self, id_produto, id_adm_empresa):
        try:
            self.cursor.execute(f"delete from produtos where id_produto = {id_produto} and id_adm_empresa = {id_adm_empresa}")
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")

    def enviarProdutoParaColeta(self, id_produto, id_adm_empresa, numero_de_rastreio, endereco_de_coleta, endereco_de_entrega, data_coleta, data_entrega, status_entrega, custo):
        try:
            self.cursor.execute(f"insert into coletas (id_produto, id_adm_empresa, numero_de_rastreio, endereco_de_coleta, endereco_de_entrega, data_coleta, data_entrega, status_entrega, custo) values ('{id_produto}', '{id_adm_empresa}', '{numero_de_rastreio}', '{endereco_de_coleta}', '{endereco_de_entrega}', '{data_coleta}', '{data_entrega}', '{status_entrega}', '{custo}')")
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")
    
    def atualizarStatusdeColeta(self, id_coleta, novo_status_entrega):
        try:
            self.cursor.execute(f"update coletas set status_entrega = '{novo_status_entrega}' where id_coleta = '{id_coleta}'")
            self.conn.commit()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")
    
    def receberNumeroDeRastreio(self, id_coleta):
        try:
            self.cursor.execute(f"select numero_de_rastreio from coletas where id_coleta = '{id_coleta}'")
            return self.cursor.fetchall()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")
    
    def visualizarColeta(self, id_coleta):
        try:
            self.cursor.execute(f"select * from coletas where id_coleta = '{id_coleta}'")
            return self.cursor.fetchall()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")
    
    def visualizarColetas(self):
        try:
            self.cursor.execute(f"select * from coletas")
            return self.cursor.fetchall()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")

    def verificarLogin(self, email, senha):
        try:
            self.cursor.execute(f"""
                select true from adm_empresa_contratante where email = '{email}' and senha = '{senha}'
            """)
            return self.cursor.fetchall()
        except sqlite3.Error as erro:
            print(f"Error: {erro}")
    
    def fechar(self):
        self.conn.close()

if __name__ == "__main__":
    banco = BD()
    print(banco.receberNumeroDeRastreio(1))
    banco.fechar()