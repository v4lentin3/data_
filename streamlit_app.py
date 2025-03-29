import streamlit as st
import pandas as pd
import plotly.express as px

# Configurações da página
st.set_page_config(
    page_title="Data Analyzer",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded"
)

col1, col2 = st.columns(2)

# # Carregar arquivo CSV
# data_file = './data2.csv'

# Carregar arquivo CSV
data_file = st.sidebar.file_uploader("Carregar arquivo CSV")

if data_file is not None:

# Opções avançadas
    show_additional_options = st.sidebar.checkbox("Opções Avançadas")
    separator, decimal_point, drop_lines = ',', ',', 2  # Valores padrão

    if show_additional_options:
        separator = st.sidebar.selectbox("Separador", [',', ';', '.', '|', ' '])
        decimal_point = st.sidebar.selectbox("Decimal", ['.', ','])
        drop_lines = st.sidebar.number_input('Remover linhas iniciais', min_value=0, value=2)

    # Tenta carregar o arquivo CSV
    try:
        df = pd.read_csv(data_file, sep=separator, decimal=decimal_point, skiprows=drop_lines)
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo CSV: {e}")
        df = None
#################
    if 'Palavra-chave' in df.columns:
        global_target = 'Palavra-chave'
        df = df.iloc[:-3]
    elif 'Termo de pesquisa' in df.columns:
        global_target = 'Termo de pesquisa'
        df = df.iloc[:-4]
# if df is not None:
    # Exibe as primeiras 20 linhas da tabela
    
    colunas_para_converter = ['Conversões', 'Custo / conv.', 'Custo', 'CPC méd.', 'Cliques']

    for col in colunas_para_converter:
        if not pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].str.replace(',', '.').str.strip()
            df[col] = pd.to_numeric(df[col], errors='coerce')

    
    # Seleciona a coluna alvo para análise univariada
    target_column = st.sidebar.selectbox("Selecione a coluna alvo:", [None] + list(df.columns))

    if target_column is not None:  
        col1.title(f"Análise Univariada de {target_column}")

                # Análise Univariada
        if df[target_column].dtype == 'float64':
            # Exibe estatísticas descritivas
            # Limites para filtragem
            maximo1 = float(df[target_column].max())
            minimo1 = float(df[target_column].min())

            # Inputs para mínimo e máximo da coluna principal
            minimo_input1 = st.sidebar.number_input("Selecione o mínimo da coluna principal", min_value=minimo1, max_value=maximo1-0.01, value=minimo1, step=0.01)
            maximo_input1 = st.sidebar.number_input("Selecione o máximo da coluna principal", min_value=minimo1+0.01, max_value=maximo1, value=maximo1, step=0.01)

            # Verifica se o mínimo é maior que o máximo
            if minimo_input1 > maximo_input1:
                st.sidebar.error("O mínimo não pode ser maior que o máximo na coluna principal!")

            # Filtra os dados com base nos limites definidos
            df_filtered = df[(df[target_column] >= minimo_input1) & (df[target_column] <= maximo_input1)]

            # Seleciona uma variável adicional para filtro
            additional_variable = st.sidebar.selectbox("Selecione a variável adicional para filtrar:", df.drop([global_target, target_column], axis=1).columns.tolist())
            
            # Verifica se a variável adicional é numérica
            if df[additional_variable].dtype in ['float64', 'int64']:
                # Limites para filtragem da variável adicional
                maximo2 = float(df[additional_variable].max())
                minimo2 = float(df[additional_variable].min())
                
                # Inputs para mínimo e máximo da variável adicional
                minimo_input2 = st.sidebar.number_input(f"Selecione o mínimo para {additional_variable}", min_value=minimo2, max_value=maximo2-0.01, value=minimo2, step=0.01)
                maximo_input2 = st.sidebar.number_input(f"Selecione o máximo para {additional_variable}", min_value=minimo2+0.01, max_value=maximo2, value=maximo2, step=0.01)

                # Verifica se o mínimo é maior que o máximo para a variável adicional
                if minimo_input2 > maximo_input2:
                    st.sidebar.error(f"O mínimo não pode ser maior que o máximo para {additional_variable}!")

                # Filtra o dataframe com base nos limites definidos para a variável adicional
                df_filtered = df_filtered[(df_filtered[additional_variable] >= minimo_input2) & (df_filtered[additional_variable] <= maximo_input2)]
            
            else:
                # Filtro para a variável adicional se não for numérica
                unique_values = df_filtered[additional_variable].unique()
                unique_values = ["Todos"] + list(unique_values)  # Adiciona a opção "Todos"

                selected_value = st.sidebar.selectbox("Selecione o valor para filtrar:", unique_values)

                # Aplica o filtro adicional ao dataframe
                if selected_value == "Todos":
                    df_filtered = df_filtered.copy()
                else:
                    df_filtered = df_filtered[df_filtered[additional_variable] == selected_value]

            # Exibe o histograma dos dados filtrados
            col1.plotly_chart(px.histogram(df_filtered, x=target_column, title=f'Histograma de {target_column} (filtrado)'), use_container_width=True)
        # Cria um novo DataFrame com as colunas que você deseja exibir
            df_to_display = df_filtered[[global_target, target_column, additional_variable]]

            # Exibe o DataFrame filtrado
            col2.write(df_to_display)
            csv = df_to_display[global_target].to_csv(index=False, header=False).encode('utf-8')
            st.download_button(
                label="Baixar Termos de Pesquisa",
                data=csv,
                file_name='melhores_termos_de_pesquisa.csv',
                mime='text/csv',
            )

        else:  # Para colunas categóricas
            categories = df[target_column].unique()
            selected_category = st.sidebar.selectbox(f"Selecione uma categoria de {target_column}:", [None] + list(categories))

            if selected_category is not None:
                df_filtered = df[df[target_column] == selected_category]
                df_to_display = df_filtered[[target_column,'Campanha','Tipo de corresp.', 'Conversões', 'Custo / conv.', 'Custo', 'CPC méd.', 'Cliques']]
                minimo_table = st.sidebar.number_input(f"Selecione o tamanho da tabela para {selected_category}", min_value=20, step=5)
                # Exibe o DataFrame filtrado
    
                st.table(df_to_display.head(minimo_table))
                # counts = df_filtered[target_column].value_counts().reset_index()
                # counts.columns = [target_column, 'Count']
                # col1.plotly_chart(px.bar(counts, x=target_column, y='Count', title=f'Gráfico de Frequência de {target_column} (filtrado)'), use_container_width=True)
    else:
        st.table(df.head(20))
 

else:
    st.warning("Por favor, suba um arquivo CSV.")
