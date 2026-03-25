import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# 1. Carregar os Dados
df = pd.read_excel('Cópia de Mapa diário.xlsx', skiprows=6)

# 2. Pegar as colunas
df_dash = df.iloc[:, [0, 1, 5, 16, 17]].copy()
df_dash.columns = ['Dia', 'Semana', 'Faturamento 25', 'Margem 25', 'Margem 26']

# 3. Conversões de limpeza
df_dash['Dia'] = df_dash['Dia'].astype(str)
df_dash.dropna(subset=['Dia'], inplace=True)
df_dash = df_dash[df_dash['Dia'] != 'nan']

# Garantir números
for col in ['Faturamento 25', 'Margem 25', 'Margem 26']:
    df_dash[col] = pd.to_numeric(df_dash[col], errors='coerce').fillna(0)

# 4. Transformar as Margens numa percentagem matemática 
def calc_perc(m, f):
    if f != 0:
        return m / f
    return 0

df_dash['Perc_Margem 25'] = df_dash.apply(lambda row: calc_perc(row['Margem 25'], row['Faturamento 25']), axis=1)
df_dash['Perc_Margem 26'] = df_dash.apply(lambda row: calc_perc(row['Margem 26'], row['Faturamento 25']), axis=1) # aproximação base

# 5. Interface da Aplicação
app = dash.Dash(__name__)

semanas_unicas = [s for s in df_dash['Semana'].unique() if pd.notna(s)]

app.layout = html.Div(style={'backgroundColor': '#111111', 'minHeight': '100vh', 'padding': '20px', 'fontFamily': 'Arial, sans-serif'}, children=[
    html.H1("Dashboard Financeiro Diário", style={'textAlign': 'center', 'color': '#00ffcc'}),
    
    html.Div([
        html.Label("Selecione as Semanas a rever:", style={'color': 'white'}),
        dcc.Dropdown(
            id='semana-dropdown',
            options=[{'label': f"{s}", 'value': s} for s in semanas_unicas],
            multi=True,
            value=semanas_unicas,
            style={'backgroundColor': 'white', 'color': 'black', 'marginTop': '10px'}
        )
    ], style={'width': '50%', 'margin': '0 auto', 'paddingBottom': '20px'}),
    
    html.Div(style={'display': 'flex', 'flexDirection': 'row', 'justifyContent': 'space-between', 'gap': '20px'}, children=[
        html.Div(dcc.Graph(id='grafico-faturamento', style={'height': '60vh'}), style={'width': '50%'}),
        html.Div(dcc.Graph(id='grafico-margens', style={'height': '60vh'}), style={'width': '50%'})
    ])
])

# Callbacks para fazer a página reagir aos filtros
@app.callback(
    [Output('grafico-faturamento', 'figure'),
     Output('grafico-margens', 'figure')],
    [Input('semana-dropdown', 'value')]
)
def update_graphs(semanas_selecionadas):
    if not semanas_selecionadas:
        dff = df_dash.copy()
    else:
        dff = df_dash[df_dash['Semana'].isin(semanas_selecionadas)]
        
    # Gráfico Esquerdo (Barras)
    fig1 = px.bar(dff, x='Dia', y='Faturamento 25', template='plotly_dark',
                  color_discrete_sequence=['#00ffcc'], title="Faturamento 25 por Dia (Baseado na Semana)")
    fig1.update_layout(paper_bgcolor='#222', plot_bgcolor='#222')
    
    # Gráfico Direito (Linhas das Margens Percentuais)
    dff_melt = dff.melt(id_vars='Dia', value_vars=['Perc_Margem 25', 'Perc_Margem 26'], 
                        var_name='Ano_Margem', value_name='Taxa Percentual')
                        
    fig2 = px.line(dff_melt, x='Dia', y='Taxa Percentual', color='Ano_Margem',
                   template='plotly_dark', color_discrete_sequence=['#ff00ff', '#00ffcc'],
                   title="Evolução da Taxa de Margem (%)")
    # formatar y as percentage
    fig2.update_layout(yaxis_tickformat='.1%', paper_bgcolor='#222', plot_bgcolor='#222')
                   
    return fig1, fig2

if __name__ == '__main__':
    app.run(debug=False, port=8050)
