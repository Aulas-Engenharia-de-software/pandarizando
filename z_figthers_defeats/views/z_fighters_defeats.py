import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Iniciando a nova análise de derrotas...")

# --- Configurações Visuais ---
sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams['figure.figsize'] = (12, 7)
plt.rcParams['font.size'] = 12

# Carregar os novos dados
df = pd.read_csv('../derrotas_guerreiros_z.csv', sep=';')

# --- Análise 1: Quem é o "Campeão" das Derrotas? ---
print("\nAnálise 1: Contagem de derrotas por personagem...")
derrotas_por_personagem = df['Personagem'].value_counts()

plt.figure()
sns.barplot(x=derrotas_por_personagem.index, y=derrotas_por_personagem.values, hue=derrotas_por_personagem.index, legend=False)
plt.title('Ranking de Derrotas: O Time dos Sacos de Pancada', fontsize=16, fontweight='bold')
plt.ylabel('Número Total de Derrotas Registradas')
plt.xlabel('Personagem')
plt.tight_layout()
plt.savefig('grafico_ranking_derrotas.png')
print("Gráfico 1 salvo: grafico_ranking_derrotas.png")


# --- Análise 2: Qual o tipo de derrota mais comum? ---
print("\nAnálise 2: Tipos de derrota mais comuns...")
derrotas_por_tipo = df['Tipo_de_Derrota'].value_counts()

plt.figure()
sns.barplot(x=derrotas_por_tipo.index, y=derrotas_por_tipo.values, hue=derrotas_por_tipo.index, legend=False)
plt.title('Tipos de Derrota Mais Comuns', fontsize=16, fontweight='bold')
plt.ylabel('Contagem')
plt.xlabel('Tipo de Derrota')
plt.tight_layout()
plt.savefig('grafico_tipos_derrota.png')
print("Gráfico 2 salvo: grafico_tipos_derrota.png")


# --- Análise 3: Qual a origem de golpe mais fatal? ---
print("\nAnálise 3: Origem dos golpes que causam derrotas...")
derrotas_por_origem = df['Origem_do_Golpe'].value_counts()

plt.figure()
# Usando um gráfico de pizza (pie chart) para variar
plt.pie(derrotas_por_origem, labels=derrotas_por_origem.index, autopct='%1.1f%%', startangle=140)
plt.title('Proporção de Derrotas por Origem do Golpe', fontsize=16, fontweight='bold')
plt.ylabel('') # Remove o rótulo Y que o pie chart cria por padrão
plt.axis('equal') # Garante que a pizza seja um círculo.
plt.tight_layout()
plt.savefig('grafico_origem_golpe.png')
print("Gráfico 3 salvo: grafico_origem_golpe.png")


# --- Análise 4 (Avançada): Derrotas por Saga e Personagem (Gráfico Empilhado) ---
print("\nAnálise 4: Derrotas por saga, detalhado por personagem...")

# Usamos 'crosstab' para criar uma tabela de frequência
tabela_cruzada = pd.crosstab(index=df['Saga'], columns=df['Personagem'])

# Plotamos a tabela cruzada como um gráfico de barras empilhadas
ax = tabela_cruzada.plot(kind='bar', stacked=True, figsize=(14, 8))
plt.title('Derrotas por Saga (Detalhado por Personagem)', fontsize=16, fontweight='bold')
plt.ylabel('Número de Derrotas')
plt.xlabel('Saga')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Personagem')
plt.tight_layout()
plt.savefig('grafico_derrotas_por_saga_empilhado.png')
print("Gráfico 4 salvo: grafico_derrotas_por_saga_empilhado.png")

print("\nAnálise concluída!")