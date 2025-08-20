import pandas as pd
import matplotlib.pyplot as plt

df_games = pd.read_csv('games.csv')
df_player = pd.read_csv('player_stats.csv')

df_steam = pd\
    .merge(df_games, df_player, left_on='AppID', right_on='GameID', how="inner", validate="many_to_many")

print("--- DataFrame Unificado ---")
print(df_steam)





print("\n\n--- Engenharia de Features ---")
media_avaliacao_genero = df_steam \
    .groupby('Genre')['Positive_Ratings_Percent'] \
    .mean() \
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

df_steam['Price_Category'] = df_steam['Price'] \
    .apply(categoriza_preco)

print("\n--- DataFrame com Categoria de Preço ---")
print(df_steam[['Name', 'Price', 'Price_Category']])







df_steam['Custo_Beneficio_Hora'] = (df_steam['Price'] / df_steam['Average_Playtime_Hours']) \
    .round(2)

print("\n--- DataFrame com Custo-Benefício por Hora ---")
print(df_steam[['Name', 'Custo_Beneficio_Hora']] \
      .sort_values(by='Custo_Beneficio_Hora'))





print("\n\n--- Correlação e Visualização ---")
correlacao = df_steam[['Price', 'Positive_Ratings_Percent', 'Average_Playtime_Hours']] \
    .corr()
print("\n--- Matriz de Correlação ---")
print(correlacao)





print("\n--- Gerando Gráfico (ver janela de plotagem) ---")
plot_grafico = df_steam.groupby('Price_Category')['Average_Playtime_Hours'] \
    .mean() \
    .sort_values() \
    .plot(kind='barh',
          title='Média de Horas Jogadas por Categoria de Preço')
# plt.tight_layout()
# plt.show()





df_indie = df_steam[df_steam['Genre'].str.contains('Indie')]
melhor_custo_beneficio_indie = df_indie.sort_values(by='Custo_Beneficio_Hora').iloc[0]
print(f"\n1. Jogo Indie com melhor custo-benefício: \n{melhor_custo_beneficio_indie[['Name', 'Custo_Beneficio_Hora']]}")


print("\n2. Gerando Gráfico de Dispersão ---")
df_steam.plot(kind='scatter', x='Average_Playtime_Hours', y='Positive_Ratings_Percent',
              title='Tempo de Jogo vs. Avaliação')
#plt.show()


df_pagos = df_steam[df_steam['Price'] > 0]
melhor_avaliado_pago = df_pagos.sort_values(by='Positive_Ratings_Percent', ascending=False).iloc[0]
print(f"\n3. Jogo pago com melhor avaliação: \n{melhor_avaliado_pago[['Name', 'Positive_Ratings_Percent']]}")







# -------------------------- RESOLUÇÃO DAS ATIVIDADES --------------------------
# =================================================================
# Tarefa 1: Análise Precisa de Gêneros
# =================================================================
# Para esta tarefa, é crucial primeiro separar os gêneros que estão em uma
# única string (ex: 'Action;FPS') em uma lista de strings.
# Depois, usamos a função .explode() que cria uma nova linha para cada
# item na lista, duplicando os outros dados da linha original.

print("\n--- Tarefa 1: Análise Precisa de Gêneros ---")
# Criamos uma cópia para não alterar o dataframe original enquanto trabalhamos nele
df_generos = df_steam.copy()
df_generos['Genre'] = df_generos['Genre'].str.split(';')
df_exploded = df_generos.explode('Genre')

# Agora podemos agrupar pelo gênero individual e calcular a média
media_horas_por_genero = df_exploded.groupby('Genre')['Average_Playtime_Hours'].mean().sort_values(ascending=False)

print("Média de horas jogadas por gênero (análise precisa):")
print(media_horas_por_genero)
print(f"\nConclusão: O gênero com maior média de horas jogadas é '{media_horas_por_genero.index[0]}'.")


# =================================================================
# Tarefa 2: Identificando as "Gemas Escondidas"
# =================================================================
# O segredo aqui é usar o operador '&' para combinar duas condições
# booleanas. Cada condição deve estar entre parênteses.

print("\n\n--- Tarefa 2: Gemas Escondidas ---")
gemas_escondidas = df_steam[
    (df_steam['Positive_Ratings_Percent'] > 95) &
    (df_steam['Average_Playtime_Hours'] < 50)
]

print("Jogos muito bem avaliados e curtos ('Gemas Escondidas'):")
print(gemas_escondidas[['Name', 'Positive_Ratings_Percent', 'Average_Playtime_Hours']])
print("\nConclusão: Encontramos jogos que podem ser ótimos para jogadores com pouco tempo.")


# =================================================================
# Tarefa 3: Criando uma Métrica de Engajamento
# =================================================================
# A melhor abordagem para evitar a divisão por zero é filtrar o DataFrame
# para incluir apenas os jogos pagos antes de fazer o cálculo.
# Trabalhar em uma cópia com .copy() evita o 'SettingWithCopyWarning'.

print("\n\n--- Tarefa 3: Índice de Retenção ---")
df_pagos = df_steam[df_steam['Price'] > 0].copy()

df_pagos['Indice_Retencao'] = df_pagos['Average_Playtime_Hours'] / df_pagos['Price']

print("Jogos com maior Índice de Retenção (horas por real gasto):")
# Mostrando o top 5
print(df_pagos.sort_values(by='Indice_Retencao', ascending=False)[['Name', 'Price', 'Indice_Retencao']].head())
print("\nConclusão: Jogos mais baratos e com alto tempo de jogo, como Terraria, lideram essa métrica.")
print("Estratégia: Analisamos apenas jogos pagos, pois o conceito de 'horas por real' não se aplica a jogos gratuitos.")


# =================================================================
# Tarefa 4: Visualização Estratégica Avançada
# =================================================================
# Usamos o .plot() com kind='scatter'. O parâmetro 's' (size) permite
# adicionar uma terceira dimensão de informação ao gráfico.
# Usamos o DataFrame de jogos pagos para ter a coluna 'Indice_Retencao'.

# =================================================================
# Tarefa 4: Visualização Estratégica Avançada com Rótulos
# =================================================================

print("\n\n--- Tarefa 4: Visualização Estratégica com Rótulos ---")

# Criamos a figura e os eixos do gráfico com o Matplotlib.
# Isso nos dá mais controle sobre a customização.
fig, ax = plt.subplots(figsize=(15, 10)) # Figura maior para caber os rótulos

# Criamos o gráfico de dispersão usando o Pandas, mas direcionando para os eixos 'ax' que criamos
df_pagos.plot(
    kind='scatter',
    x='Indice_Retencao',
    y='Positive_Ratings_Percent',
    s=df_pagos['Average_Playtime_Hours'], # Tamanho do ponto reflete as horas jogadas
    ax=ax, # Usando os eixos criados
    grid=True,
    alpha=0.6 # Leve transparência para os pontos
)

# --- A GRANDE NOVIDADE: Adicionando os rótulos ---
# Estratégia: Para não poluir o gráfico, vamos rotular apenas os pontos mais relevantes.
# Por exemplo, jogos com Índice de Retenção muito alto ou Avaliação muito alta.
df_para_rotular = df_pagos[
    (df_pagos['Indice_Retencao'] > 4) |
    (df_pagos['Positive_Ratings_Percent'] > 97)
]

# Agora, iteramos APENAS sobre as linhas do DataFrame filtrado
for index, row in df_para_rotular.iterrows():
    ax.text(
        row['Indice_Retencao'] + 0.1, # Pequeno deslocamento no eixo x para não sobrepor o ponto
        row['Positive_Ratings_Percent'], # Posição exata no eixo y
        row['Name'], # O texto do rótulo
        fontsize=9 # Tamanho da fonte
    )

# Melhorando os títulos e eixos
ax.set_title('Retenção vs. Avaliação de Jogos Pagos na Steam', fontsize=16)
ax.set_xlabel("Índice de Retenção (Horas por R$)", fontsize=12)
ax.set_ylabel("Avaliações Positivas (%)", fontsize=12)

# Garante que tudo seja exibido corretamente
plt.tight_layout()
plt.show()