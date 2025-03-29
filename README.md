# 📊 Dashboard de Análise de Conversões e Termos de Pesquisa do Google  

Este é um **dashboard interativo** desenvolvido em **Streamlit** para análise de **conversões, custo por conversão, cliques e CPC médio** em campanhas do Google Ads. Ele permite explorar dados de palavras-chave e termos de pesquisa, aplicar filtros dinâmicos e visualizar estatísticas descritivas.

## 🚀 Funcionalidades  

✅ Upload de arquivos CSV diretamente no aplicativo.  
✅ Configuração personalizada de separadores e decimais.  
✅ Filtros interativos para análise univariada.  
✅ Histogramas dinâmicos para distribuição dos dados.  
✅ Exportação dos melhores termos de pesquisa.  
✅ Suporte para colunas numéricas e categóricas.  

## 🛠 Tecnologias Utilizadas  

- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [Pandas](https://pandas.pydata.org/)  
- [Plotly Express](https://plotly.com/python/)  

## 📂 Como Usar  

### 1️⃣ Instale as dependências  
```bash
pip install streamlit pandas plotly
```

### 2️⃣ Execute o aplicativo  
```bash
streamlit run app.py
```

### 3️⃣ Faça o upload do arquivo CSV  
- O arquivo deve conter colunas como **"Palavra-chave"** ou **"Termo de pesquisa"**.  
- Selecione os separadores corretos caso necessário.  

### 4️⃣ Explore os dados  
- Escolha a **coluna-alvo** para análise.  
- Ajuste filtros numéricos ou categóricos.  
- Visualize histogramas e estatísticas descritivas.  

## 📌 Exemplo de Uso  

🔹 Suponha que você tenha um arquivo CSV com os seguintes dados:  

| Palavra-chave | Conversões | Custo / conv. | Custo | CPC méd. | Cliques |
|--------------|------------|--------------|-------|---------|---------|
| Produto A    | 10         | 5.00         | 50.00 | 2.50    | 20      |
| Produto B    | 15         | 3.50         | 52.50 | 1.75    | 30      |

✅ O dashboard permitirá visualizar estatísticas sobre **conversões**, **custo por conversão** e outros indicadores de desempenho.  

## 📄 Licença  

Este projeto é de código aberto sob a licença **MIT**.  

---  
Feito com ❤️ por [danttis](https://github.com/danttis)

