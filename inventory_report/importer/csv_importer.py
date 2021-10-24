from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    stock = []

    def __init__(self):
        self.stock = []

    @staticmethod
    def import_data(nome_arquivo):
        csvImporter = CsvImporter()
        extensao = Importer.verifica_tipo_arquivo(nome_arquivo)
        if extensao == '.csv':
            with open(nome_arquivo, 'r') as arq:
                reader = csv.DictReader(arq)
                for row in reader:
                    csvImporter.stock.append(dict(row))
                return csvImporter.stock
        else:
            raise ValueError("Arquivo inválido")
