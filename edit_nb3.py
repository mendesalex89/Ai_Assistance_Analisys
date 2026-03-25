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
                "> \"Cria um gráfico de barras lado a lado (agrupadas) comparando a Marg_2025 (verde) e Marg_2026 (vermelho) por dia. \n",
                "> - Usa as barras `alpha=0.8`.\n",
                "> - Define o formato do eixo Y como percentagem (`mtick.PercentFormatter(1.0)`).\n",
                "> - **Dica extra de Blindagem**: Usa `indices = np.arange(len(df))` para posicionar as barras e no `plt.xticks` usa `df['Dia'].astype(str).tolist()` para garantir que o Matplotlib não dê erro com os dias vazios.\""
            ]
            cell['source'] = new_source

with open('01_exploracao.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)
