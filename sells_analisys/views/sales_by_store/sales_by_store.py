import pandas as pd
import matplotlib.pyplot as plt
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

print("Gerando Gráfico: Vendas por Loja...")
vendas_por_loja = df_vendas.groupby('Loja')['Preco_Total'].sum().sort_values(ascending=True)

plt.figure()

ax = sns.barplot(x=vendas_por_loja.values,
                 y=vendas_por_loja.index,
                 hue=vendas_por_loja.index,
                 palette='magma',
                 orient='h',
                 legend=False)

plt.title('Desempenho de Vendas por Loja', fontsize=16, fontweight='bold')
plt.xlabel('Faturamento Total (R$)', fontsize=12)
plt.ylabel('Loja', fontsize=12)

formatter_milhoes = FuncFormatter(lambda x, _: f'R$ {x/1e6:.2f} M')
ax.xaxis.set_major_formatter(formatter_milhoes)
plt.tight_layout()
plt.savefig('grafico_vendas_por_loja.png')
