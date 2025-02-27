import streamlit as st
from view import View
from templates.solicitacoes_reservaUI import Solicitacoes_emprestimo_admin_UI
from templates.livro_disponivelUI import Livros_Disponiveis_UI
from templates.manter_emprestimoUI import Manter_Emprestimo_UI
from templates.livros_emprestadosUI import Livros_Indisponiveis_UI

class Reserva_Adm_UI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Visualizar Reservas")
        tab1, tab2, tab3, tab4 = st.tabs(["Reservas pendentes", "Confirmar reserva", "Livros indisponíveis", "Livros disponíveis"])
        with tab1: Solicitacoes_emprestimo_admin_UI.main()
        with tab2: Manter_Emprestimo_UI.atualizar()
        with tab3: Livros_Indisponiveis_UI.main()
        with tab4: Livros_Disponiveis_UI.main()
