
import streamlit as st
from PIL import Image

# CONFIG
st.set_page_config(page_title="Portfólio | Sales Brito", page_icon="💼", layout="wide")

# HEADER
st.markdown("""
    <style>
        .main-title {font-size: 3em; font-weight: bold; color: #2E86C1; text-align: center; margin-bottom: 0.5em;}
        .subtitle {font-size: 1.5em; color: #555; text-align: center; margin-bottom: 2em;}
        .project-box {border: 1px solid #DDD; border-radius: 10px; padding: 1.5em; margin-bottom: 2em; background-color: #FAFAFA;}
        .project-title {font-size: 1.3em; font-weight: bold; color: #1A5276;}
        .project-desc {font-size: 1em; color: #333; margin-top: 0.5em;}
        .btn-link a {color: white; background-color: #2E86C1; padding: 0.5em 1em; border-radius: 5px; text-decoration: none;}
        .btn-link a:hover {background-color: #1A5276;}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Portfólio Profissional</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Desenvolvedor Python | TI & Segurança | Projetos Interativos</div>', unsafe_allow_html=True)

# SOBRE MIM
st.subheader("👨‍💻 Sobre mim")
st.write("""
Sou Marcos Vinicius Sales de Brito, formado em Tecnologia da Informação, com experiência em desenvolvimento com Python (Streamlit), suporte técnico e segurança patrimonial.

Criei soluções como o Painel @sales_brito e o MegaMasters, focadas em produtividade, automação e interatividade.
""")

# PROJETOS
st.subheader("🖥️ Projetos em Destaque")

with st.container():
    st.markdown('<div class="project-box">', unsafe_allow_html=True)
    st.markdown('<div class="project-title">Painel @sales_brito</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-desc">Plataforma pessoal e profissional com integração a estudos (PMGO), investimentos, tarefas, clima, senhas e muito mais.</div>', unsafe_allow_html=True)
    st.markdown('<div class="btn-link"><a href="https://salesbrito.streamlit.app" target="_blank">🔗 Acessar Painel</a></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="project-box">', unsafe_allow_html=True)
    st.markdown('<div class="project-title">MegaMasters</div>', unsafe_allow_html=True)
    st.markdown('<div class="project-desc">Simulador da Mega-Sena feito com Python e Streamlit, com visual moderno e funcional.</div>', unsafe_allow_html=True)
    st.markdown('<div class="btn-link"><a href="https://megamasters.streamlit.app" target="_blank">🔗 Acessar MegaMasters</a></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# CONTATO
st.subheader("📞 Contato")
st.write("""
- E-mail: SALESBRITO080@GMAIL.COM
- WhatsApp: (61) 99691-8191
- Instagram: @salesbrito_
- Usuário: @Sales_brito
""")
