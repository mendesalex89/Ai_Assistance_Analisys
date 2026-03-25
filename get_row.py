import pandas as pd
import json

df = pd.read_excel('Cópia de Mapa diário.xlsx', sheet_name='Mapa diário', skiprows=6)
row = df.iloc[1].to_dict()

# Convert NaN to string to make it JSON serializable
import math
cleaned_row = {str(k): (str(v) if isinstance(v, float) and math.isnan(v) else v) for k, v in row.items()}

with open('row_out.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_row, f, indent=2)
