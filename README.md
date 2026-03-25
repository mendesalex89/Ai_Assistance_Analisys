# Formação Vibe Coding PCG

Bem-vindo à **Formação Vibe Coding: Do Excel ao Python**! 🚀

Este treinamento interativo é o seu **guia de transição** para modernizar a forma de lidar com tabelas (como o seu *Mapa diário.xlsx*). O objetivo não é programar automações complexas do zero, mas sim ensinar a usar a **Inteligência Artificial** (Copilot/ChatGPT) para gerar e correr o código de forma simples e imediata (Vibe Coding).

⚠️ **O Verdadeiro Foco (Zero Automação Mágica)**: 
A inteligência artificial programa; cabe-lhe a si fazer o trabalho analítico! Este guia dá-lhe as bases sólidas (as famosas "Regras de Ouro") para saber organizar os prompts e pedir informações à IA com eficácia. A partir daí, tornar-se um especialista na ferramenta exigirá **muita exploração individual, treino diário e experiência profunda no terreno** com as suas próprias folhas de Excel.

### 🎯 **O que vamos cobrar nesta primeira etapa prática?**
Durante esta jornada inicial, vai aprender a:
- 🐍 **Preparar o Ambiente**: Configurar as ferramentas fundamentais (Python, VS Code, e Jupyter) em minutos.
- 🤖 **Interagir com IA Blindada**: Como criar _prompts_ bem construídos para o Chat entender a estrutura desarrumada e colunas escondidas das suas folhas de Excel.
- 📊 **Construir Visualizações em Código**: Substituir os filtros, tabelas dinâmicas e fórmulas de Margens do Excel, por uma simples ordem de texto em linguagem natural fornecida à IA, gerando Dashboards na hora.

A jornada para a **Análise Interativa com IA** começa aqui. Teste, explore as respostas do robô e descubra o poder dos dados!

---
## Passo 1: Instalar Python e plugins essenciais

Checklist rápido:
- Instalar **Python 3.12+** marcando "Add python.exe to PATH".
- Instalar **VS Code** (ou abrir o seu) e adicionar as extensões:
  - **Python** (Microsoft)
  - **Jupyter**
  - **Pylance** ou **IntelliCode**
  - (Opcional) **GitHub Copilot Chat**

Teste a instalação do Python no terminal:
```bash
python --version
pip --version
```

- Baixe e instale o **Python 3.12+** marcando a opção "Add python.exe to PATH". (Download: https://www.python.org/downloads/)
- Instale o **Visual Studio Code** (ou abra o que já usa) e adicione as extensões: 
  - **Python** (Microsoft) – suporte à linguagem e depuração.
  - **Jupyter** – notebooks dentro do VS Code.
  - **Pylance** ou **IntelliCode** – autocompletar rápido.
  - (Opcional) **GitHub Copilot Chat** – para pedir passos por texto.

## Passo 2: Criar e Ativar o Ambiente Virtual

Por que isso é fundamental: o ambiente virtual isola as bibliotecas deste treino, evita conflitos com outros projetos e facilita gerar o `requirements.txt` para todos terem as mesmas versões.

Podemos criá-lo de duas formas: pedindo à IA ou executando o comando diretamente.

**Opção A: Prompt curto para a IA**
```
Crie e ative um ambiente virtual Python chamado .venv neste projeto e mostre o comando de ativação.
```

**Opção B: Comando direto no terminal**
```bash
python -m venv .venv
```

Depois de criado, precisamos ativá-lo com o seguinte comando para que o terminal comece a usá-lo.

**Comando para ativar o ambiente (no Windows):**
```bash
.venv\Scripts\activate
```

## Passo 3: Instalar pacotes e gerar o requirements.txt

Por que isso é fundamental: ao registrar as versões em `requirements.txt`, garantimos que todos os analistas usem o mesmo conjunto de bibliotecas para Excel, gráficos e análises estatísticas.

Bibliotecas essenciais para este treino (descrição e docs):
- `pandas`  
  - Tabelas, limpeza e junções de dados tabulares.  
  - Docs: https://pandas.pydata.org
- `numpy`  
  - Cálculo vetorial/matriz; base numérica usada por outras libs.  
  - Docs: https://numpy.org
- `openpyxl`  
  - Ler e escrever arquivos `.xlsx` sem precisar do Excel instalado.  
  - Docs: https://openpyxl.readthedocs.io
- `pyarrow`  
  - I/O rápido para CSV/Parquet e integração com pandas.  
  - Docs: https://arrow.apache.org/docs/python/
- `matplotlib`  
  - Biblioteca base de gráficos 2D; controle fino de eixos e figuras.  
  - Docs: https://matplotlib.org
- `seaborn`  
  - Camada de alto nível sobre matplotlib para gráficos estatísticos com bom padrão visual.  
  - Docs: https://seaborn.pydata.org
- `plotly`  
  - Gráficos interativos (zoom, hover) para compartilhar em navegador ou notebooks.  
  - Docs: https://plotly.com/python/

**Opção A: Prompt curto para a IA**
```
No ambiente virtual ativo, instale pandas, numpy, openpyxl, pyarrow, matplotlib, seaborn, plotly. Depois gere um requirements.txt com as versões instaladas.
```

**Opção B: Comando direto no terminal**
```bash
pip install pandas numpy openpyxl pyarrow matplotlib seaborn plotly
pip freeze > requirements.txt
```

> Dica: sempre rode `pip install` com o ambiente virtual ativado (`.venv\Scripts\activate`). Se não ativar, os pacotes irão para o Python global.

### Reinstalar tudo a partir do requirements.txt
Se já existe um `requirements.txt`, basta instalar em um novo ambiente com:
```bash
pip install -r requirements.txt
```
Isso garante que todos usem exatamente as mesmas versões listadas no arquivo.

## Passo 4: Criar o notebook Jupyter para a análise

Por que isso é fundamental: o notebook é onde vamos fazer perguntas sobre os dados (Excel/CSV) e visualizar resultados rapidamente.

**Opção A: Prompt curto para a IA**
```
Crie um notebook Jupyter chamado 01_exploracao.ipynb nesta pasta, usando o ambiente virtual .venv, e abra-o para eu começar a escrever células.
```

**Opção B: Fazer direto no VS Code / terminal**
1) Ative o ambiente: `.venv\Scripts\activate`
2) No terminal: `code .` (abre a pasta no VS Code)  
   - No VS Code, clique em “New File” → escolha “Jupyter Notebook”, salve como `01_exploracao.ipynb`.
   - Alternativa via terminal: `python -m jupyter lab` e, no navegador, `File > New Notebook` (Python 3) e salve como `01_exploracao.ipynb`.

### Abrir o Jupyter no navegador

**Prompt para a IA abrir no browser**
```
Ative o .venv e abra o Jupyter Lab no navegador para mim.
```

**Manual (sem IA)**
```bash
.venv\Scripts\activate
python -m jupyter lab
```
Depois de rodar, abra o link que aparece no terminal (geralmente http://localhost:8888/lab). Feche o terminal para encerrar o servidor quando terminar.

## Passo 5: Carregar o Excel no notebook e fazer a primeira análise

Por que isso é fundamental: confirma que o ambiente está funcionando e mostra a equivalência entre o que fazíamos no Excel e no Python.

**Prepare o arquivo**  
Coloque a planilha de exemplo em `dados/exemplo.xlsx` (pode usar a cópia interna “Mapa diário”). Mantenha o repositório interno.

**Opção A: Prompt curto para a IA**
```
No notebook 01_exploracao.ipynb, carregue o arquivo dados/exemplo.xlsx na primeira aba, mostre as 5 primeiras linhas e faça um gráfico de barras com a coluna de faturação por dia.
```

**Opção B: Fazer direto no notebook**
1) Abra o `01_exploracao.ipynb` (Passo 4).  
2) Rode estas células iniciais:
```python
import pandas as pd

caminho = "dados/exemplo.xlsx"  # ajuste se usar outro nome
df = pd.read_excel(caminho, sheet_name=0)

df.head()
```
3) Gráfico simples (substitua `Dia` e `Faturação` pelos nomes reais das colunas):
```python
df.plot(kind="bar", x="Dia", y="Faturação", figsize=(10,4), title="Faturação por dia")
```
4) Salve o notebook após testar.







## Passo 6: Expandir para um Dashboard Interativo (Plotly + Dash)

Por que isso é fundamental: depois de limpar os dados e criar os primeiros gráficos estáticos num Notebook, o próximo grande salto de maturidade analítica é partilhar esses resultados de forma apelativa. O **Dash** (junto com o motor visual **Plotly**) permite criar aplicações web poderosas e altamente customizáveis, em que os diretores podem cruzar filtros, e interagir clicando nas barras ou nas margens. 

Aqui, em vez de codificar bloco a bloco, a forma mais rentável de trabalhar (Vibe Coding) é fornecer à Inteligência Artificial um **Briefing (Prompt)** muito cirúrgico com a estrutura exata do nosso Excel.

**Prompt Detalhado para criar o Dashboard (copie e cole no ChatGPT/Copilot):**

> Usa a linguagem Python e as bibliotecas `dash` e `plotly` para criar uma aplicação web chamada 'dashboard.py'. Usa tema escuro.  
> 
> **Requisitos do Carregamento de Dados:**
> 1. Carrega o ficheiro local `'Cópia de Mapa diário.xlsx'` do Microsoft Excel. Ignora as primeiras 6 linhas (`skiprows=6`).
> 2. Pega apenas nas seguintes colunas pelo índice `iloc`: 
>    - **Coluna 0**: 'Dia'
>    - **Coluna 1**: 'Semana'
>    - **Coluna 5**: 'Faturamento 25'
>    - **Coluna 16**: 'Margem 25'
>    - **Coluna 17**: 'Margem 26'
> 3. Converte essas métricas usando `pd.to_numeric(errors='coerce')` para limpar quaisquer aspas em branco. O 'Dia' mantém-se como string e descarta os campos 'Dia' vazios (`dropna(subset=['Dia'])`).  
> 4. Transforma as Margens numa percentagem matemática: (Margem 25 / Faturamento 25).
>     
> **Requisitos da Interface e Interatividade:**
> 5. Configura no topo 1 Título grande centrado: "Dashboard Financeiro Diário". Usar letra Arial ou Roboto e cores Neon.
> 6. Um `dcc.Dropdown` (filtros Múltiplos) para a pessoa poder escolher as Semanas e a página atualizar instantaneamente (`@app.callback`).
> 7. Abaixo cria 2 gráficos grandes lado a lado (estilo "flexbox" com 50% largura cada):
>    - **Gráfico 1 (Esquerda):** Gráfico de Barras do 'Faturamento 25' distribuído por 'Dia'. Barras de cor azul petróleo (`px.bar`, template='plotly_dark').
>    - **Gráfico 2 (Direita):** Gráfico de Linhas comparando a evolução a 2 anos da 'Margem 25' e 'Margem 26' também ao longo do 'Dia'.  
> 8. Certifica-te que incluis o final `if __name__ == '__main__': app.run_server(debug=True)`. Gera apenas o bloco de código limpo.

---
**Como Testar esta Magia no seu Computador:**
1. No seu terminal com o ambiente ativado (`.venv\Scripts\activate`), garanta as instalações: `pip install dash pandas openpyxl`
2. Num ficheiro novo chamado `dashboard.py` (ou dentro do Jupyter), cole a resposta gigante do Chat.
3. No terminal corra `python dashboard.py` e abra o endereço de internet que surgir (geralmente será algo como `http://127.0.0.1:8050`). Divirta-se a olhar para os seus dados a ganharem vida!

