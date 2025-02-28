import streamlit as st
import pandas as pd
from view import View
from modelos.livro import Livros

class Minhas_Reservas_UI:
    def main():
        st.header("Meus Empréstimos")
        Minhas_Reservas_UI.listar()

    def listar():
        emprestimos = View.emprestimo_listar()  

        usuario_logado = st.session_state["usuario_id"]
        emprestimos_usuario = [e for e in emprestimos if e.get_idUsuario() == usuario_logado]

        if not emprestimos_usuario:
            st.write("Você ainda não realizou nenhum empréstimo.")
        else:
            dados = []
            for obj in emprestimos_usuario: 
                livro_obj = Livros.listar_id(obj.get_idLivro())  
                
                nome_livro = livro_obj.get_livro() if livro_obj else "Livro não encontrado"
                
                dados.append({
                    "Livro": nome_livro,
                    "Reserva": obj.get_reserva(),
                    "Data Empréstimo": obj.get_data_emprestimo(),
                    "Data Devolução": obj.get_data_devolucao(),
                    "Devolução": obj.get_devolucao()
                })

            df = pd.DataFrame(dados)
            st.dataframe(df)