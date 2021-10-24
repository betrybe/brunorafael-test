from collections.abc import Iterator


class InventoryIterator(Iterator):

    def __init__(self, data):
        self.data = data
        self.posicao = -1

    def __next__(self):
        try:
            self.posicao += 1
            return self.data[self.posicao]
        except IndexError:
            raise StopIteration()
