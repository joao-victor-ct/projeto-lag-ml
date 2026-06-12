from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]
DATASET = BASE_DIR / "dados" / "dataset_lag_publico.csv"
RESULTADOS_DIR = BASE_DIR / "resultados"
FEATURES = ["throughput", "congestion", "packet_loss", "latency", "jitter"]


def main() -> None:
    RESULTADOS_DIR.mkdir(exist_ok=True)
    df = pd.read_csv(DATASET)

    ax = df["rotulo"].value_counts().reindex(["normal", "moderado", "severo"]).plot(kind="bar")
    ax.set_title("Distribuição das Classes")
    ax.set_xlabel("Classe")
    ax.set_ylabel("Quantidade de registros")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(RESULTADOS_DIR / "distribuicao_classes.png", dpi=150)
    plt.close()

    for col in FEATURES:
        ax = df.boxplot(column=col, by="rotulo")
        plt.title(f"Distribuição de {col} por classe")
        plt.suptitle("")
        ax.set_xlabel("Classe")
        ax.set_ylabel(col)
        plt.tight_layout()
        plt.savefig(RESULTADOS_DIR / f"boxplot_{col}.png", dpi=150)
        plt.close()

    print(f"Gráficos salvos em: {RESULTADOS_DIR}")


if __name__ == "__main__":
    main()
