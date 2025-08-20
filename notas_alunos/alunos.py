import pandas as pd
import matplotlib.pyplot as plt

# Lê os dados do dataset
dados = pd.read_csv('alunos.csv')

# Apresenta as primeiras linhas do dataset
# print(dados.head())

# Cria o campo média e insere a média do aluno
dados['media'] = dados[['nota1', 'nota2', 'nota3']].mean(axis=1)

# Cria o campo situação e insere a situação do aluno (Aprovado/Reprovado)
dados['situacao'] = dados['media'].apply(lambda x: 'Aprovado' if x >= 7 else 'Reprovado')

print(dados.head())

total_aprovados = dados[dados['situacao'] == 'Aprovado'].shape[0]
print("Alunos Aprovados: ", total_aprovados)


# gerar um grafico de media por idade
df_gourp_by_idade = dados.groupby('idade')['media'].mean()\
    .plot(kind='bar')
plt.title('Média por Idade dos Alunos')
plt.xlabel('Jao')
plt.ylabel('Maria')
plt.show()


df_group_aproveado = dados.groupby('situacao')['media'].mean()\
    .plot(kind='bar')

plt.title('Situaçõ por Idade dos Alunos')
plt.xlabel('Jao')
plt.ylabel('Maria')
plt.show()

#plt.show()