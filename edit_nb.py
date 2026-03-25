import json

with open('01_exploracao.ipynb', 'r', encoding='utf-8') as f:
    nbs = f.read()

nbs = nbs.replace("- Margem: Índice 12 (2025), 13 (2026), 15 (Orc).", "- Margem: Índice 16 (2025), 17 (2026), 19 (Orc).")
nbs = nbs.replace("iloc[:, 12]", "iloc[:, 16]")
nbs = nbs.replace("iloc[:, 13]", "iloc[:, 17]")
nbs = nbs.replace("iloc[:, 15]", "iloc[:, 19]")

with open('01_exploracao.ipynb', 'w', encoding='utf-8') as f:
    f.write(nbs)
