# Previsão de Preços de Ações com Prophet

Este é um exemplo de código em Python que utiliza a biblioteca Prophet para prever os preços de ações. O código realiza as seguintes etapas:

1. Importa as bibliotecas necessárias, incluindo Prophet, numpy, pandas, matplotlib e sklearn.
2. Obtém os dados históricos de preços de ações do índice Bovespa (BVSP) usando a biblioteca yfinance.
3. Prepara os dados, ajustando o formato e renomeando as colunas necessárias.
4. Cria um modelo Prophet e o ajusta aos dados históricos.
5. Faz previsões futuras dos preços de ações para um determinado período.
6. Plota os resultados das previsões e os componentes do modelo.
7. Divide os dados em conjuntos de treinamento e teste.
8. Cria um segundo modelo Prophet usando apenas os dados de treinamento.
9. Faz previsões usando o modelo treinado e compara com os valores reais dos dados de teste.
10. Plota os resultados das previsões em comparação com os valores reais.

## Requisitos

Certifique-se de ter as seguintes bibliotecas instaladas:

- prophet
- numpy
- pandas
- matplotlib
- sklearn
- yfinance

Você pode instalar as bibliotecas usando o pip:

pip install prophet numpy pandas matplotlib sklearn yfinance

## Resultados

Os resultados das previsões serão exibidos em gráficos, mostrando as previsões futuras dos preços de ações, bem como os componentes do modelo.
 
