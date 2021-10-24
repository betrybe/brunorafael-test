import os.path
from abc import ABC, abstractmethod


class Importer(ABC):

    @abstractmethod
    def import_data(nome_arquivo):
        pass

    @staticmethod
    def verifica_tipo_arquivo(arquivo):
        return os.path.splitext(arquivo)[1]
