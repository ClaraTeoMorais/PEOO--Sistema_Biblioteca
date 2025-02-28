import streamlit as st
import pandas as pd
from view import View
import time

class Manter_Genero_UI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Cadastro de Gênero")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: Manter_Genero_UI.listar()
        with tab2: Manter_Genero_UI.inserir()
        with tab3: Manter_Genero_UI.atualizar()
        with tab4: Manter_Genero_UI.excluir()

    def listar():
        generos = View.genero_listar()
        if len(generos) == 0: 
            st.write("Nenhum gênero cadastrado")
        else:    
            dic = [{
                "Gênero": g.get_genero(),
            } for g in generos]

            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        genero = st.text_input("Informe o nome do gênero")

        if st.button("Inserir"):
            if genero == "":
                st.session_state["placeholder"] = "O campo não pode estar vazio!"
                st.error("Informe o gênero")
                time.sleep(2)
                st.rerun()
            else:
                View.genero_inserir(genero)
                st.success("Gênero inserido com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        generos = View.genero_listar()
        if len(generos) == 0: 
            st.write("Nenhum gênero cadastrado")
        else:
            op = st.selectbox("Atualização de gênero", generos)
            genero = st.text_input("Informe o novo nome do gênero", op.get_genero())
            if st.button("Atualizar"):
                View.genero_atualizar(op.get_id(), genero)
                st.success("Gênero atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        generos = View.genero_listar()
        if len(generos) == 0: 
            st.write("Nenhum gênero cadastrado")
        else:
            op = st.selectbox("Exclusão de gênero", generos)
            if st.button("Excluir"):
                View.genero_excluir(op.get_id())
                st.success("Gênero excluído com sucesso")
                time.sleep(2)
                st.rerun()    