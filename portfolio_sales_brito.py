import streamlit as st

# CONFIGURAÇÕES INICIAIS
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
st.markdown('<div class="subtitle">Desenvolvedor Python | TI & Segurança | Projetos Interativos</div>', unsafe_allow_html=True)

# SOBRE MIM
st.subheader("👨‍💻 Sobre mim")
st.write("""
Sou Marcos Vinicius Sales de Brito, profissional formado em Tecnologia da Informação, com experiência em desenvolvimento de sistemas com Python, segurança patrimonial, automação de processos e suporte técnico. Possuo conhecimento em Streamlit, planilhas, organização de estudos e investimentos.
""")

# PROJETOS
st.subheader("🖥️ Projetos em Destaque")

projects = [
    {
        "title": "Painel @sales_brito",
        "desc": "Painel completo com abas de estudo (PMGO), investimentos integrados, tarefas, clima, senhas e atalhos. Visual profissional, seguro e responsivo.",
        "link": "https://salesbrito.streamlit.app"
    },
    {
        "title": "MegaMasters",
        "desc": "Simulador da Mega-Sena com sorteios automáticos, interface intuitiva e estatísticas. Feito com Streamlit.",
        "link": "https://megamasters.streamlit.app"
    },
    {
        "title": "Currículo Campeão",
        "desc": "Currículo profissional com objetivo otimizado, layout moderno e destaque para as habilidades em segurança e TI.",
        "link": "https://drive.google.com"  # Substitua com seu link real se desejar
    },
    {
        "title": "Portfólio Online",
        "desc": "Portfólio criado no Canva com design moderno, responsivo e pronto para apresentar em entrevistas ou redes sociais.",
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
- E-mail: SALESBRITO080@GMAIL.COM  
- WhatsApp: (61) 99691-8191  
- Instagram: @salesbrito_  
- Usuário: @Sales_brito  
""")
