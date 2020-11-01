# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import mode

# Base de dados
xi = [3246, 3476, 3724, 3773, 3837, 3968, 4198, 4048, 4170, 4226, 4788, 4009, 3568, 4357]

#Base de dados COM Outliers
xy = [6799, 3476, 3724, 3773, 3837, 3968, 4198, 4048, 4170, 4226, 4788, 4009, 3568, 4357]

def print_full(x):
    pd.options.display.max_rows = len(x)
    pd.options.display.max_columns = 999
    ##pd.set_option('display.max_rows', len(x))
    ##pd.set_option('display.max_columns', len(x.iloc[0])+1)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')

# Média
xi_media = np.mean(xi)
xy_media = np.mean(xy)

# Mediana
xi_mediana = np.median(xi)
xy_mediana = np.median(xy)

# Moda
xi_moda = mode(xi)[0][0]
xy_moda = mode(xy)[0][0]

# Desvio padrão
xi_std = np.std(xi, ddof=1)
xy_std = np.std(xy, ddof=1)

# Z-Score ( Subtrai da média e divide pelo desvio padrão. Deve ser menor que 3, m moódulo.
z_score_xi = (xi - xi_media) / xi_std
z_score_xy = (xy - xy_media) / xy_std

print( "----- Lista Sem Anomalias -------------")
print(f"Lista                      ::  {xi}")
print(f"A media da lista é         ::  {xi_media}")
print(f"A mediana da lista é       ::  {xi_mediana}")
print(f"A moda da lista é          ::  {xi_moda}")
print(f"O desvio padrão da lista é ::  {xi_std}")

print( "----- Lista COM Anomalias -------------")
print(f"Lista                      ::  {xy}")
print(f"A media da lista é         ::  {xy_media}")
print(f"A mediana da lista é       ::  {xy_mediana}")
print(f"A moda da lista é          ::  {xy_moda}")
print(f"O desvio padrão da lista é ::  {xy_std}")

cols = ['Base sem anomalias', 'Z-Score sem anomalias', 'Base COM anomalias', 'Z-Score COM anomalias']
df = pd.DataFrame({cols[0]:xi, cols[1]:z_score_xi, cols[2]:xy, cols[3]:z_score_xy})

df.round(2)

## Como ele imprimia somente 3 colunas, decidi imprimir de 2 em 2.
print_full(df[cols[0:2]])

print_full(df[cols[2:4]])

print_full(df[[cols[1],cols[3]]])

## Abre uma "base" do gráfico #1
graficos = plt.figure(1, figsize=(12, 10))

## Cria um grid 2x2 gráficos e pega a posição 1.
grafico1 = graficos.add_subplot(221)
stats.probplot(xi, dist="norm", plot=grafico1)
grafico1.grid(True)
grafico1.text(-1.5, 4600.0, f"Média = {xi_media:.3f} +- {(2*xi_std):.3f}", fontsize=10)

## Cria um grid 2x2 gráficos e pega a posição 2.
grafico2 = graficos.add_subplot(222)
stats.probplot(xy, dist="norm", plot=grafico2)
grafico2.grid(True)
grafico2.text(-1.5, 6500.0, f"Média = {xy_media:.3f} +- {(2*xy_std):.3f}", fontsize=10)


## Cria um grid 2x2 gráficos e pega a posição 3.
axi = graficos.add_subplot(223)
bp_xi = axi.boxplot(xi)
axi.title.set_text ('Box plot de série sem oulier')

## Cria um grid 2x2 gráficos e pega a posição 4.
axy = graficos.add_subplot(224)
bp_xy = axy.boxplot(xy)
axy.title.set_text ('Box plot de série COM oulier')

plt.savefig('resultado.png')
plt.show()

