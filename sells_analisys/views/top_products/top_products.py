import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

print("Iniciando script de análise e visualização de dados...")

# --- Configurações Visuais ---
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 7)
plt.rcParams['font.size'] = 12


print("\nCarregando e processando dados de vendas...")
df_vendas = pd.read_csv('../../eletronics_sales.csv', sep=';', decimal=',', parse_dates=['Data'])

print("Gerando Gráfico: Top 5 Produtos...")
top_5_produtos = df_vendas.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False).head(5)

plt.figure()

sns.barplot(x=top_5_produtos.index,
            y=top_5_produtos.values,
            hue=top_5_produtos.index,
            palette='viridis',
            legend=False
            )

plt.title('Top 5 Produtos Mais Vendidos (por Quantidade)', fontsize=16, fontweight='bold')
plt.xlabel('Produto', fontsize=12)
plt.ylabel('Total de Unidades Vendidas', fontsize=12)

plt.tight_layout()
plt.savefig('grafico_top_5_produtos.png')
