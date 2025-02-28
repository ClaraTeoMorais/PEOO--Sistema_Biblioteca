import streamlit as st
import pandas as pd
from view import View
from datetime import datetime, timedelta
from modelos.livro import Livros
import time

class Confirmar_devolucao_UI:
    def main():
        st.write("Confirmação de devolução")
        Confirmar_devolucao_UI.atualizar()


    def formatar_emprestimo(emprestimo):
        livro_obj = Livros.listar_id(emprestimo.get_idLivro())
        usuario_obj = View.usuario_listar_id(emprestimo.get_idUsuario())
        
        nome_livro = livro_obj.get_livro() if livro_obj else "Livro não encontrado"
        nome_usuario = usuario_obj.get_nome() if usuario_obj else "Usuário não encontrado"

        reserva = emprestimo.get_reserva()
        if reserva == True:
            reserva = "Reservado"
        else: 
            reserva = "Reserva pendente"
        return f"{nome_usuario}: {nome_livro} - {reserva}"

    def atualizar():
        emprestimos = View.emprestimo_listar()
        if not emprestimos:
            st.write("Nenhum empréstimo cadastrado")
            return
        
        reservados = [
            e for e in emprestimos
            if e.get_reserva() == True
        ]

        op = st.selectbox("Selecione o empréstimo para confirmar devolução", reservados, format_func=Confirmar_devolucao_UI.formatar_emprestimo)

        atualizacao_devolucao = datetime.combine(st.date_input("Atualize a data de devolução", datetime.today() + timedelta(days=7)), datetime.min.time())
        devolucao = st.checkbox("Confirmação de devolução")
        reserva = True

        if st.button("Confirmar devolução"):
            try:
                View.emprestimo_atualizar(
                    op.get_id(),
                    op.get_idLivro(),
                    op.get_idUsuario(),
                    reserva,
                    op.get_data_emprestimo(),
                    atualizacao_devolucao.strftime('%d/%m/%Y %H:%M'),
                    devolucao
                )
                View.emprestimo_excluir(op.get_id())
                st.success("Devolução confirmada!")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao atualizar empréstimo: {e}")