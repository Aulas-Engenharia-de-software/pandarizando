import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import FuncFormatter

print("Iniciando script de análise e visualização de dados (versão corrigida)...")

# --- Configurações Visuais ---
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 7)
plt.rcParams['font.size'] = 12

print("\nCarregando e processando dados de vendas...")
df_vendas = pd.read_csv('../../eletronics_sales.csv', sep=';', decimal=',', parse_dates=['Data'])
formatter = FuncFormatter(lambda y, _: f'R$ {int(y):,}')


print("Gerando Gráfico: Faturamento por Categoria...")
faturamento_categoria = df_vendas.groupby('Categoria')['Preco_Total'].sum().sort_values(ascending=False)

plt.figure()

ax = sns.barplot(x=faturamento_categoria.index,
                 y=faturamento_categoria.values,
                 hue=faturamento_categoria.index,
                 palette='plasma', legend=False)

plt.title('Faturamento Total por Categoria de Produto', fontsize=16, fontweight='bold')
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Faturamento Total (R$)', fontsize=12)
ax.yaxis.set_major_formatter(formatter)
plt.tight_layout()
plt.savefig('grafico_faturamento_categoria.png')
