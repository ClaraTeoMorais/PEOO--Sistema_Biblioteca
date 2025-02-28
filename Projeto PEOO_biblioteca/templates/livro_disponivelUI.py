import streamlit as st
import pandas as pd
from view import View
from datetime import datetime
from modelos.genero import Generos

class Livros_Disponiveis_UI:
    def main():
        st.header("Livros disponíveis para empréstimo")
        Livros_Disponiveis_UI.listar()

    def listar():
        livros = View.livro_listar()  
        emprestimos = View.emprestimo_listar() 
        generos = View.genero_listar() 

        # Criar um dicionário para contar quantos exemplares de cada livro estão emprestados
        emprestimos_por_livro = {}
        for e in emprestimos:
            if e.get_data_devolucao() > datetime.now():  # Apenas empréstimos não devolvidos
                emprestimos_por_livro[e.get_idLivro()] = emprestimos_por_livro.get(e.get_idLivro(), 0) + 1

        # Ajustar quantidade para o usuário
        livros_disponiveis = []
        for livro in livros:
            total_disponivel = livro.get_quantDisponivel() - emprestimos_por_livro.get(livro.get_id(), 0)
            if total_disponivel > 0:
                livros_disponiveis.append((livro, total_disponivel))

        pesquisa = st.text_input("Pesquisar pelo título, autor, gênero ou editora do livro:")

        if pesquisa:
            pesquisa = pesquisa.lower()
            genero_id = next((g.get_id() for g in generos if g.get_genero().lower() == pesquisa), None)

            livros_disponiveis = [
                (livro, qtd) for livro, qtd in livros_disponiveis
                if pesquisa in livro.get_livro().lower() or  
                   pesquisa in livro.get_autor().lower() or   
                   pesquisa in livro.get_editora().lower() or  
                   (genero_id is not None and livro.get_id_genero() == genero_id)
            ]

        if not livros_disponiveis:
            st.write("Nada foi encontrado")
        else:
            lista_formatada = []
            for livro, qtd_disponivel in livros_disponiveis:
                genero_obj = Generos.listar_id(livro.get_id_genero())
                nome_genero = genero_obj.get_genero() if genero_obj else "Gênero não encontrado"

                lista_formatada.append({
                    "Título": livro.get_livro(),
                    "Autor": livro.get_autor(),
                    "Gênero": nome_genero,
                    "Editora": livro.get_editora(),
                    "Ano": livro.get_ano(),
                    "Disponível": qtd_disponivel 
                })

            st.write("Livros Disponíveis:")
            df = pd.DataFrame(lista_formatada)
            st.dataframe(df)
