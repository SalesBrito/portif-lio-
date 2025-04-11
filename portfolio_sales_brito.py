import streamlit as st

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Portfólio | Sales Brito", page_icon="💼", layout="wide")

# ESTILO PERSONALIZADO
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

# TÍTULO E SUBTÍTULO
st.markdown('<div class="main-title">Portfólio Profissional</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Desenvolvedor Python | Segurança | Soluções Digitais</div>', unsafe_allow_html=True)

# SOBRE MIM
st.subheader("👨‍💻 Sobre mim")
st.write("""
Sou Marcos Vinicius Sales de Brito, profissional formado em **Tecnologia da Informação** com forte atuação em desenvolvimento de sistemas, automações em Python e soluções de produtividade digital.

💡 Tenho experiência com:
- Desenvolvimento em **Python** (Streamlit, automações, dashboards)
- **JavaScript**, **HTML** e **CSS** para web
- Integrações com planilhas, bancos de dados e plataformas como Google Drive
- Segurança patrimonial e digital
- Suporte técnico, monitoramento e gestão de informações

Busco sempre entregar projetos funcionais, modernos e de alto impacto profissional.
""")

# PROJETOS
st.subheader("🖥️ Projetos em Destaque")

projects = [
    {
        "title": "Painel @sales_brito",
        "desc": "Painel completo de produtividade com estudos para concursos, finanças, tarefas, clima, senhas e atalhos. Acesso protegido e visual profissional.",
        "link": "https://salesbrito.streamlit.app"
    },
    {
        "title": "MegaMasters",
        "desc": "Simulador da Mega-Sena com sorteio automático, estatísticas e design interativo. Criado em Python com Streamlit.",
        "link": "https://megamasters.streamlit.app"
    },
    {
        "title": "AlfaProvas (em desenvolvimento)",
        "desc": "Sistema de geração e correção de provas com QR Code, painel de professor e portal do aluno. Projeto em andamento para escolas e cursinhos.",
        "link": ""
    }
]

for proj in projects:
    with st.container():
        st.markdown('<div class="project-box">', unsafe_allow_html=True)
        st.markdown(f'<div class="project-title">{proj["title"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="project-desc">{proj["desc"]}</div>', unsafe_allow_html=True)
        if proj["link"]:
            st.markdown(f'<div class="btn-link"><a href="{proj["link"]}" target="_blank">🔗 Acessar Projeto</a></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# CONTATO
st.subheader("📞 Contato")
st.write("""
- 📧 E-mail: SALESBRITO080@GMAIL.COM  
- 📱 WhatsApp: (61) 99691-8191  
- 📷 Instagram: [@salesbrito_](https://instagram.com/salesbrito_)  
- 👨‍💻 Usuário profissional: @Sales_brito  
""")
