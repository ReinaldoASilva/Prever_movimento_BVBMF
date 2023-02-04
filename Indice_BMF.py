import prophet
from prophet import Prophet
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from prophet.plot import plot_plotly, plot_components_plotly
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

import yfinance as yf 
import pandas_datareader.data as web
yf.pdr_override()
from pylab import rcParams
rcParams['figure.figsize'] = 20, 10

p = web.get_data_yahoo('^BVSP', start='2010-01-01', end='2020-01-01')

adj_close = p['Adj Close']

adj_close.plot()
plt.xlabel('Data', size=16)
plt.ylabel('Preço', size=16)
plt.show()

type(adj_close)
adj_close = pd.DataFrame(adj_close)

# a coluna data está como o indice do dataframe, agora precisamar mudar isso

adj_close.reset_index(('Date'), inplace=True)

adj_close.columns = ['ds', 'y']


# modelo preditivo

modelo = Prophet()
modelo.fit(adj_close)

adj_close_future = pd.date_range(start='2020-01-01', end='2023-01-01')
adj_close_future = pd.DataFrame(adj_close_future)
# alterar o nome da coluna

adj_close_future.columns = ['ds']

previsao = modelo.predict(adj_close_future)

#selecionar as colunas que eu quero

previsao[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

modelo.plot(previsao)
modelo.plot_components(previsao)
plt.show()

plot_plotly(modelo, previsao)

# criando modelo de treino e teste

adj_close_train, adj_close_test = train_test_split(adj_close, test_size=0.3, shuffle=False)

modelo2 = Prophet()

modelo2.fit(adj_close_train)

prev2 = modelo2.predict(pd.DataFrame(adj_close_test['ds']))

y_prev = prev2['yhat'].values
y_true = adj_close_test['y'].values

plt.plot(y_true, label='Verdadeiro')
plt.plot(y_prev, label='Previsão')
plt.legend()
plt.show()









