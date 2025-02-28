import streamlit as st
from templates.solicitacoes_reservaUI import Solicitacoes_emprestimo_admin_UI
from templates.livro_disponivelUI import Livros_Disponiveis_UI
from templates.livros_emprestadosUI import Livros_Indisponiveis_UI
from templates.confirmar_devolucao import Confirmar_devolucao_UI

class Reserva_Adm_UI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Visualizar Reservas")
        tab1, tab2, tab3, tab4 = st.tabs(["Reservas pendentes", "Confirmar devolução", "Livros indisponíveis", "Livros disponíveis"])
        with tab1: Solicitacoes_emprestimo_admin_UI.main()
        with tab2: Confirmar_devolucao_UI.main()
        with tab3: Livros_Indisponiveis_UI.main()
        with tab4: Livros_Disponiveis_UI.main()
