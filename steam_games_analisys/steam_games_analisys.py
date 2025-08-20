import pandas as pd
import matplotlib.pyplot as plt


df_games = pd.read_csv('games.csv')
df_player = pd.read_csv('player_stats.csv')

df_steam = pd\
    .merge(
    df_games,
    df_player,
    left_on='AppID',
    right_on='GameID',
    how="inner",
    validate="many_to_many"
)

print("--- DataFrame Unificado ---")
print(df_steam)





print("\n\n--- Engenharia de Features ---")
media_avaliacao_genero = df_steam \
    .groupby('Genre')['Positive_Ratings_Percent'].mean() \
    .sort_values(ascending=False)

print("\n--- Média de Avaliação por Gênero ---")
print(media_avaliacao_genero.round(2))








def categoriza_preco(preco):
    if preco == 0:
        return 'Gratuito'
    elif preco < 100:
        return 'Barato'
    else:
        return 'O seu Rim ou olho esquerdo'

df_steam['Price_Category'] = df_steam['Price'].apply(categoriza_preco)

print("\n--- DataFrame com Categoria de Preço ---")
print(df_steam[['Name', 'Price', 'Price_Category']])







df_steam['Custo_Beneficio_Hora'] = (df_steam['Price'] / df_steam['Average_Playtime_Hours']) \
    .round(2)

print("\n--- DataFrame com Custo-Benefício por Hora ---")
print(df_steam[['Name', 'Custo_Beneficio_Hora']] \
      .sort_values(by='Custo_Beneficio_Hora'))







print("\n--- Gerando Gráfico (ver janela de plotagem) ---")
plot_grafico = df_steam.groupby('Price_Category')['Average_Playtime_Hours'].mean() \
    .sort_values() \
    .plot(kind='barh',
          title='Média de Horas Jogadas por Categoria de Preço',
          x='Categoria de Preço',
          y='Média de Horas Jogadas',
          )
plt.tight_layout()
#plt.show()


df_indie = df_steam[df_steam['Genre'].str.contains('Indie')]
melhor_custo_beneficio_indie = df_indie.sort_values(by='Custo_Beneficio_Hora').iloc[0]
print(f"\n1. Jogo Indie com melhor custo-benefício: \n{melhor_custo_beneficio_indie[['Name', 'Custo_Beneficio_Hora']]}")

print("\n2. Gerando Gráfico de Dispersão (ver janela de plotagem) ---")
df_steam.plot(kind='scatter',
              x='Average_Playtime_Hours',
              y='Positive_Ratings_Percent',
              title='Tempo de Jogo vs. Avaliação')
plt.show()

df_pagos = df_steam[df_steam['Price'] > 0]
melhor_avaliado_pago = df_pagos.sort_values(by='Positive_Ratings_Percent', ascending=False).iloc[0]
print(f"\n3. Jogo pago com melhor avaliação: \n{melhor_avaliado_pago[['Name', 'Positive_Ratings_Percent']]}")


