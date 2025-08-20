# Importação das bibliotecas necessárias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# --- 1. Carregamento e Preparação dos Dados ---

# Carregar o dataset a partir do arquivo CSV
# O arquivo 'Iris.csv' deve estar na mesma pasta do script
try:
    df_iris = pd.read_csv('Iris.csv')
except FileNotFoundError:
    print("Erro: Arquivo 'Iris.csv' não encontrado. Certifique-se de que ele está na pasta correta.")
    exit()

# Remover a coluna 'Id' que não é necessária para o modelo
df_iris = df_iris.drop('Id', axis=1)

# Separar os dados em atributos (X) e alvo (y)
# X contém as 4 colunas com as medidas das flores
X = df_iris.drop('Species', axis=1)
# y contém a coluna com as espécies (o que queremos prever)
y = df_iris['Species']

# Dividir os dados em conjuntos de treino e teste
# 80% dos dados para treino e 20% para teste
# random_state=42 garante que a divisão seja sempre a mesma, para reprodutibilidade
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print("Dados carregados e divididos com sucesso.")
print(f"Tamanho do conjunto de treino: {X_train.shape[0]} amostras")
print(f"Tamanho do conjunto de teste: {X_test.shape[0]} amostras")
print("-" * 30)

# --- 2. Escolha e Treinamento do Modelo ---

# Escolha do modelo: K-Nearest Neighbors (KNN)
# É um modelo simples, intuitivo e que funciona muito bem para o dataset Iris.
# n_neighbors=3 significa que ele vai olhar para os 3 vizinhos mais próximos para classificar uma nova flor.
model = KNeighborsClassifier(n_neighbors=3)

# Treinamento do modelo com os dados de treino
model.fit(X_train, y_train)

print("Modelo KNN treinado com sucesso.")
print("-" * 30)

# --- 3. Avaliação do Modelo ---

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Calcular a acurácia (percentual de acertos)
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {accuracy:.2f}")
print(f"Isso significa que o modelo acertou {accuracy * 100:.2f}% das previsões no conjunto de teste.")
print("-" * 30)

# Exibir outras métricas importantes
print("Matriz de Confusão:")
# Mostra quantos de cada classe foram classificados corretamente.
# A diagonal principal mostra os acertos. Fora dela, os erros.
print(confusion_matrix(y_test, y_pred))
print("-" * 30)

print("Relatório de Classificação:")
# Mostra precisão, recall e f1-score para cada classe.
print(classification_report(y_test, y_pred))

# --- Exemplo de Previsão com Novos Dados ---
# Suponha uma nova flor com as seguintes medidas:
# SepalLengthCm = 5.0, SepalWidthCm = 3.5, PetalLengthCm = 1.5, PetalWidthCm = 0.2
nova_flor = [[5.0, 3.5, 1.5, 0.2]]
previsao = model.predict(nova_flor)
print("-" * 30)
print(f"Previsão para uma nova flor {nova_flor}: Espécie = {previsao[0]}")