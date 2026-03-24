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
