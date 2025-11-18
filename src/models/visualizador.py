from utils.interfaces import Exibivel

class Visualizador(Exibivel):
    """Classe para geração de gráficos.
    Integrante C deve implementar:
    - exibir()
    """

    def __init__(self, df):
        self.df = df

    def exibir(self):
        pass
