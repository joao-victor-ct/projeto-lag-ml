from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DADOS_DIR = BASE_DIR / "dados"
ARQUIVO_ENTRADA = DADOS_DIR / "network_dataset_labeled.csv"
ARQUIVO_SAIDA = DADOS_DIR / "dataset_lag_publico.csv"

FEATURES = ["throughput", "congestion", "packet_loss", "latency", "jitter"]
ANOMALIAS = [
    "anomaly_throughput",
    "anomaly_congestion",
    "anomaly_packet_loss",
    "anomaly_latency",
    "anomaly_jitter",
]


def classificar_lag(qtd_anomalias: int) -> str:
    """Converte a quantidade de anomalias em três classes do projeto."""
    if qtd_anomalias == 0:
        return "normal"
    if qtd_anomalias == 1:
        return "moderado"
    return "severo"


def main() -> None:
    if not ARQUIVO_ENTRADA.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {ARQUIVO_ENTRADA}")

    df = pd.read_csv(ARQUIVO_ENTRADA)

    colunas_necessarias = FEATURES + ANOMALIAS
    faltando = [col for col in colunas_necessarias if col not in df.columns]
    if faltando:
        raise ValueError(f"Colunas ausentes no dataset: {faltando}")

    df_modelo = df[FEATURES + ANOMALIAS].copy()
    df_modelo["qtd_anomalias"] = df_modelo[ANOMALIAS].sum(axis=1)
    df_modelo["rotulo"] = df_modelo["qtd_anomalias"].apply(classificar_lag)

    # Mantém no CSV final apenas as métricas de rede e o rótulo usado no ML.
    df_final = df_modelo[FEATURES + ["rotulo"]]
    df_final.to_csv(ARQUIVO_SAIDA, index=False)

    print(f"Dataset preparado em: {ARQUIVO_SAIDA}")
    print("Distribuição das classes:")
    print(df_final["rotulo"].value_counts())


if __name__ == "__main__":
    main()
