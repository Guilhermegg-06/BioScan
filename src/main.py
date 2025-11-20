import pandas as pd
from src.models.amostra import Amostra
from src.models.analise import Analise
from src.models.interpretador import Interpretador
from src.models.visualizador import Visualizador
from src.utils.exceptions import ExcecaoAmostraInvalida

def main():
    print("=== BioScan – Sistema de Análise Científica ===")

    try:
        df = pd.read_csv("data/amostras.csv")

        # Criação das amostras
        amostras = []
        for _, row in df.iterrows():
            amostras.append(
                Amostra(
                    id=row["ID"],
                    glicose=row["Glicose"],
                    proteina=row["Proteina"],
                    colesterol=row["Colesterol"]
                )
            )

        print(f"[OK] {len(amostras)} amostras carregadas.")

        # Análise
        analise = Analise(amostras)
        medias = analise.medias()
        desvios = analise.desvios()

        print("\n=== Estatísticas Gerais ===")
        print("Médias:", medias)
        print("Desvios:", desvios)

        # Interpretação
        interpretador = Interpretador(amostras)
        resultados = interpretador.interpretar()

        print("\n=== Classificação das Amostras ===")
        for res in resultados:
            print(f"Amostra {res[0]} → {res[1]}")

        # Visualização
        visualizador = Visualizador(df)
        print("\nGerando gráficos...")
        visualizador.exibir()

    except ExcecaoAmostraInvalida as e:
        print(e)
    except FileNotFoundError:
        print("[ERRO] Arquivo amostras.csv não encontrado em /data.")
    except Exception as e:
        print("[ERRO GERAL]", e)

if __name__ == "__main__":
    main()
