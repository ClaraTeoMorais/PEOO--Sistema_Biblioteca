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
        if len(livros) == 0: 
            st.write("Nenhum livro cadastrado")
        else:    
            dic = []
            for obj in livros:
                obj_formatado = obj
                # Buscar o nome do gênero pelo ID
                genero_obj = Generos.listar_id(obj.get_id_genero())
                nome_genero = genero_obj.get_genero() if genero_obj else "Gênero não encontrado"
                
                # Atualizar o objeto formatado com o nome do gênero
                obj_formatado.set_genero(nome_genero)
                
                # Adicionar o dicionário do objeto com o nome do gênero
                dic.append(obj_formatado.__dict__)
            
            # Criar o DataFrame com a lista de dicionários
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        generos = View.genero_listar()
        livros = st.text_input("Informe o nome do livro")
        autor = st.text_input("Informe o autor do livro")
        genero = st.selectbox("Informe o gênero do livro", generos, index = None)
        editora = st.text_input("Informe a editora do livro")
        ano = st.text_input("Informe o ano que o livro foi publicado")
        quantidade = (st.text_input("Informe o quantidade de livros"))
        quantDisponivel = (st.text_input("Informe o quantidade de livros disponíveis"))

        if st.button("Inserir"):

            id_Genero = None
            if genero != None: id_Genero = genero.get_id()
            if livros == "":
                st.session_state["placeholder"] = "O campo não pode estar vazio!"
                st.error("Informe o livro")
                time.sleep(2)
                st.rerun()
            
            else:
                View.livro_inserir(livros, autor, id_Genero, editora, ano, quantidade, quantDisponivel)
                st.success("livro inserido com sucesso")
                time.sleep(2)
                st.rerun()
        
    def atualizar():
        livros = View.livro_listar()
        if len(livros) == 0: 
            st.write("Nenhum livro cadastrado")
        else:
            op = st.selectbox("Atualização de livro", livros)
            livro = st.text_input("Informe o novo nome do livro", op.get_livro())
            if st.button("Atualizar"):
                View.livro_atualizar(op.get_id(), livro)
                st.success("livro atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        livros = View.livro_listar()
        if len(livros) == 0: 
            st.write("Nenhum livro cadastrado")
        else:
            op = st.selectbox("Exclusão de livro", livros)
            if st.button("Excluir"):
                View.livro_excluir(op.get_id())
                st.success("livro excluído com sucesso")
                time.sleep(2)
                st.rerun()    