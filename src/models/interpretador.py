# src/models/interpretador.py
class Interpretador:
    def __init__(self, amostras):
        self.amostras = amostras

    def interpretar(self):
        resultados = []
        for a in self.amostras:
            if a.glicose > 125:
                status = "ALTO RISCO"
            elif a.glicose < 70:
                status = "BAIXO RISCO"
            else:
                status = "NORMAL"
            resultados.append((a.id, status))
        return resultados
