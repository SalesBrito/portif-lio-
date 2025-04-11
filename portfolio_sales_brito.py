import streamlit as st

# CONFIG
st.set_page_config(page_title="Portfólio | Sales Brito", page_icon="💼", layout="wide")

# ESTILO
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

# TÍTULO
st.markdown('<div class="main-title">Portfólio Profissional</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Desenvolvedor Python | Segurança | Projetos Interativos</div>', unsafe_allow_html=True)

# SOBRE MIM
st.subheader("👨‍💻 Sobre mim")
st.write("""
Sou Marcos Vinicius Sales de Brito, desenvolvedor com formação em Tecnologia da Informação e experiência em segurança, suporte técnico e criação de sistemas personalizados.

Tenho foco em soluções práticas, com domínio em:

- Python (Streamlit, automações, integração com planilhas)
- JavaScript e HTML (projetos web e interfaces)
- Excel Avançado, Banco de Dados e Dashboards
- Organização de estudos, investimentos e controle financeiro

Sou criador de plataformas como o **Painel @sales_brito** e o sistema **AlfaProvas**, voltadas à produtividade, educação e inovação digital.
""")

# PROJETOS
st.subheader("🖥️ Projetos em Destaque")

projects = [
    {
        "title": "Painel @sales_brito",
        "desc": "Painel completo com organização de estudos (PMGO), investimentos integrados, tarefas, clima, senhas e atalhos. Visual profissional e seguro.",
        "link": "https://salesbrito.streamlit.app"
    },
    {
        "title": "MegaMasters",
        "desc": "Simulador da Mega-Sena com sorteios automáticos, estatísticas e interface interativa. Desenvolvido em Python com Streamlit.",
        "link": "https://megamasters.streamlit.app"
    },
    {
        "title": "AlfaProvas",
        "desc": "Sistema completo de criação e correção de provas com QR Code, painel de professor e portal do aluno. Ideal para escolas e cursinhos.",
        "link": "https://alfa-provas-demo.streamlit.app/"  # Substitua se mudar o domínio
    },
    {
        "title": "Portfólio Online (PDF)",
        "desc": "Versão visual do portfólio criada no Canva. Design moderno e ideal para apresentar em entrevistas e redes sociais.",
        "link": "https://www.canva.com/design/DAGkU_qyLM4/r8Uu1LR8ThOtVbpmpsr9xQ/edit"
    }
]

for proj in projects:
    with st.container():
        st.markdown('<div class="project-box">', unsafe_allow_html=True)
        st.markdown(f'<div class="project-title">{proj["title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="project-desc">{proj["desc"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="btn-link"><a href="{proj["link"]}" target="_blank">🔗 Acessar Projeto</a></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# CONTATO
st.subheader("📞 Contato")
st.write("""
- 📧 E-mail: SALESBRITO080@GMAIL.COM  
- 📱 WhatsApp: (61) 99691-8191  
- 📷 Instagram: @salesbrito_  
- 🧑‍💼 Usuário profissional: @Sales_brito  
""")
