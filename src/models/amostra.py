class Amostra:
    """Classe que representa uma amostra biológica.
    Integrante B deve implementar futuras validações se necessário.
    """
    def __init__(self, id, glicose, proteina, colesterol):
        self.id = id
        self.glicose = glicose
        self.proteina = proteina
        self.colesterol = colesterol
