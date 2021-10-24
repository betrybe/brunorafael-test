from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    lista = []
    TITULO = "\nProdutos estocados por empresa: \n"

    def __init__(self):
        self.lista = []

    @staticmethod
    def generate(stock):
        obj = SimpleReport()
        complete = CompleteReport()
        retorno = obj.generate(stock)
        retorno = retorno + complete.qtd_produto_by_empresa(stock)
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
        for lista_empresa in self.lista:
            empresa = empresa + '- '
            empresa = empresa + lista_empresa['nome'] + ': '
            empresa = empresa + str(lista_empresa['qtd'])+'\n'

        return retorno + empresa

    def adicionar_lista(self, nome, qtd):
        self.nome = nome
        self.qtd = qtd
        if self.verifica_lista(self.nome):
            empresa_dic = {}
            empresa_dic['nome'] = self.nome
            empresa_dic['qtd'] = self.qtd
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
