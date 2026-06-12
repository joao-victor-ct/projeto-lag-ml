from pathlib import Path
import sys
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
MODELO = BASE_DIR / "modelos" / "melhor_modelo_lag.pkl"
FEATURES = ["throughput", "congestion", "packet_loss", "latency", "jitter"]


def main() -> None:
    if len(sys.argv) != 6:
        print("Uso: python3 scripts/predizer_lag.py <throughput> <congestion> <packet_loss> <latency> <jitter>")
        print("Exemplo: python3 scripts/predizer_lag.py 1.2 40 10 80 2")
        sys.exit(1)

    if not MODELO.exists():
        raise FileNotFoundError("Modelo não encontrado. Execute primeiro: python3 scripts/treinar_modelos.py")

    valores = [float(v) for v in sys.argv[1:]]
    entrada = pd.DataFrame([valores], columns=FEATURES)

    modelo = joblib.load(MODELO)
    predicao = modelo.predict(entrada)[0]

    print(f"Classificação prevista: {predicao}")

    if hasattr(modelo, "predict_proba"):
        probabilidades = modelo.predict_proba(entrada)[0]
        classes = modelo.classes_
        print("Probabilidades:")
        for classe, prob in zip(classes, probabilidades):
            print(f"  {classe}: {prob:.2%}")


if __name__ == "__main__":
    main()
