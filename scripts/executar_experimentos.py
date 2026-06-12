import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "preparar_dataset.py",
    "gerar_graficos_dataset.py",
    "treinar_modelos.py",
]

for script in SCRIPTS:
    caminho = BASE_DIR / "scripts" / script
    print(f"\nExecutando {script}...")
    subprocess.run([sys.executable, str(caminho)], check=True)

print("\nExperimentos concluídos.")
