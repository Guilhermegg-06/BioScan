from .amostra import Amostra

class Interpretador:
    def __init__(self):
        self.limite_glucose = 125
        self.limite_colesterol = 230

    def classificar(self, amostra: Amostra):
        if amostra.glucose_mg_dL > self.limite_glucose:
            return "alterado"

        if amostra.colesterol_mg_dL > self.limite_colesterol:
            return "alterado"

        return "normal"

    def classificar_lista(self, amostras):
        resultados = []
        for a in amostras:
            resultados.append({
                "id": a.id,
                "resultado": self.classificar(a)
            })
        return resultados
