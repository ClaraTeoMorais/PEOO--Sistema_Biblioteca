import streamlit as st
from view import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema da Biblioteca")
        email = st.text_input("Informe seu e-mail")
        senha = st.text_input("Informe sua senha", type="password")
        if st.button("Entrar"):
            u = View.usuario_autenticar(email, senha)
            if u == None: 
                st.write("E-mail ou senha inválidos")
            else:
                st.session_state["usuario_id"] = u["id"]
                st.session_state["usuario_nome"] = u["nome"]
                st.rerun()