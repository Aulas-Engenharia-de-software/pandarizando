import pandas as pd

arquivo_saida = 'eletronics_sales.csv'

pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:,.2f}'.format

print("==========================================================")
print("INICIANDO ANÁLISE DA BASE DE VENDAS DA LOJA DE ELETRÔNICOS")
print("==========================================================")

df_vendas = pd.read_csv(arquivo_saida, sep=';', decimal=',')
df_vendas['Data'] = pd.to_datetime(df_vendas['Data'])
df_vendas['Mes'] = df_vendas['Data'].dt.to_period('M')


def analisar_faturamento_por_mes():
    print("\n--- 1. Faturamento Total por Mês ---")

    faturamento_mensal = df_vendas\
        .groupby('Mes')['Preco_Total']\
        .sum()\
        .reset_index()

    faturamento_mensal['Mes'] = faturamento_mensal['Mes']\
        .dt\
        .strftime('%Y-%m')


    print(faturamento_mensal)
    print("Insight: Podemos ver a sazonalidade das vendas, com picos em meses específicos.")

def analisar_produtos_mais_vendidos_por_quantidade():
    print("\n--- 2. Top 5 Produtos Mais Vendidos (por Quantidade) ---")

    top_5_produtos = df_vendas\
        .groupby('Produto')['Quantidade']\
        .sum()\
        .sort_values(ascending=False)\
        .head(5)

    print(top_5_produtos)
    print("Insight: Acessórios mais baratos como 'Fone de Ouvido' e 'Carregador' tendem a vender mais em volume.")


def analisar_faturamento_por_categoria():
    print("\n--- 3. Faturamento por Categoria de Produto ---")

    faturamento_categoria = df_vendas\
        .groupby('Categoria')['Preco_Total']\
        .sum()\
        .sort_values(ascending=False)

    print(faturamento_categoria)
    print("Insight: Embora acessórios vendam mais em quantidade, 'Laptops' e 'Smartphones' geram a maior parte da receita.")



def analisar_desempenho_por_loja():
    print("\n--- 4. Desempenho de Vendas por Loja ---")

    vendas_por_loja = df_vendas\
        .groupby('Loja')['Preco_Total']\
        .sum()\
        .sort_values(ascending=False)

    print(vendas_por_loja)
    print("Insight: A loja 'Online' e a de 'São Paulo' são os carros-chefe da empresa.")


analisar_faturamento_por_mes()
analisar_desempenho_por_loja()
analisar_produtos_mais_vendidos_por_quantidade()
analisar_faturamento_por_categoria()

