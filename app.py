import streamlit as st
import re
import json

st.set_page_config(page_title="Formação Vibe Coding PCG", page_icon="🚀", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap');
html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
}
p, li { font-size: 1.15rem; line-height: 1.6; color: #cbd5e1; }
code {
    background-color: #1A202C !important;
    color: #38bdf8 !important;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-size: 1.05rem;
}
.stCodeBlock { border: 1px solid #1e293b; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
div[data-testid="stSidebar"] { border-right: 1px solid #1e293b; box-shadow: 4px 0 10px rgba(0,0,0,0.5); }
h1 { color: #f8fafc !important; }
h2, h3 { color: #00d2ff !important; margin-top: 1.5rem !important; }
.step-card {
    background: #1e293b;
    border-radius: 10px;
    padding: 14px 12px;
    margin: 4px 0;
    text-align: center;
    border: 1px solid #334155;
    height: 90px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.image(
    "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=400&auto=format&fit=crop",
    use_container_width=True
)
st.sidebar.markdown(
    "<h2 style='text-align: center; color: #00d2ff;'>🚀 Vibe Coding PCG</h2>",
    unsafe_allow_html=True
)
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

REFERENCIA_KEY = "📋 Referência Rápida de Prompts"
opcoes_menu = ["🏠 Introdução"] + [f"📍 {titulo}" for titulo in passos.keys()] + [REFERENCIA_KEY]
total_passos = len(passos)

escolha_raw = st.sidebar.radio("Navegação do Treinamento:", opcoes_menu, key="nav_radio")

# Barra de progresso na sidebar (apenas nos passos)
if escolha_raw not in ("🏠 Introdução", REFERENCIA_KEY):
    idx_passo = opcoes_menu.index(escolha_raw)
    st.sidebar.progress(idx_passo / total_passos, text=f"Progresso: {idx_passo}/{total_passos} passos")


# ── Introdução ──────────────────────────────────────────────────────────────
if escolha_raw == "🏠 Introdução":
    st.markdown(introducao)

    st.markdown("---")
    st.markdown("### 🗺️ Mapa da Jornada")

    passos_list = list(passos.keys())
    cols = st.columns(4)
    for i, titulo in enumerate(passos_list):
        label = titulo.split(": ", 1)[-1][:40]
        numero = i + 1
        with cols[i % 4]:
            st.markdown(
                f"<div class='step-card'>"
                f"<b style='color:#00d2ff; font-size:1.1rem;'>Passo {numero}</b>"
                f"<br><small style='color:#94a3b8;'>{label}</small>"
                f"</div>",
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚀 Começar — Ir para o Passo 1", type="primary", use_container_width=True):
        st.session_state["nav_radio"] = opcoes_menu[1]
        st.rerun()


# ── Referência Rápida ────────────────────────────────────────────────────────
elif escolha_raw == REFERENCIA_KEY:
    st.markdown(
        "<h1 style='color:#f8fafc; font-weight: 600;'>📋 Referência Rápida de Prompts</h1>",
        unsafe_allow_html=True
    )
    st.markdown("Revisão de todas as **Regras de Ouro** e Prompts Blindados presentes no nosso Notebook base:")
    st.markdown("\n\n---\n\n" + parse_notebook_prompts())


# ── Passos ───────────────────────────────────────────────────────────────────
else:
    titulo_real = escolha_raw[2:].strip()
    idx_atual = opcoes_menu.index(escolha_raw)

    st.markdown(
        f"<h1 style='color:#f8fafc; font-weight: 600;'>{titulo_real}</h1>",
        unsafe_allow_html=True
    )
    st.markdown(passos[titulo_real])

    st.markdown("<br><br><hr style='border: 1px solid #1e293b;'>", unsafe_allow_html=True)

    # Conclusão do módulo
    st.markdown("<h3 style='color: #94a3b8;'>Progresso do Módulo</h3>", unsafe_allow_html=True)
    if st.checkbox(f"✅ Eu completei as instruções práticas do módulo **{titulo_real}**!"):
        st.success("🎉 **Trabalho Fantástico!** Continua o excelente ritmo avançando para o próximo tópico no menu.")
        st.balloons()

    # Navegação anterior / próximo
    st.markdown("<br>", unsafe_allow_html=True)
    col_prev, col_spacer, col_next = st.columns([1, 2, 1])

    with col_prev:
        if idx_atual > 1:
            label_prev = opcoes_menu[idx_atual - 1][2:].strip()
            if st.button(f"⬅️ {label_prev[:28]}", use_container_width=True):
                st.session_state["nav_radio"] = opcoes_menu[idx_atual - 1]
                st.rerun()

    with col_next:
        proximo_idx = idx_atual + 1
        if proximo_idx < len(opcoes_menu):
            label_next = opcoes_menu[proximo_idx][2:].strip()
            if st.button(f"➡️ {label_next[:28]}", type="primary", use_container_width=True):
                st.session_state["nav_radio"] = opcoes_menu[proximo_idx]
                st.rerun()
