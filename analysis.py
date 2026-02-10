import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("data/harry_potter_characters.csv")

print("Colunas do dataset:")
print(df.columns)

print("\nPrimeiras linhas:")
print(df.head())

# Tratar valores nulos
df["house"] = df["house"].fillna("Unknown")
df["gender"] = df["gender"].fillna("Unknown")
df["species"] = df["species"].fillna("Unknown")

# Contagem por casa
house_counts = df["house"].value_counts()
print("\nPersonagens por casa:")
print(house_counts)

# Gráfico: personagens por casa
house_counts.plot(kind="bar")
plt.title("Distribuição de personagens por casa")
plt.xlabel("Casa")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.show()

# Contagem por gênero
gender_counts = df["gender"].value_counts()
gender_counts.plot(kind="bar")
plt.title("Distribuição de personagens por gênero")
plt.xlabel("Gênero")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.show()

# Top espécies
species_counts = df["species"].value_counts()
species_counts.plot(kind="bar")
plt.title("Distribuição de espécies")
plt.xlabel("Espécie")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.show()
