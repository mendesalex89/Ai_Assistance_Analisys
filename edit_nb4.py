import json

with open('01_exploracao.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = "".join(cell['source'])
        if 'Célula 4: Análise de Margem' in source:
            new_source = [
                "### Célula 4: Análise de Margem (Gráfico de Barras)\n",
                "\n",
                "**Excel**: Verificação de rentabilidade.\n",
                "\n",
                "**Prompt sugerido para a IA (BLINDAGEM)**:\n",
                "> \"Cria um gráfico de barras lado a lado comparando a Marg_2025 (verde) e Marg_2026 (vermelho) por dia. \n",
                "> - O eixo Y deve estar em formato de percentagem.\n",
                "> - **Dica para a IA não falhar**: Atenção que a coluna 'Dia' tem valores vazios. Força o eixo dos dias (X) a ser texto (string) e agrupa as barras usando posições numéricas, para que o gráfico não fique desconfigurado ou dê erro.\""
            ]
            cell['source'] = new_source

with open('01_exploracao.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)
