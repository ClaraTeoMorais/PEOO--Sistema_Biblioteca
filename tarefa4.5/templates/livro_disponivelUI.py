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
        livros = View.livro_listar()  # Obtém todos os livros
        emprestimos = View.emprestimo_listar()  # Obtém todos os empréstimos ativos
        generos = View.genero_listar()  # Obtém todos os gêneros cadastrados

        # Pega os IDs dos livros que estão emprestados no momento
        livros_emprestados = {e.get_idLivro() for e in emprestimos if e.get_data_devolucao() > datetime.now()}

        # Filtra os livros disponíveis (quantidade > 0 e não emprestados)
        livros_disponiveis = [
            livro for livro in livros
            if livro.get_quantDisponivel() > 0 and livro.get_id() not in livros_emprestados
        ]

        pesquisa = st.text_input("Pesquisar pelo título, autor, gênero, editora ou ano do livro:")

        if pesquisa:
            pesquisa = pesquisa.lower()
            # o .lower() deixa todas as letras minúsculas - p n dar problema na hora de filtrar

            genero_id = next((g.get_id() for g in generos if g.get_genero().lower() == pesquisa), None)
            # verifica se o q foi digitado é um genero -> se sim, pega o ID, se n, retorna a none
            # next() -> pega o primeiro valor encontrado

            # Filtra os livros de acordo com o que foi digitado
            livros_disponiveis = [
                livro for livro in livros_disponiveis
                if pesquisa in livro.get_livro().lower() or   # nome do livro contém termo pesquisado
                   pesquisa in livro.get_autor().lower() or   
                   pesquisa in livro.get_editora().lower() or  
                   pesquisa in livro.get_ano().lower() or  
                   (genero_id is not None and livro.get_id_genero() == genero_id)   # gênero do livro é o que foi pesquisado
            ]

        if not livros_disponiveis:
            st.write("Nada foi encontrado")
        else:
            d = []
            for obj in livros:
                obj_formatado = obj
                # Buscar o nome do gênero pelo ID 
                genero_obj = Generos.listar_id(obj.get_id_genero())
                nome_genero = genero_obj.get_genero() if genero_obj else "Gênero não encontrado"
                
                # Atualizar o objeto formatado com o nome do gênero
                obj_formatado.set_genero(nome_genero)
                
                # Adicionar o dicionário do objeto com o nome do gênero
                d.append(obj_formatado.__dict__)
            
            dic = [{
                "Título": livro.get_livro(),
                "Autor": livro.get_autor(),
                "Gênero": livro.get_id_genero(),
                "Editora": livro.get_editora(),
                "Ano": livro.get_ano(),
                "Disponível": livro.get_quantDisponivel()
            } for livro in livros_disponiveis]

            st.write("Livros Disponíveis:")
            df = pd.DataFrame(dic)
            st.dataframe(df)