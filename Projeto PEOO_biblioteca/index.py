from templates.manter_emprestimoUI import Manter_Emprestimo_UI
from templates.manter_generoUI import Manter_Genero_UI
from templates.manter_livroUI import Manter_Livro_UI
from templates.manter_usuarioUI import Manter_Usuario_UI
from templates.livro_disponivelUI import Livros_Disponiveis_UI
from templates.solicitar_emprestimoUI import Solicitar_Emprestimo_usuario_UI
from templates.grafico_livrosUI import Livros_pelo_Genero_UI
from templates.criar_contaUI import Criar_ContaUI
from templates.loginUI import LoginUI
from templates.visualizar_reservas_admUI import Reserva_Adm_UI
from templates.minhas_reservasUI import Minhas_Reservas_UI
from view import View

import streamlit as st

# MENUS

class IndexUI: 
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Criar Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Criar Conta": Criar_ContaUI.main()
               
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Gêneros", "Cadastro de Livros", "Cadastro de Usuários", "Cadastro de Empréstimo", "Visualizar Reservas", "Gráfico de livros pelo gênero"])
        if op == "Cadastro de Gêneros": Manter_Genero_UI.main()
        if op == "Cadastro de Livros": Manter_Livro_UI.main()
        if op == "Cadastro de Usuários": Manter_Usuario_UI.main()
        if op == "Cadastro de Empréstimo": Manter_Emprestimo_UI.main()
        if op == "Visualizar Reservas": Reserva_Adm_UI.main()
        if op == "Gráfico de livros pelo gênero": Livros_pelo_Genero_UI.main()


    def menu_usuario():
        op = st.sidebar.selectbox("Menu", ["Livros Disponíveis", "Solicitar Empréstimo", "Meus Empréstimos", "Gráfico de livros pelo gênero"])
        if op == "Livros Disponíveis": Livros_Disponiveis_UI.main()
        if op == "Solicitar Empréstimo": Solicitar_Emprestimo_usuario_UI.main()
        if op == "Meus Empréstimos": Minhas_Reservas_UI.main()
        if op == "Gráfico de livros pelo gênero": Livros_pelo_Genero_UI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"] #se n funcioar, testar get_id()
            del st.session_state["usuario_nome"]
            st.rerun()
    
    def sidebar():
        if "usuario_id" not in st.session_state:  # verifica se há algum usuário logado
            IndexUI.menu_visitante()  # caso não senha, irá abrir o menu do visitante

        else:  # usuário está logado
            admin = st.session_state["usuario_nome"] == "Admin"  # poder verificar se é o admin logado 
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])  # mensagen de bem-vindo
            
            if admin:
                IndexUI.menu_admin()
            else: 
                IndexUI.menu_usuario()
                
            # controle de sair do sistema
            IndexUI.sair_do_sistema() 
    
    def main():
        View.usuario_admin() # cria o admin
        IndexUI.sidebar() # monta o sidebar
       
IndexUI.main()