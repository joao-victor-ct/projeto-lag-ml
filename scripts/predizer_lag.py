import joblib
import pandas as pd
import sys

if len(sys.argv) != 4:
    print("Uso: python3 predizer_lag.py latencia jitter perda")
    sys.exit(1)

latencia = float(sys.argv[1])
jitter = float(sys.argv[2])
perda = float(sys.argv[3])

modelo = joblib.load("modelos/modelo_lag.pkl")

entrada = pd.DataFrame([{
    "latencia_media": latencia,
    "jitter": jitter,
    "perda_pacotes": perda
}])

resultado = modelo.predict(entrada)

print("Classificação:", resultado[0])
