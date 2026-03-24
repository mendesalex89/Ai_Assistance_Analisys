# Formação Vibe Coding PCG

## Passo 0: Instalar Python e plugins essenciais
- Baixe e instale o **Python 3.12+** marcando a opção "Add python.exe to PATH". (Download: https://www.python.org/downloads/)
- Instale o **Visual Studio Code** (ou abra o que já usa) e adicione as extensões: 
  - **Python** (Microsoft) – suporte à linguagem e depuração.
  - **Jupyter** – notebooks dentro do VS Code.
  - **Pylance** ou **IntelliCode** – autocompletar rápido.
  - (Opcional) **GitHub Copilot Chat** – para pedir passos por texto.

## Passo 1: Criar e Ativar o Ambiente Virtual

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

## Passo 2: Instalar pacotes e gerar o requirements.txt

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
pip install pandas numpy openpyxl pyarrow matplotlib seaborn plotly scikit-learn statsmodels
pip freeze > requirements.txt
```

> Dica: sempre rode `pip install` com o ambiente virtual ativado (`.venv\Scripts\activate`). Se não ativar, os pacotes irão para o Python global.

### Reinstalar tudo a partir do requirements.txt
Se já existe um `requirements.txt`, basta instalar em um novo ambiente com:
```bash
pip install -r requirements.txt
```
Isso garante que todos usem exatamente as mesmas versões listadas no arquivo.

## Passo 3: Criar o notebook Jupyter para a análise

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
