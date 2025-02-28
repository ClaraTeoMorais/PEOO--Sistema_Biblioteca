import streamlit as st
import pandas as pd
from view import View
from datetime import datetime, timedelta
from modelos.livro import Livros
import time

class Solicitacoes_emprestimo_admin_UI:
    def main():
        st.write("Solicitações de reserva pendentes")
        Solicitacoes_emprestimo_admin_UI.listar()

        st.write("Confirmação de reserva")
        Solicitacoes_emprestimo_admin_UI.atualizar()

    def listar():
        livros = View.livro_listar()
        emprestimos = View.emprestimo_listar() 

        # vai pegar os ids dos livros que estão emprestados
        livros_emprestados = {e.get_idLivro() for e in emprestimos if e.get_reserva() == False}

        # flitrar livros com solicitação de empréstimo (quantidade > 0, "e" está emprestados)
        solicitacoes = [
            livro for livro in livros 
            if livro.get_quantDisponivel() > 0 and livro.get_id() in livros_emprestados
        ]

        if not solicitacoes:
            st.write("Nenhuma solicitação pendente.")
        else:
            dic = [{"Título": livro.get_livro(), "Autor": livro.get_autor(), 
                    "Editora": livro.get_editora(), "Ano": livro.get_ano(), 
                    "Disponível": livro.get_quantDisponivel()} for livro in solicitacoes]

            df = pd.DataFrame(dic)
            st.dataframe(df)

    
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
        
        reservas_pendentes = [
            e for e in emprestimos
            if e.get_reserva() == False
        ]


        op = st.selectbox("Selecione o empréstimo para confirmar", reservas_pendentes, format_func=Solicitacoes_emprestimo_admin_UI.formatar_emprestimo)

        nova_data_devolucao = datetime.combine(st.date_input("Nova data de devolução", datetime.today() + timedelta(days=7)), datetime.min.time())
        reserva = st.checkbox("Confirmação de reserva")
        devolucao = False

        if st.button("Confirmar"):
            try:
                View.emprestimo_atualizar(
                    op.get_id(),
                    op.get_idLivro(),
                    op.get_idUsuario(),
                    reserva,
                    op.get_data_emprestimo(),
                    nova_data_devolucao.strftime('%d/%m/%Y %H:%M'),
                    devolucao
                )
                st.success("Empréstimo confirmado")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao atualizar empréstimo: {e}")