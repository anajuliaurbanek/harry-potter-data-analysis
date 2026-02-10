import pandas as pd
import matplotlib.pyplot as plt

# 1) Carregar dados
df = pd.read_csv("data/harry_potter_characters.csv")

# 2) Exploração básica
print("Primeiras linhas:")
print(df.head())

print("\nColunas:")
print(df.columns)

print("\nTamanho do dataset:")
print(df.shape)

print("\nValores nulos por coluna:")
print(df.isna().sum())

# 3) Limpeza simples (ajuste os nomes das colunas conforme o CSV real)
# Exemplo: padronizar nomes de casas
if "house" in df.columns:
    df["house"] = df["house"].fillna("Unknown")
    df["house"] = df["house"].str.strip()

# 4) Análises
if "house" in df.columns:
    house_counts = df["house"].value_counts()
    print("\nPersonagens por casa:")
    print(house_counts)

    # 5) Gráfico: personagens por casa
    house_counts.plot(kind="bar")
    plt.title("Distribuição de personagens por casa")
    plt.xlabel("Casa")
    plt.ylabel("Quantidade")
    plt.tight_layout()
    plt.show()

# Gênero
if "gender" in df.columns:
    gender_counts = df["gender"].fillna("Unknown").value_counts()
    gender_counts.plot(kind="bar")
    plt.title("Distribuição de personagens por gênero")
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade")
    plt.tight_layout()
    plt.show()

# Espécies
if "species" in df.columns:
    species_counts = df["species"].fillna("Unknown").value_counts().head(10)
    species_counts.plot(kind="bar")
    plt.title("Top 10 espécies mais comuns")
    plt.xlabel("Espécie")
    plt.ylabel("Quantidade")
    plt.tight_layout()
    plt.show()
