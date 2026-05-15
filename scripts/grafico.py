import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dados/dataset_lag.csv")

plt.figure(figsize=(10,6))

for rotulo in df["rotulo"].unique():

    dados = df[df["rotulo"] == rotulo]

    plt.scatter(
        dados["latencia_media"],
        dados["jitter"],
        label=rotulo
    )

plt.xlabel("Latência Média (ms)")
plt.ylabel("Jitter (ms)")
plt.title("Distribuição dos Cenários de Rede")

plt.legend()

plt.savefig("resultados/grafico.png")

print("Gráfico salvo em resultados/grafico.png")
