import streamlit as st
import pandas as pd
from view import View
import time

class Manter_Usuario_UI:
    def main():
        if "placeholder" not in st.session_state: 
            st.session_state["placeholder"] = ""
        st.header("Cadastro de Usuário")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: Manter_Usuario_UI.listar()
        with tab2: Manter_Usuario_UI.inserir()
        with tab3: Manter_Usuario_UI.atualizar()
        with tab4: Manter_Usuario_UI.excluir()

    def listar():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0: 
            st.write("Nenhum usuário cadastrado")
        else:    
            dic = []
            for obj in usuarios: 
                dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        nome = st.text_input("Informe o nome do cliente", placeholder = st.session_state["placeholder"])
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Inserir"):
            if nome == "":
                st.session_state["placeholder"] = "O campo não pode estar vazio!"
                st.error("Informe o nome")
                time.sleep(2)
                st.rerun()
            else:
                View.usuario_inserir(nome, email, senha)
                st.success("Usuário inserido com sucesso")
                time.sleep(2)
                st.rerun()

    def atualizar():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0: 
            st.write("Nenhum usuário cadastrado")
        else:
            op = st.selectbox("Atualização de usuário", usuarios)
            nome = st.text_input("Informe o novo nome do usuário", op.get_nome())
            email = st.text_input("Informe o novo e-mail", op.get_email())
            senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
            if st.button("Atualizar"):
                View.usuario_atualizar(op.get_id(), nome, email, senha)
                st.success("Usuário atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        usuarios = View.usuario_listar()
        if len(usuarios) == 0: 
            st.write("Nenhum usuário cadastrado")
        else:
            op = st.selectbox("Exclusão de usuário", usuarios)
            if st.button("Excluir"):
                View.usuario_excluir(op.get_id())
                st.success("Usuário excluído com sucesso")
                time.sleep(2)
                st.rerun()