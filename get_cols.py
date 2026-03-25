import pandas as pd
import sys

df = pd.read_excel('Cópia de Mapa diário.xlsx', sheet_name='Mapa diário', skiprows=6)
with open('cols_out.txt', 'w', encoding='utf8') as f:
    for i, col in enumerate(df.columns):
        f.write(f"{i}: {col}\n")
    
    # Also write a few rows of data from column 10 to 15
    f.write("\nData excerpt:\n")
    f.write(df.iloc[:5, 10:16].to_string())
