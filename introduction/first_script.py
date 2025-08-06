import pandas as pd

dados = {
    'Nome': ['Ana', 'Bruno', 'carla', 'DANIEL', 'Eduardo da silva', 'Fernanda Alves', 'gustavo', 'Helena', 'IGOR', 'Julia'],
    'Idade': [28, 35, 22, 41, 30, None, 33, 29, 24, None],
    'Cidade': [
        'São Paulo', 'Rio de Janeiro', 'Curitiba', 'SALVADOR', 'Belo Horizonte',
        'fortaleza', 'Brasília', 'Manaus', 'Recife', 'porto alegre'
    ]
}

df = pd.DataFrame(dados)
print(f'DataFrame completo: \n{df}')




# ---------------------- EXPLORAR DADOS DENTRO DO DATAFRAME ----------------------
primeiras_linhas = df.head(2)
print(f'\nPrimeiras linhas do dataframe: \n{primeiras_linhas}')

ultimas_linhas = df.tail(2)
print(f'\nUltimas linhas do dataframe: \n{ultimas_linhas}')

dimensoes = df.shape
print(f'\nDimensoes do dataframe: \n{dimensoes}')

estatisticas = df.describe()
print(f'\nEstatisticas do dataframe: \n{estatisticas}')




# ---------------------- FILTRANDO OS DADOS ----------------------
maiores_que_30_anos = df[df['Idade'] > 30]
print(f'\nPessoas com mais de 30 anos: \n{maiores_que_30_anos}')

menores_que_30_anos = df[df['Idade'] <= 30]
print(f'\nPessoas com menos de 30 anos: \n{menores_que_30_anos}')

filtro_com_mais_condicoes = df[(df['Cidade'] == 'São Paulo') & (df['Idade'] < 30)]
print(f'\nFiltro com mais condições: \n{filtro_com_mais_condicoes}')





# ---------------------- MANIPULANDO OS DADOS ---------------------
df['Estado'] = ['SP', 'RJ', 'PR', 'BA', 'RS', 'CE', 'DF', 'AM', 'PE', 'DF']
print(f'\nAdicionando coluna de estado: \n{df}')

df['Idade'] = df['Idade'] + 1
print(f'\nModificando valor da coluna Idade: \n{df}')


df_sem_nulos = df.dropna()
print(f'\nDataframe retirando valores nulos : \n{df_sem_nulos}')

media_idade = df['Idade'].mean() # média da coluna Idade
df_preenchido = df['Idade'].fillna(media_idade)
print(f'\nAo invés de excluir os dados nulos, adicionamos e média das outras idades nos campos nulos : \n{df_preenchido}')

df_idade_media_por_cidade = df.groupby('Cidade')['Idade'].mean()
print(f'\nDataframe de idade média por cidade: \n{df_idade_media_por_cidade}')






# -----------------------------------------------

# PROCESSO DE NORMALIZAÇÃO

print("--- Iniciando a Normalização dos Dados ---\n")

print("1. Padronizando a capitalização de 'Nome' e 'Cidade'...")
df['Nome'] = df['Nome'].str.title()
df['Cidade'] = df['Cidade'].str.title()


# Passo 2: Tratar os valores ausentes na coluna 'Idade'.
print("1. Padronizando a capitalização de 'Nome' e 'Cidade'...")
media_idade_original = df['Idade'].mean()
print(f"\n2. A média de idade (ignorando nulos) é: {media_idade_original:.2f}")


df['Idade'] = df['Idade'].fillna(media_idade_original)
print("Valores nulos da coluna 'Idade' foram preenchidos com a média.")


print("\n3. Convertendo a coluna 'Idade' para o tipo inteiro...")
df['Idade'] = df['Idade'].astype(int)


# Criamos um mapeamento cidade -> estado para garantir a consistência lógica.
mapa_estados = {
    'São Paulo': 'SP',
    'Rio De Janeiro': 'RJ',
    'Curitiba': 'PR',
    'Salvador': 'BA',
    'Belo Horizonte': 'MG',
    'Fortaleza': 'CE',
    'Brasília': 'DF',
    'Manaus': 'AM',
    'Recife': 'PE',
    'Porto Alegre': 'RS'
}
print("\n4. Adicionando coluna 'Estado' com base na cidade (dados corrigidos)...")
df['Estado'] = df['Cidade'].map(mapa_estados)


print("\n" + "="*50)
print("--- DataFrame Final, Normalizado e Pronto para Análise ---")
print(df)
print("\n--- Informações Finais do DataFrame Limpo ---")
df.info()

