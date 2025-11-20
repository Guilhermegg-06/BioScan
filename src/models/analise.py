from typing import List
from .amostra import Amostra
import statistics

class Analise:
    def __init__(self, amostras: List[Amostra]):
        self.amostras = amostras

    def media(self, campo):
        valores = [getattr(a, campo) for a in self.amostras]
        return statistics.mean(valores)

    def minimo(self, campo):
        valores = [getattr(a, campo) for a in self.amostras]
        return min(valores)

    def maximo(self, campo):
        valores = [getattr(a, campo) for a in self.amostras]
        return max(valores)

    def resumo(self, campo):
        return {
            "media": self.media(campo),
            "min": self.minimo(campo),
            "max": self.maximo(campo)
        }
