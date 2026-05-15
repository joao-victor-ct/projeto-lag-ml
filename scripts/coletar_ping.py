import subprocess
import re
import csv
import sys
from datetime import datetime

if len(sys.argv) < 2:
    print("Uso: python3 coletar_ping.py normal|moderado|severo")
    sys.exit(1)

rotulo = sys.argv[1]

arquivo = "dados/dataset_lag.csv"

comando = ["ping", "-c", "20", "10.0.0.2"]

resultado = subprocess.run(comando, capture_output=True, text=True)

saida = resultado.stdout

latencias = re.findall(r"time=([\d.]+)", saida)

if latencias:
    latencias = [float(x) for x in latencias]

    latencia_media = sum(latencias) / len(latencias)

    jitter = max(latencias) - min(latencias)

else:
    latencia_media = 0
    jitter = 0

perda_match = re.search(r"(\d+)% packet loss", saida)

perda = float(perda_match.group(1)) if perda_match else 100

with open(arquivo, "a", newline="") as f:

    escritor = csv.writer(f)

    if f.tell() == 0:
        escritor.writerow([
            "data",
            "latencia_media",
            "jitter",
            "perda_pacotes",
            "rotulo"
        ])

    escritor.writerow([
        datetime.now(),
        latencia_media,
        jitter,
        perda,
        rotulo
    ])

print("Coleta salva com sucesso")
print("Latência média:", latencia_media)
print("Jitter:", jitter)
print("Perda:", perda)
print("Rótulo:", rotulo)
