import random
from datetime import datetime, timedelta

import pandas as pd


print("Iniciando a geração do arquivo de vendas...")
arquivo_saida = 'eletronics_sales.csv'
num_registros = 50000
data_inicial = datetime(2024, 1, 1)
data_final = datetime(2024, 12, 31)

print(f"Criando dados de vendas para ${num_registros} registros ")
produtos = {
    'Smartphone X1': {'categoria': 'Smartphones', 'preco': 2500},
    'Smartphone ProMax': {'categoria': 'Smartphones', 'preco': 7500},
    'Laptop Gamer Z': {'categoria': 'Laptops', 'preco': 8200},
    'Laptop Office': {'categoria': 'Laptops', 'preco': 3800},
    'Fone de Ouvido BT': {'categoria': 'Acessórios', 'preco': 350},
    'Teclado Mecânico': {'categoria': 'Acessórios', 'preco': 550},
    'Mouse Gamer': {'categoria': 'Acessórios', 'preco': 280},
    'Smart TV 55"': {'categoria': 'TVs e Vídeo', 'preco': 4200},
    'Smartwatch Fit': {'categoria': 'Wearables', 'preco': 1200},
    'Carregador Turbo': {'categoria': 'Acessórios', 'preco': 150},
}

lojas = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Online', 'Curitiba']

dados_vendas = []
dias_no_periodo = (data_final - data_inicial).days

print("Iniciando geração dos CSV de vendas...")
for i in range(num_registros):
    nome_produto = random.choice(list(produtos.keys()))
    info_produto = produtos[nome_produto]

    data_venda = data_inicial + timedelta(days=random.randint(0, dias_no_periodo),
                                          hours=random.randint(0, 23),
                                          minutes=random.randint(0, 59))
    quantidade = random.randint(1, 5)
    preco_unitario = info_produto['preco']
    preco_total = quantidade * preco_unitario
    loja = random.choice(lojas)

    dados_vendas.append({
        'ID_Venda': i + 1,
        'Data': data_venda,
        'Produto': nome_produto,
        'Categoria': info_produto['categoria'],
        'Quantidade': quantidade,
        'Preco_Unitario': preco_unitario,
        'Preco_Total': preco_total,
        'Loja': loja
    })

df_vendas = pd.DataFrame(dados_vendas)

df_vendas.to_csv(arquivo_saida, index=False, sep=';', decimal=',', encoding='utf-8-sig')
print(f"Arquivo ${arquivo_saida} criado com sucesso com ${num_registros} registros!")
