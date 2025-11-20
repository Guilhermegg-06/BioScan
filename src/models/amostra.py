from dataclasses import dataclass

@dataclass
class Amostra:
    id: int
    idade: int
    sexo: str
    altura_cm: float
    peso_kg: float
    glucose_mg_dL: float
    colesterol_mg_dL: float

    def imc(self):
        h = self.altura_cm / 100
        return self.peso_kg / (h * h)
