import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

import joblib

df = pd.read_csv("dados/dataset_lag.csv")

X = df[[
    "latencia_media",
    "jitter",
    "perda_pacotes"
]]

y = df["rotulo"]

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

modelo = RandomForestClassifier(random_state=42)

modelo.fit(X_treino, y_treino)

predicoes = modelo.predict(X_teste)

print("Acurácia:", accuracy_score(y_teste, predicoes))

print(classification_report(y_teste, predicoes))

joblib.dump(modelo, "modelos/modelo_lag.pkl")

print("Modelo salvo com sucesso!")
