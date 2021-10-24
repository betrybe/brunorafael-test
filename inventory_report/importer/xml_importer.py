import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    stock = []

    def __init__(self):
        self.stock = []

    @staticmethod
    def import_data(nome_arquivo):
        extensao = Importer.verifica_tipo_arquivo(nome_arquivo)
        if extensao == '.xml':
            xmlImporter = XmlImporter()
            xml = ET.parse(nome_arquivo)
            root = xml.getroot()
            for item in root.findall('record'):
                dic_xml = {}
                item_atributo = item.attrib
                dic_xml.update(item_atributo)
                for child in item:
                    dic_xml[child.tag] = child.text
                xmlImporter.stock.append(dic_xml)
            return xmlImporter.stock
        else:
            raise ValueError("Arquivo inválido")
