import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns
from matplotlib.ticker import FuncFormatter

print("Iniciando script de análise e visualização de dados...")

# --- Configurações Visuais ---
sns.set_theme(style="whitegrid")
plot.rcParams['figure.figsize'] = (12, 7)
plot.rcParams['font.size'] = 12


print("\nCarregando e processando dados de vendas...")
df_vendas = pd.read_csv('../../eletronics_sales.csv', sep=';', decimal=',', parse_dates=['Data'])

print("Gerando Gráfico: Faturamento Mensal...")
df_vendas['Mes'] = df_vendas['Data'].dt.to_period('M')
faturamento_mensal = df_vendas.groupby('Mes')['Preco_Total'].sum()
faturamento_mensal.index = faturamento_mensal.index.to_timestamp()

plot.figure()

ax = sns.lineplot(x=faturamento_mensal.index,
                  y=faturamento_mensal.values,
                  marker='o',
                  linestyle='-')

plot.title('Faturamento Mensal da Loja em 2024', fontsize=16, fontweight='bold')
plot.xlabel('Mês', fontsize=12)
plot.ylabel('Faturamento (R$)', fontsize=12)

formatter = FuncFormatter(lambda y, _: f'R$ {int(y):,}')
ax.yaxis.set_major_formatter(formatter)
plot.xticks(rotation=45)
plot.tight_layout()
plot.savefig('grafico_faturamento_mensal.png')