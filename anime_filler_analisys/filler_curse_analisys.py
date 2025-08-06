import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import PercentFormatter

print("Iniciando a análise da 'Maldição dos Fillers'...")

sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (12, 7)
plt.rcParams['font.size'] = 12


df = pd.read_csv('episodios_animes.csv', sep=';')

print("\nAnálise 1: Proporção geral de fillers...")
proporcao_geral = df['tipo_episodio'].value_counts()

plt.figure()
plt.pie(proporcao_geral, labels=proporcao_geral.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("muted")[0:2])
plt.title('Proporção Geral de Episódios: Canônico vs. Filler', fontsize=16, fontweight='bold')
plt.ylabel('')
plt.savefig('grafico_proporcao_geral.png')
print("Gráfico 1 salvo: grafico_proporcao_geral.png")

print("\nAnálise 2: Proporção de fillers por anime...")
tabela_proporcao = pd.crosstab(index=df['anime'], columns=df['tipo_episodio'], normalize='index')

ax = tabela_proporcao.plot(kind='bar', stacked=True, figsize=(14, 8), color=sns.color_palette("muted")[0:2])
plt.title('Proporção de Fillers por Anime', fontsize=16, fontweight='bold')
plt.ylabel('Porcentagem de Episódios')
plt.xlabel('Anime')
plt.xticks(rotation=0)
plt.legend(title='Tipo de Episódio')
ax.yaxis.set_major_formatter(PercentFormatter(1.0)) # Formata o eixo Y como porcentagem
plt.tight_layout()
plt.savefig('grafico_proporcao_por_anime.png')
print("Gráfico 2 salvo: grafico_proporcao_por_anime.png")

print("\nAnálise 3: Comparando as notas médias...")
nota_media_por_tipo = df.groupby('tipo_episodio')['nota_simulada'].mean().sort_values(ascending=False)

plt.figure()
ax = sns.barplot(x=nota_media_por_tipo.index, y=nota_media_por_tipo.values, hue=nota_media_por_tipo.index, legend=False)
plt.title('Nota Média: Episódios Canônicos vs. Fillers', fontsize=16, fontweight='bold')
plt.ylabel('Nota Média Simulada (de 1 a 10)')
plt.xlabel('Tipo de Episódio')
ax.set_ylim(0, 10) # Define o limite do eixo Y para ser de 0 a 10
plt.tight_layout()
plt.savefig('grafico_comparacao_notas.png')
print("Gráfico 3 salvo: grafico_comparacao_notas.png")

print("\nAnálise 4: Distribuição das notas por anime e tipo...")

plt.figure(figsize=(16, 9))
sns.boxplot(data=df, x='anime', y='nota_simulada', hue='tipo_episodio')
plt.title('Distribuição de Notas por Anime e Tipo de Episódio', fontsize=16, fontweight='bold')
plt.ylabel('Nota Simulada')
plt.xlabel('Anime')
plt.legend(title='Tipo de Episódio')
plt.tight_layout()
plt.savefig('grafico_distribuicao_detalhada.png')
print("Gráfico 4 salvo: grafico_distribuicao_detalhada.png")

print("\nAnálise concluída com sucesso!")