import os.path
from collections.abc import Iterable
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    stock = []

    def __init__(self, importer):
        self.importer = importer
        self.data = []
        self.stock = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, arquivo, tp_relatorio):
        self.arquivo = arquivo
        self.tp_relatorio = tp_relatorio
        self.data.extend(self.importer.import_data(self.arquivo))
        self.stock.clear()
        extensao = self.verifica_tipo_arquivo(self.arquivo)
        self.redirect(extensao, self.arquivo)
        if len(self.stock) > 0 and self.tp_relatorio == 'simples':
            return self.relatorio_simples()
        if len(self.stock) > 0 and self.tp_relatorio == 'completo':
            return self.relatorio_completo()

    def verifica_tipo_arquivo(self, arquivo):
        self.arquivo = arquivo
        return os.path.splitext(self.arquivo)[1]

    def importar(self, extensao, arquivo):
        if extensao == '.csv':
            csvImporter = CsvImporter()
            self.stock = csvImporter.import_data(self.arquivo)

    def redirect(self, extensao, arquivo):
        self.extensao = extensao
        self.arquivo = arquivo
        if extensao == '.csv':
            csvImporter = CsvImporter()
            self.stock = csvImporter.import_data(self.arquivo)
        if extensao == '.json':
            jsonImporter = JsonImporter()
            self.stock = jsonImporter.import_data(self.arquivo)
        if extensao == '.xml':
            xmlImporter = XmlImporter()
            self.stock = xmlImporter.import_data(self.arquivo)

    def relatorio_simples(self):
        obj = SimpleReport()
        return obj.generate(self.stock)

    def relatorio_completo(self):
        obj = CompleteReport()
        return obj.generate(self.stock)
