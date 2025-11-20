# src/models/visualizador.py
import matplotlib.pyplot as plt

class Visualizador:
    def __init__(self, df):
        self.df = df

    def exibir(self):
        # Plota as colunas numéricas (Glicose, Proteina, Colesterol)
        try:
            self.df.plot(kind="line", title="Glicose, Proteína e Colesterol")
            plt.show()
        except Exception as e:
            print("[AVISO] Não foi possível gerar o gráfico:", e)
