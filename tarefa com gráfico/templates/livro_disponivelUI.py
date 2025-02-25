import streamlit as st
import pandas as pd
from view import View
from datetime import datetime

class Livros_Disponiveis_UI:
    def main():
        st.header("Livros disponíveis para empréstimo")
        Livros_Disponiveis_UI.listar()

    def listar():
        livros = View.livro_listar()
        emprestimos = View.emprestimo_listar() 

        # vai pegar os ids dos livros que estão emprestados
        livros_emprestados = {e.get_idLivro() for e in emprestimos if e.get_data_devolucao() > datetime.now()}

        # flitrar livros disponíveis (quantidade > 0, "e" não está emprestados)
        livros_disponiveis = [
            livro for livro in livros 
            if livro.get_quantDisponivel() > 0 and livro.get_id() not in livros_emprestados
        ]

        if not livros_disponiveis:
            st.write("Nenhum livro disponível no momento.")
        else:
            dic = [{"ID": livro.get_id(), "Título": livro.get_livro(), "Autor": livro.get_autor(), 
                    "Editora": livro.get_editora(), "Ano": livro.get_ano(), 
                    "Disponível": livro.get_quantDisponivel()} for livro in livros_disponiveis]

            df = pd.DataFrame(dic)
            st.dataframe(df)