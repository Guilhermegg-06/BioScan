# src/models/amostra.py
from src.utils.exceptions import ExcecaoAmostraInvalida

class Amostra:
    def __init__(self, id, glicose, proteina, colesterol):
        try:
            self.id = int(id)
            self.glicose = float(glicose)
            self.proteina = float(proteina)
            self.colesterol = float(colesterol)
        except Exception:
            raise ExcecaoAmostraInvalida("Valores inválidos na amostra.")

    def __repr__(self):
        return f"Amostra(ID={self.id}, G={self.glicose}, P={self.proteina}, C={self.colesterol})"
