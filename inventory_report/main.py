import os.path
import sys

from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) == 3:
        _, arquivo, tp_relatorio = sys.argv
        extensao = verifica_tipo_arquivo(arquivo)
        importer = retornaImporter(extensao)
        if importer != '':
            inventoryRefactor = InventoryRefactor(importer)
            report = inventoryRefactor.import_data(arquivo, tp_relatorio)
            print(report, end="")
    else:
        print("Verifique os argumentos", file=sys.stderr)
        return


def verifica_tipo_arquivo(arquivo):
    arquivo = arquivo
    return os.path.splitext(arquivo)[1]


def retornaImporter(extensao):
    importer = ''
    if extensao == '.csv':
        importer = CsvImporter()
    if extensao == '.json':
        importer = JsonImporter()
    if extensao == '.xml':
        importer = XmlImporter()
    return importer
