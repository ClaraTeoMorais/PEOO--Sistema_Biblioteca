import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from modelos.livro import Livros
from view import View
import time

class Manter_Emprestimo_UI:
    def main():
        st.header("Cadastro de Empréstimos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: Manter_Emprestimo_UI.listar()
        with tab2: Manter_Emprestimo_UI.inserir()
        with tab3: Manter_Emprestimo_UI.atualizar()
        with tab4: Manter_Emprestimo_UI.excluir()

    def listar():
        emprestimos = View.emprestimo_listar()
        if not emprestimos: 
            st.write("Nenhum empréstimo cadastrado")
            return

        dados = []
        for obj in emprestimos:
            livro_obj = Livros.listar_id(obj.get_idLivro())
            nome_livro = livro_obj.get_livro() if livro_obj else "Livro não encontrado"
            dados.append({
                "ID": obj.get_id(),
                "Livro": nome_livro,
                "Usuário": obj.get_idUsuario(),
                "Reserva": obj.get_reserva(),
                "Data Empréstimo": obj.get_data_emprestimo(),
                "Data Devolução": obj.get_data_devolucao()
            })
        
        df = pd.DataFrame(dados)
        st.dataframe(df)

    def inserir():
        livros = View.livro_listar()
        usuarios = View.usuario_listar()
        if not livros:
            st.write("Nenhum livro disponível")
            return
        if not usuarios:
            st.write("Nenhum usuário disponível")
            return

        livro = st.selectbox("Selecione o livro", livros, format_func=lambda x: x.get_livro(), index=None)
        usuario = st.selectbox("Selecione o usuário", usuarios, format_func=lambda x: x.get_nome(), index=None)
        reserva = st.checkbox("Reserva")

        data_emprestimo = datetime.today()
        data_devolucao = data_emprestimo + timedelta(days=7)

        if st.button("Inserir"):
            if livro is None or usuario is None:
                st.error("Selecione um livro e um usuário antes de continuar.")
            else:
                try:
                    View.emprestimo_inserir(
                        id_Livro=livro.get_id(),  
                        idUsuario=usuario.get_id(),
                        reserva=reserva,
                        data_emprestimo=data_emprestimo.strftime('%Y-%m-%d'),
                        data_devolucao=data_devolucao.strftime('%Y-%m-%d')
                    )
                    st.success("Empréstimo cadastrado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao inserir empréstimo: {e}")

    def atualizar():
        emprestimos = View.emprestimo_listar()
        if not emprestimos:
            st.write("Nenhum empréstimo cadastrado")
            return

        op = st.selectbox("Selecione o empréstimo para atualizar", emprestimos, format_func=lambda x: f"{x.get_id()} - {x.get_idLivro()} - {x.get_idUsuario()}" )

        nova_data_devolucao = datetime.combine(st.date_input("Nova data de devolução", datetime.today() + timedelta(days=7)), datetime.min.time())
        reserva = st.checkbox("Confirmação de reserva")

        #O combine serve para adicionar um horário

        if st.button("Atualizar"):
            try:
                View.emprestimo_atualizar(
                    op.get_id(),
                    op.get_idLivro(),
                    op.get_idUsuario(),
                    reserva,
                    op.get_data_emprestimo(),
                    nova_data_devolucao.strftime('%d/%m/%Y %H:%M')
                )
                st.success("Empréstimo atualizado com sucesso")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao atualizar empréstimo: {e}")


    def excluir():
        emprestimos = View.emprestimo_listar()
        if not emprestimos:
            st.write("Nenhum empréstimo cadastrado")
            return

        op = st.selectbox("Selecione o empréstimo para excluir", emprestimos, format_func=lambda x: f"{x.get_id()} - {x.get_idLivro()} - {x.get_idUsuario()}" )

        if st.button("Excluir"):
            try:
                View.emprestimo_excluir(op.get_id())
                st.success("Empréstimo excluído com sucesso")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao excluir empréstimo: {e}")