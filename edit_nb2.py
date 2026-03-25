import json

with open('01_exploracao.ipynb', 'r', encoding='utf-8') as f:
    nbs = f.read()

# Revert my previous partial fix if it exists
nbs = nbs.replace("iloc[:, 16], errors='coerce')", "iloc[:, 16], errors='coerce') / pd.to_numeric(df_raw.iloc[:, 5], errors='coerce')")
nbs = nbs.replace("iloc[:, 17], errors='coerce')", "iloc[:, 17], errors='coerce') / pd.to_numeric(df_raw.iloc[:, 6], errors='coerce')")
nbs = nbs.replace("iloc[:, 19], errors='coerce')", "iloc[:, 19], errors='coerce') / pd.to_numeric(df_raw.iloc[:, 7], errors='coerce')")

# Fix the prompt text just in case it wasn't fixed
nbs = nbs.replace("- Margem: Índice 12 (2025), 13 (2026), 15 (Orc).", "- Margem: Índice 16 (2025), 17 (2026), 19 (Orc) divididos pelo Faturamento.")

with open('01_exploracao.ipynb', 'w', encoding='utf-8') as f:
    f.write(nbs)
