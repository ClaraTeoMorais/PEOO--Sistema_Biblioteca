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
        genero_dict = {genero.get_id(): genero.get_genero() for genero in generos}

        df_livros = pd.DataFrame([livro.__dict__ for livro in livros])

        #st.write("Colunas do DataFrame de livros:", df_livros.columns) #mostra as variáveis do livro

        coluna_id_genero = "_Livro__idGenero"

        # Verificando se a coluna existe
        if coluna_id_genero not in df_livros.columns:
            st.write("A coluna de ID do gênero não foi encontrada. Verifique a estrutura dos objetos 'Livro'.")
            return

        # Mapeando os ids de gênero para os nomes
        df_livros['genero'] = df_livros[coluna_id_genero].map(genero_dict)

        # Contabilizando a quantidade de livros por gênero
        livro_por_genero = df_livros['genero'].value_counts().reset_index()
        livro_por_genero.columns = ['genero', 'quantidade']

        chart = alt.Chart(livro_por_genero).mark_bar().encode(
            x='genero:N',  
            y='quantidade:Q',  
            color='genero:N',  
            tooltip=['genero', 'quantidade'] 
        ).properties(
            title="Quantidade de Livros por Gênero",
            width=600,
            height=400
        )
        
        st.altair_chart(chart)

        # Exibindo os livros por gênero abaixo do gráfico
        st.write("Livros por Gênero:")
        for _, row in livro_por_genero.iterrows():
            livros_do_genero = df_livros[df_livros['genero'] == row['genero']]['_Livro__livro']
            st.write(f"**{row['genero']}**: {', '.join(livros_do_genero)}")

    def main():
        st.title("Gráfico de Livros por Gênero")
        Livros_pelo_Genero_UI.Grafico() 
