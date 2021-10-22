import os.path
import csv
import json
import xml.etree.ElementTree as ET


from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    stock = []

    def __init__(self) -> None:
        pass

    @staticmethod
    def import_data(arquivo, tipo_relatorio):
        invetory = Inventory()
        arquivo = '../'+arquivo
        invetory.stock.clear()
        extensao = invetory.verifica_tipo_arquivo(arquivo)
        invetory.redireciona_extensao(extensao, arquivo, tipo_relatorio)
        if len(invetory.stock) > 0 and tipo_relatorio == 'simples':
            return invetory.relatorio_simples()
        if len(invetory.stock) > 0 and tipo_relatorio == 'completo':
            return invetory.relatorio_completo()

    def verifica_tipo_arquivo(self, arquivo):
        self.arquivo = arquivo
        return os.path.splitext(self.arquivo)[1]

    def redireciona_extensao(self, extensao, arquivo, tipo_relatorio):
        invetory = Inventory()
        self.extensao = extensao
        self.arquivo = arquivo
        self.tipo_relatorio = tipo_relatorio
        if extensao == '.csv':
            invetory.executa_csv(self.arquivo, self.tipo_relatorio)
        if extensao == '.json':
            invetory.executa_json(self.arquivo, self.tipo_relatorio)
        if extensao == '.xml':
            invetory.executa_xml(self.arquivo, self.tipo_relatorio)

    def executa_csv(self, arquivo, tipo):
        self.arquivo = arquivo
        self.tipo = tipo
        with open(self.arquivo, 'r') as arq:
            reader = csv.DictReader(arq)
            for row in reader:
                self.stock.append(dict(row))

    def executa_xml(self, arquivo, tipo):
        self.arquivo = arquivo
        self.tipo = tipo
        xml = ET.parse(self.arquivo)
        print(self.arquivo)
        root = xml.getroot()

        for item in root.findall('record'):
            dic_xml = {}
            item_atributo = item.attrib
            dic_xml.update(item_atributo)
            for child in item:
                dic_xml[child.tag] = child.text
            self.stock.append(dic_xml)

    def executa_json(self, arquivo, tipo):
        self.arquivo = arquivo
        self.tipo = tipo
        with open(self.arquivo) as arq:
            reader = json.load(arq)
            for row in reader:
                self.stock.append(dict(row))

    def relatorio_simples(self):
        obj = SimpleReport()
        return obj.generate(self.stock)

    def relatorio_completo(self):
        obj = CompleteReport()
        return obj.generate(self.stock)
