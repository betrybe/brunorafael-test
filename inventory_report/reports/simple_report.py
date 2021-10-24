from datetime import date


class SimpleReport:
    '''Recebe dados e retorna uma string formatada como um relatório'''
    def __init__(self):
        pass

    def data_antiga(self, stock):
        self.stock = stock
        dataFabricacaoAntiga = date.fromisoformat(str(date.today()))
        for produto in self.stock:
            dataFabricacao = date.fromisoformat(produto['data_de_fabricacao'])
            if dataFabricacao < dataFabricacaoAntiga:
                dataFabricacaoAntiga = dataFabricacao
        DT_FAB_ANT = 'Data de fabricação mais antiga: '
        mensagem = DT_FAB_ANT + str(dataFabricacaoAntiga.isoformat())
        return mensagem

    def val_proxima(self, stock):
        self.stock = stock
        dataAtual = date.fromisoformat(str(date.today()))
        aux = 0
        dataMaisProxima = date.fromisoformat(str(date.today()))
        for produto in self.stock:
            dataValidade = date.fromisoformat(produto['data_de_validade'])
            if dataValidade >= dataAtual:
                if aux == 0 or dataValidade <= dataMaisProxima:
                    dataMaisProxima = dataValidade
                    aux = 1
        DT_VAL_PROX = 'Data de validade mais próxima: '
        mensagem = DT_VAL_PROX + dataMaisProxima.isoformat()
        return mensagem

    def maior_estoque(self, stock):
        self.stock = stock
        total = 0
        empresaMaiorQtdProdutos = ""
        for produto in self.stock:
            qtdaux = 0
            nomeEmpresa = produto['nome_da_empresa']
            for produtoLista in self.stock:
                if produtoLista['nome_da_empresa'] == nomeEmpresa:
                    qtdaux += 1
                if qtdaux > total:
                    empresaMaiorQtdProdutos = nomeEmpresa
                    total += 1
        EMP_MAI_EST = 'Empresa com maior quantidade de produtos estocados:'
        mensagem = EMP_MAI_EST + ' ' + empresaMaiorQtdProdutos + '\n'
        return mensagem

    @staticmethod
    def generate(stock):
        sr = SimpleReport()
        dt_antiga = sr.data_antiga(stock)
        prox_dt = sr.val_proxima(stock)
        maior_estq = sr.maior_estoque(stock)
        return dt_antiga + '\n' + prox_dt + '\n' + maior_estq
