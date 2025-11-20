# src/models/analise.py
import statistics

class Analise:
    def __init__(self, amostras):
        self.amostras = amostras

    def medias(self):
        return {
            "Glicose": statistics.mean([a.glicose for a in self.amostras]),
            "Proteina": statistics.mean([a.proteina for a in self.amostras]),
            "Colesterol": statistics.mean([a.colesterol for a in self.amostras])
        }

    def desvios(self):
        # statistics.stdev exige >=2 valores; tratar caso contrário
        def stdev_safe(vals):
            return statistics.stdev(vals) if len(vals) >= 2 else 0.0

        return {
            "Glicose": stdev_safe([a.glicose for a in self.amostras]),
            "Proteina": stdev_safe([a.proteina for a in self.amostras]),
            "Colesterol": stdev_safe([a.colesterol for a in self.amostras])
        }
