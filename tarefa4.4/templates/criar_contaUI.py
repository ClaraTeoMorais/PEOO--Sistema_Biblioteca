import streamlit as st
from view import View
import time

class Criar_ContaUI:
    def main():
        st.header("Criar Conta no Sistema da Biblioteca")
        Criar_ContaUI.inserir()

    def inserir():
        nome = st.text_input("Informe seu nome")
        email = st.text_input("Informe seu e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            View.usuario_inserir(nome, email, senha)
            st.success("Conta criada com sucesso!")
            time.sleep(2)
            st.rerun()