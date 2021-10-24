import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    stock = []

    def __init__(self):
        self.stock = []

    @staticmethod
    def import_data(nome_arquivo):
        jsonImporter = JsonImporter()
        extensao = Importer.verifica_tipo_arquivo(nome_arquivo)
        if extensao == '.json':
            with open(nome_arquivo) as arq:
                reader = json.load(arq)
                for row in reader:
                    jsonImporter.stock.append(dict(row))
                return jsonImporter.stock
        else:
            raise ValueError("Arquivo inválido")
