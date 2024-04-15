from Corrida import Corrida
class Motorista:
    def __init__(self):
        self.corridas = []

    def add_corrida(self, corrida):
        self.corridas.append(corrida)

    def remove_corrida(self, corrida):
        self.corridas.remove(corrida)