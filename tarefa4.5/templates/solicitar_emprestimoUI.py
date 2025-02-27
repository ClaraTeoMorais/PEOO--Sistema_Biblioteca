import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from modelos.livro import Livros
from view import View
import time

class Solicitar_Emprestimo_usuario_UI:
    def main():
        st.header("Solicitar empréstimo")
        Solicitar_Emprestimo_usuario_UI.inserir()

    def inserir():
        livros = View.livro_listar()
        emprestimos = View.emprestimo_listar() 
        if not livros:
            st.write("Nenhum livro disponível")
            return
        
        # vai pegar os ids dos livros que estão emprestados
        livros_emprestados = {e.get_idLivro() for e in emprestimos if e.get_data_devolucao() > datetime.now()}

        # flitrar livros disponíveis (quantidade > 0, "e" não está emprestados)
        livros_disponiveis = [
            livro for livro in livros 
            if livro.get_quantDisponivel() > 0 and livro.get_id() not in livros_emprestados
        ]

        livro = st.selectbox("Selecione o livro", livros_disponiveis, format_func=lambda x: x.get_livro(), index=None)

        data_emprestimo = datetime.today()
        data_devolucao = data_emprestimo + timedelta(days=7)

        if st.button("Inserir"):
            if livro is None:
                st.error("Selecione um livro antes de continuar.")
            else:
                try:
                    View.emprestimo_inserir(
                        id_Livro=livro.get_id(),  
                        idUsuario=st.session_state["usuario_id"],
                        reserva=False,
                        data_emprestimo=data_emprestimo.strftime('%Y-%m-%d'),
                        data_devolucao=data_devolucao.strftime('%Y-%m-%d')
                    )
                    st.success("Empréstimo solicitado com sucesso, aguarde o administrador fazer a confirmação")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao solicitar empréstimo: {e}")