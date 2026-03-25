import streamlit as st
import re
import os
import json

st.set_page_config(page_title="Formação Vibe Coding PCG", page_icon="🚀", layout="wide")

st.sidebar.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=400&auto=format&fit=crop", use_container_width=True)

st.sidebar.markdown("<h2 style='text-align: center; color: #00d2ff;'>🚀 Vibe Coding PCG</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")

def parse_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        st.error("O ficheiro README.md não foi encontrado.")
        return "", {}

    parts = re.split(r'\n## ', content)
    
    introducao = parts[0]
    passos = {}
    
    for section in parts[1:]:
        lines = section.split('\n')
        titulo = lines[0].strip()
        corpo = "\n".join(lines[1:])
        passos[titulo] = corpo
        
    return introducao, passos

def parse_notebook_prompts():
    try:
        with open("01_exploracao.ipynb", "r", encoding="utf-8") as f:
            nb = json.load(f)
    except FileNotFoundError:
        return "Notebook não encontrado."
        
    markdown_content = []
    for cell in nb.get('cells', []):
        if cell['cell_type'] == 'markdown':
            source = "".join(cell.get('source', []))
            markdown_content.append(source)
            markdown_content.append("\n\n---\n\n")
    
    return "".join(markdown_content)

introducao, passos = parse_readme()

if not passos:
    st.stop()

# Menus de Navegação com ícones
opcoes_menu = ["🏠 Introdução"] + [f"📍 {titulo}" for titulo in passos.keys()] + ["📓 Regras e Prompts Jupyter"]
escolha_raw = st.sidebar.radio("Navegação do Treinamento:", opcoes_menu)

# Custom CSS para afinar detalhes como fontes modernas e blocos de código
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');
html, body, [class*="css"]  {
    font-family: 'Outfit', sans-serif;
}
p, li { font-size: 1.15rem; line-height: 1.6; color: #cbd5e1; }
code {
    background-color: #1A202C !important;
    color: #38bdf8 !important;   /* Azul claro para comandos terminal/inline */
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-size: 1.05rem;
}
/* Arredondamento dos códigos grandes e do painel lateral */
.stCodeBlock { border: 1px solid #1e293b; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
div[data-testid="stSidebar"] { border-right: 1px solid #1e293b; box-shadow: 4px 0 10px rgba(0,0,0,0.5); }
/* Título nas abas */
h1 { color: #f8fafc !important; }
h2, h3 { color: #00d2ff !important; margin-top: 1.5rem !important;}
</style>
""", unsafe_allow_html=True)

if escolha_raw == "🏠 Introdução":
    st.markdown(introducao)
    st.info("👈 **Para iniciar a sua jornada de forma prática**, use a barra lateral e clique no **Passo 1**!")


elif escolha_raw == "📓 Regras e Prompts Jupyter":
    st.markdown("<h1 style='color:#f8fafc; font-weight: 600;'>📓 Regras e Prompts Jupyter</h1>", unsafe_allow_html=True)
    st.markdown("Revisão de todas as **Regras de Ouro** e Prompts Blindados presentes no nosso Notebebook base:")
    st.markdown("\n\n---\n\n" + parse_notebook_prompts())

else:
    titulo_real = escolha_raw[2:].strip()
    st.markdown(f"<h1 style='color:#f8fafc; font-weight: 600;'>{titulo_real}</h1>", unsafe_allow_html=True)
    
    texto_pagina = passos[titulo_real]
    
    # Renderizar conteúdo principal
    st.markdown(texto_pagina)
    
    st.markdown("<br><br><hr style='border: 1px solid #1e293b;'>", unsafe_allow_html=True)
    
    # Gamification and feedback
    st.markdown("<h3 style='color: #94a3b8;'>Progresso do Módulo</h3>", unsafe_allow_html=True)
    if st.checkbox(f"✅ Eu completei as instruções práticas do módulo **{titulo_real}**!"):
        st.success("🎉 **Trabalho Fantástico!** Continua o excelente ritmo avançando para o próximo tópico no menu.")
        st.balloons()
