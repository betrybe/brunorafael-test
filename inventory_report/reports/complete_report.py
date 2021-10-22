from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    lista = []
    TITULO = "\nProdutos estocados por empresa: \n"

    def __init__(self):
        pass

    @staticmethod
    def generate(stock):
        obj = SimpleReport()
        complete = CompleteReport()
        retorno = obj.generate(stock)
        retorno = retorno + complete.qtd_produto_by_empresa(stock)
        #retorno = complete.qtd_produto_by_empresa(stock)
        return retorno

    def qtd_produto_by_empresa(self, stock):
        retorno = self.TITULO
        empresa = ''
        self.stock = stock
        for produto in self.stock:
            qtdaux = 0
            nomeEmpresa = produto['nome_da_empresa']
            for produtoLista in self.stock:
                if produtoLista['nome_da_empresa'] == nomeEmpresa:
                    qtdaux += 1
                    
            self.adicionar_lista(nomeEmpresa, qtdaux)

            #empresa = '- ' + nomeEmpresa + ' : ' + str(qtdaux)+'\n'
            #retorno = retorno + ' ' + empresa
            #empresa = ''
        for lista_empresa in self.lista:
            empresa = empresa + '- ' + lista_empresa['nome'] + ': ' + lista_empresa['qtd']+'\n'

        return retorno + empresa

    def adicionar_lista(self, nome, qtd):
        self.nome = nome
        self.qtd = qtd
        if self.verifica_lista(self.nome):
            empresa_dic = {}
            empresa_dic['nome'] = self.nome
            empresa_dic['qtd'] = str(self.qtd)
            self.lista.append(empresa_dic)

    def verifica_lista(self, nome):
        self.nome = nome
        retorno = True
        if len(self.lista) == 0:
            return retorno
        else:
            for lista_aux in self.lista:
                if lista_aux['nome'] == self.nome:
                    retorno = False
            return retorno





