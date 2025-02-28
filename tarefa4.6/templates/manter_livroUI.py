import streamlit as st
import pandas as pd
from modelos.genero import Generos
from view import View
import time

class Manter_Livro_UI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Cadastro de Livros")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: Manter_Livro_UI.listar()
        with tab2: Manter_Livro_UI.inserir()
        with tab3: Manter_Livro_UI.atualizar()
        with tab4: Manter_Livro_UI.excluir()
    
    def listar():
        livros = View.livro_listar()
        if not livros:
            st.write("Nenhum livro cadastrado")
            return

        dados = []
        for livro in livros:
            genero_obj = Generos.listar_id(livro.get_id_genero())
            nome_genero = genero_obj.get_genero() if genero_obj else "Gênero não encontrado"
            dados.append({
                "Título": livro.get_livro(),
                "Autor": livro.get_autor(),
                "Gênero": nome_genero,
                "Editora": livro.get_editora(),
                "Ano": livro.get_ano(),
                "Quantidade": livro.get_quantidade(),
                "Disponível": livro.get_quantDisponivel()
            })
        df = pd.DataFrame(dados)
        st.dataframe(df)
    
    def inserir():
        generos = View.genero_listar()
        livros = st.text_input("Informe o nome do livro")
        autor = st.text_input("Informe o autor do livro")
        genero = st.selectbox("Informe o gênero do livro", generos, format_func=lambda x: x.get_genero(), index=None)
        editora = st.text_input("Informe a editora do livro")
        ano = st.number_input("Informe o ano que o livro foi publicado", step=1, value=2000, max_value=2025)
        quantidade = st.number_input("Informe a quantidade de livros", step=1, min_value=0)
        quantDisponivel = st.number_input("Informe a quantidade de livros disponíveis", step=1, min_value=0)

        if st.button("Inserir"):
            id_Genero = genero.get_id() if genero else None
            if not livros:
                st.error("Informe o livro")
                time.sleep(2)
                st.rerun()
            else:
                View.livro_inserir(livros, autor, id_Genero, editora, ano, quantidade, quantDisponivel)
                st.success("Livro inserido com sucesso")
                time.sleep(2)
                st.rerun()
    
    def atualizar():
        livros = View.livro_listar()
        if not livros:
            st.write("Nenhum livro cadastrado")
            return

        op = st.selectbox("Atualização de livro", livros, format_func=lambda x: x.get_livro())
        generos = View.genero_listar()
        livro = st.text_input("Informe o novo nome do livro", op.get_livro())
        autor = st.text_input("Informe o novo autor do livro", op.get_autor())
        genero = st.selectbox("Informe o novo gênero do livro", generos, format_func=lambda x: x.get_genero(), index=None)
        editora = st.text_input("Informe a nova editora do livro", op.get_editora())
        ano = st.number_input("Informe o novo ano que o livro foi publicado", step=1, value=int(op.get_ano()), max_value=2025)
        quantidade = st.number_input("Informe a nova quantidade de livros", step=1, min_value=0, value=int(op.get_quantidade()))
        quantDisponivel = st.number_input("Informe a nova quantidade de livros disponíveis", step=1, min_value=0, value=int(op.get_quantDisponivel()))

        if st.button("Atualizar"):
            id_Genero = genero.get_id() if genero else None
            View.livro_atualizar(op.get_id(), livro, autor, id_Genero, editora, ano, quantidade, quantDisponivel)
            st.success("Livro atualizado com sucesso")
            time.sleep(2)
            st.rerun()
    
    def excluir():
        livros = View.livro_listar()
        if not livros:
            st.write("Nenhum livro cadastrado")
            return

        op = st.selectbox("Exclusão de livro", livros, format_func=lambda x: x.get_livro())

        if st.button("Excluir"):
            View.livro_excluir(op.get_id())
            st.success("Livro excluído com sucesso")
            time.sleep(2)
            st.rerun()
