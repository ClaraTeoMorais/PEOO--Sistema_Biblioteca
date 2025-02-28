import streamlit as st
import pandas as pd
from view import View

class Livros_Indisponiveis_UI:
    def main():
        st.write("Livros indisponíveis para empréstimo")
        Livros_Indisponiveis_UI.listar()

    def listar():
        livros = View.livro_listar()
        emprestimos = View.emprestimo_listar() 

        # vai pegar os ids dos livros que estão emprestados
        livros_emprestados = {e.get_idLivro() for e in emprestimos if e.get_reserva()}

        # flitrar livros com solicitação de empréstimo (quantidade > 0, "e" está emprestados)
        solicitacoes = [
            livro for livro in livros 
            if livro.get_quantDisponivel() > 0 and livro.get_id() in livros_emprestados
        ]

        if not solicitacoes:
            st.write("Todos os livros estão disponíveis!")
        else:
            dic = [{"Título": livro.get_livro(), "Autor": livro.get_autor(), 
                    "Editora": livro.get_editora(), "Ano": livro.get_ano(), 
                    "Disponível": livro.get_quantDisponivel()} for livro in solicitacoes]

            df = pd.DataFrame(dic)
            st.dataframe(df)