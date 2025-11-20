import csv
from pathlib import Path

p = Path("data") / "amostras.csv"
with p.open("r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
print("Linhas lidas:", len(rows))
print(rows[:3])
