from pathlib import Path
import time
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

BASE_DIR = Path(__file__).resolve().parents[1]
DADOS_DIR = BASE_DIR / "dados"
MODELOS_DIR = BASE_DIR / "modelos"
RESULTADOS_DIR = BASE_DIR / "resultados"
DATASET = DADOS_DIR / "dataset_lag_publico.csv"

FEATURES = ["throughput", "congestion", "packet_loss", "latency", "jitter"]
TARGET = "rotulo"
ORDEM_CLASSES = ["normal", "moderado", "severo"]


def criar_modelos():
    scaler = ColumnTransformer([("scaler", StandardScaler(), FEATURES)], remainder="drop")
    return {
        "Random Forest": Pipeline([
            ("modelo", RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced"))
        ]),
        "Decision Tree": Pipeline([
            ("modelo", DecisionTreeClassifier(random_state=42, class_weight="balanced"))
        ]),
        "KNN": Pipeline([
            ("preprocessamento", scaler),
            ("modelo", KNeighborsClassifier(n_neighbors=5))
        ]),
        "Logistic Regression": Pipeline([
            ("preprocessamento", scaler),
            ("modelo", LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42))
        ]),
    }


def main() -> None:
    MODELOS_DIR.mkdir(exist_ok=True)
    RESULTADOS_DIR.mkdir(exist_ok=True)

    if not DATASET.exists():
        raise FileNotFoundError("Execute primeiro: python3 scripts/preparar_dataset.py")

    df = pd.read_csv(DATASET)
    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42, stratify=y
    )

    resultados = []
    melhor_nome = None
    melhor_modelo = None
    melhor_f1 = -1
    melhor_pred = None

    for nome, modelo in criar_modelos().items():
        modelo.fit(X_train, y_train)

        inicio = time.perf_counter()
        y_pred = modelo.predict(X_test)
        fim = time.perf_counter()
        tempo_medio_ms = ((fim - inicio) / len(X_test)) * 1000

        metricas = {
            "modelo": nome,
            "acuracia": accuracy_score(y_test, y_pred),
            "precisao_macro": precision_score(y_test, y_pred, average="macro", zero_division=0),
            "recall_macro": recall_score(y_test, y_pred, average="macro", zero_division=0),
            "f1_macro": f1_score(y_test, y_pred, average="macro", zero_division=0),
            "tempo_inferencia_ms": tempo_medio_ms,
        }
        resultados.append(metricas)

        nome_arquivo = nome.lower().replace(" ", "_") + ".pkl"
        joblib.dump(modelo, MODELOS_DIR / nome_arquivo)

        if metricas["f1_macro"] > melhor_f1:
            melhor_f1 = metricas["f1_macro"]
            melhor_nome = nome
            melhor_modelo = modelo
            melhor_pred = y_pred

    df_resultados = pd.DataFrame(resultados).sort_values("f1_macro", ascending=False)
    df_resultados.to_csv(RESULTADOS_DIR / "metricas_modelos.csv", index=False)

    joblib.dump(melhor_modelo, MODELOS_DIR / "melhor_modelo_lag.pkl")

    print("Resultados dos modelos:")
    print(df_resultados)
    print(f"\nMelhor modelo: {melhor_nome}")

    # Matriz de confusão do melhor modelo
    cm = confusion_matrix(y_test, melhor_pred, labels=ORDEM_CLASSES)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=ORDEM_CLASSES)
    disp.plot(values_format="d")
    plt.title(f"Matriz de Confusão - {melhor_nome}")
    plt.tight_layout()
    plt.savefig(RESULTADOS_DIR / "matriz_confusao_melhor_modelo.png", dpi=150)
    plt.close()

    # Comparação de modelos por F1-score
    ax = df_resultados.plot(kind="bar", x="modelo", y="f1_macro", legend=False)
    ax.set_title("Comparação de Modelos - F1-score Macro")
    ax.set_ylabel("F1-score Macro")
    ax.set_xlabel("Modelo")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(RESULTADOS_DIR / "comparacao_modelos_f1.png", dpi=150)
    plt.close()

    # Importância das variáveis, quando disponível
    if melhor_nome in ["Random Forest", "Decision Tree"]:
        importancias = melhor_modelo.named_steps["modelo"].feature_importances_
        df_imp = pd.DataFrame({"variavel": FEATURES, "importancia": importancias}).sort_values("importancia", ascending=False)
        df_imp.to_csv(RESULTADOS_DIR / "importancia_variaveis.csv", index=False)
        ax = df_imp.plot(kind="bar", x="variavel", y="importancia", legend=False)
        ax.set_title(f"Importância das Variáveis - {melhor_nome}")
        ax.set_ylabel("Importância")
        ax.set_xlabel("Variável")
        plt.xticks(rotation=25, ha="right")
        plt.tight_layout()
        plt.savefig(RESULTADOS_DIR / "importancia_variaveis.png", dpi=150)
        plt.close()


if __name__ == "__main__":
    main()
