import altair as alt
import pandas as pd
import streamlit as st
from view import View

class Livros_pelo_Genero_UI:
    def Grafico():
        livros = View.livro_listar()  
        generos = View.genero_listar()  

        if len(livros) == 0 or len(generos) == 0:
            st.write("Não há livros ou gêneros cadastrados.")
            return

        # Criando um dicionário para mapear id para o nome do gênero
        genero_dict = {genero.get_id(): genero.get_genero() for genero in generos}  # Usando os métodos 'get_id' e 'get_genero'

        # Criando o dataframe de livros
        df_livros = pd.DataFrame([livro.__dict__ for livro in livros])  # Supondo que 'livros' seja uma lista de objetos

        # Verificando as colunas do DataFrame de livros para garantir a chave correta
        st.write("Colunas do DataFrame de livros:", df_livros.columns)

        # Verificando o conteúdo das primeiras linhas para confirmar se a coluna 'idGenero' existe
        st.write("Primeiras linhas do DataFrame de livros:", df_livros.head())

        # Caso a coluna 'idGenero' não exista, verifique o nome correto da chave do livro
        if 'idGenero' not in df_livros.columns:
            st.write("A coluna 'idGenero' não foi encontrada. Verifique a estrutura dos objetos 'Livro'.")
            return

        # Mapeando os ids de gênero para os nomes
        df_livros['genero'] = df_livros['idGenero'].map(genero_dict)  # Usando 'idGenero' como chave para mapear o nome do gênero

        # Contabilizando a quantidade de livros por gênero
        livro_por_genero = df_livros['genero'].value_counts().reset_index()
        livro_por_genero.columns = ['genero', 'quantidade']

        # Criando o gráfico de barras
        chart = alt.Chart(livro_por_genero).mark_bar().encode(
            x='genero:N',  # Eixo X com o nome do gênero
            y='quantidade:Q',  # Eixo Y com a quantidade de livros
            color='genero:N',  # Cor das barras de acordo com o gênero
            tooltip=['genero', 'quantidade']  # Tooltip exibindo gênero e quantidade
        ).properties(
            title="Quantidade de Livros por Gênero",
            width=600,
            height=400
        )
        
        # Exibindo o gráfico no Streamlit
        st.altair_chart(chart)

        # Exibindo os livros por gênero abaixo do gráfico
        st.write("Livros por Gênero:")
        for _, row in livro_por_genero.iterrows():
            livros_do_genero = df_livros[df_livros['genero'] == row['genero']]['livro']
            st.write(f"**{row['genero']}**: {', '.join(livros_do_genero)}")

    # Função principal para ser chamada na interface Streamlit
    def main():
        st.title("Gráfico de Livros por Gênero")
        Livros_pelo_Genero_UI.Grafico()  # Chama a função que gera o gráfico e lista os livros
