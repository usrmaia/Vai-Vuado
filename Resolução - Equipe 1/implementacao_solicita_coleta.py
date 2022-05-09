import solicitar_coleta, bd_vai_vuado

class Coleta():
    def __init__(self, id_adm_empresa, bd, endereco_adm):
        self.id_adm_empresa = id_adm_empresa
        self.bd = bd
        self.endereco_de_coleta = endereco_adm
        self.coleta = solicitar_coleta.Coleta(self.id_adm_empresa, self.bd, self.endereco_de_coleta)
    
    def solicitarColeta(self):
        while(True):

            self.coleta.visualizarProdutosDoAdm()
            self.coleta.redefinirVariaveis()
            self.coleta.editarColetaSimples()

            if self.coleta.opcao == "5":

                if self.coleta.validarIdProduto():

                    self.coleta.calcularNumeroDeRastreioCusto()

                    while(True):

                        self.coleta.exibirMenuDePreColetaCompleto()

                        match self.coleta.opcao:
                            case "5": self.coleta.editarMenuPreColeta()
                            case "6": 
                                self.coleta.obterStatusDoVaiVuado()
                                operacao_bem_sucedida = self.coleta.solicitarColeta()
                                
                                if operacao_bem_sucedida: pass 
                                else:
                                    if self.coleta.repetirColeta(): pass
                                    else: break

                            case _: break

                else: 

                    if self.coleta.repetirColeta(): pass
                    else: break

            else:

                if self.coleta.repetirColeta(): pass
                else: break

            
if __name__ == "__main__": 
    bd = bd_vai_vuado.BD()
    id_adm_empresa = 1
    coleta = Coleta(id_adm_empresa, bd, "Rua T - 58")
    coleta.solicitarColeta()

