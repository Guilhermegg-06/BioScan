import csv
from src.models.amostra import Amostra
from src.models.analise import Analise
from src.models.interpretador import Interpretador

print(" Lendo CSV...")
amostras = []
with open("data/amostras.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for r in reader:
        a = Amostra(
            id=int(r['id']),
            idade=int(r['idade']),
            sexo=r['sexo'],
            altura_cm=float(r['altura_cm']),
            peso_kg=float(r['peso_kg']),
            glucose_mg_dL=float(r['glucose_mg_dL']),
            colesterol_mg_dL=float(r['colesterol_mg_dL'])
        )
        amostras.append(a)

print("👍 CSV carregado. Total de amostras:", len(amostras))

analise = Analise(amostras)
print("\n📊 Resumo da glucose:", analise.resumo("glucose_mg_dL"))

interp = Interpretador()
print("\n Classificação das 5 primeiras:")
for item in interp.classificar_lista(amostras)[:5]:
    print(item)
