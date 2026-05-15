# 🎮 Predição de Eventos de Alta Latência (Lag) em Jogos Online utilizando Machine Learning

## 📌 Sobre o Projeto

Este projeto propõe uma solução baseada em Machine Learning para prever eventos de alta latência (lag) em jogos online utilizando métricas de rede coletadas em tempo quase real.

A aplicação utiliza um ambiente emulado com Mininet para simular diferentes condições de rede, incluindo:

* baixa latência;
* jitter;
* perda de pacotes;
* congestionamento;
* cenários severos de degradação.

Os dados coletados são utilizados para treinar um modelo de classificação capaz de identificar automaticamente o estado da rede.

---

# 🚀 Funcionalidades

✅ Emulação de rede com Mininet

✅ Simulação de lag com tc/netem

✅ Coleta automática de métricas de rede

✅ Geração automática de dataset CSV

✅ Treinamento de modelo de Machine Learning

✅ Predição automática de cenários de rede

✅ Geração de gráficos para análise

✅ Estrutura pronta para expansão futura

---

# 🧠 Classificações da Rede

O modelo classifica a rede em três categorias:

| Classe   | Descrição                        |
| -------- | -------------------------------- |
| normal   | Rede estável e jogável           |
| moderado | Pequeno impacto na jogabilidade  |
| severo   | Lag severo e perda de desempenho |

---

# 🏗️ Arquitetura do Projeto

```text
Cliente (h1)
      ↓
Rede Emulada (Mininet + tc/netem)
      ↓
Servidor (h2)
      ↓
Coleta de Métricas
      ↓
Dataset CSV
      ↓
Treinamento da IA
      ↓
Predição de Lag
```

---

# 📁 Estrutura do Projeto

```text
projeto-lag-ml/
├── dados/
│   └── dataset_lag.csv
├── imagens/
├── modelos/
│   └── modelo_lag.pkl
├── resultados/
│   └── grafico.png
├── scripts/
│   ├── coletar_ping.py
│   ├── grafico.py
│   ├── predizer_lag.py
│   ├── topologia.py
│   └── treinar_modelo.py
├── README.md
└── venv/
```

---

# 🛠️ Tecnologias Utilizadas

| Tecnologia   | Finalidade                     |
| ------------ | ------------------------------ |
| Python       | Linguagem principal            |
| Mininet      | Emulação de rede               |
| tc/netem     | Simulação de condições de rede |
| Scikit-learn | Machine Learning               |
| Pandas       | Manipulação de dados           |
| Matplotlib   | Geração de gráficos            |
| Git/GitHub   | Versionamento                  |

---

# 💻 Requisitos

## Sistema operacional

Recomendado:

* Ubuntu 22.04+
* Debian 12+

---

# ⚙️ Instalação Completa

## 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/projeto-lag-ml.git
```

Entre na pasta:

```bash
cd projeto-lag-ml
```

---

## 2. Instalar dependências do sistema

```bash
sudo apt update
```

```bash
sudo apt install mininet python3 python3-pip python3-venv python3-full git -y
```

---

## 3. Criar ambiente virtual Python

```bash
python3 -m venv venv
```

---

## 4. Ativar ambiente virtual

```bash
source venv/bin/activate
```

O terminal ficará semelhante a:

```text
(venv) usuario@linux:~/projeto-lag-ml$
```

---

## 5. Instalar bibliotecas Python

```bash
pip install pandas scikit-learn matplotlib joblib
```

---

# ▶️ Como Executar o Projeto

# ETAPA 1 — Limpar sessões antigas do Mininet

```bash
sudo mn -c
```

---

# ETAPA 2 — Iniciar a topologia

```bash
sudo python3 scripts/topologia.py
```

Resultado esperado:

```text
mininet>
```

---

# 🌐 Testando a Topologia

Dentro do Mininet:

```bash
pingall
```

Resultado esperado:

```text
*** Results: 0% dropped
```

---

# 📡 Simulação de Cenários de Rede

# 🟢 Cenário NORMAL

```bash
h1 tc qdisc add dev h1-eth0 root netem delay 20ms loss 0%
```

---

# 🟡 Cenário MODERADO

Remover configuração anterior:

```bash
h1 tc qdisc del dev h1-eth0 root
```

Aplicar cenário:

```bash
h1 tc qdisc add dev h1-eth0 root netem delay 80ms 20ms loss 2%
```

---

# 🔴 Cenário SEVERO

Remover configuração anterior:

```bash
h1 tc qdisc del dev h1-eth0 root
```

Aplicar cenário:

```bash
h1 tc qdisc add dev h1-eth0 root netem delay 180ms 50ms loss 8%
```

---

# 📊 Coleta de Métricas

Entre no host virtual h1:

```bash
h1 /bin/bash
```

Vá até a pasta do projeto:

```bash
cd /home/SEU_USUARIO/projeto-lag-ml
```

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

---

# 🟢 Coleta NORMAL

```bash
python3 scripts/coletar_ping.py normal
```

---

# 🟡 Coleta MODERADA

```bash
python3 scripts/coletar_ping.py moderado
```

---

# 🔴 Coleta SEVERA

```bash
python3 scripts/coletar_ping.py severo
```

---

# 🗂️ Dataset Gerado

O dataset será salvo automaticamente em:

```text
dados/dataset_lag.csv
```

Formato esperado:

```csv
data,latencia_media,jitter,perda_pacotes,rotulo
2026...,20.5,1.8,0,normal
2026...,82.4,19.5,2,moderado
2026...,190.1,60.2,8,severo
```

---

# 🤖 Treinamento do Modelo

Saia do Mininet:

```bash
exit
```

Execute:

```bash
python3 scripts/treinar_modelo.py
```

Resultado esperado:

```text
Acurácia: 1.0
```

O modelo será salvo em:

```text
modelos/modelo_lag.pkl
```

---

# 🔮 Predição de Lag

# Exemplo NORMAL

```bash
python3 scripts/predizer_lag.py 20 2 0
```

Resultado esperado:

```text
Classificação: normal
```

---

# Exemplo MODERADO

```bash
python3 scripts/predizer_lag.py 80 20 2
```

Resultado esperado:

```text
Classificação: moderado
```

---

# Exemplo SEVERO

```bash
python3 scipts/predizer_lag.py 180 50 8
```

Resultado esperado:

```text
Classificação: severo
```

---

# 📈 Geração de Gráficos

Execute:

```bash
python3 scripts/grafico.py
```

O gráfico será salvo em:

```text
resultados/grafico.png
```

---

# 📋 Métricas Utilizadas

## Métricas de Rede

* Latência
* Jitter
* Perda de pacotes

## Métricas de Machine Learning

* Acurácia
* Precisão
* Recall
* F1-score

---

# 🧪 Fluxo Completo de Teste

## 1. Subir topologia

```bash
sudo python3 scripts/topologia.py
```

---

## 2. Aplicar cenário

```bash
h1 tc qdisc add dev h1-eth0 root netem delay 180ms 50ms loss 8%
```

---

## 3. Entrar no host virtual

```bash
h1 /bin/bash
```

---

## 4. Coletar métricas

```bash
python3 scripts/coletar_ping.py severo
```

---

## 5. Treinar IA

```bash
python3 scripts/treinar_modelo.py
```

---

## 6. Realizar predição

```bash
python3 scripts/predizer_lag.py 180 50 8
```

---

# 🐞 Problemas Comuns

# Permissão negada no dataset

Corrigir:

```bash
sudo chown $USER:$USER dados/dataset_lag.csv
```

---

# Mininet travado

Limpar sessões:

```bash
sudo mn -c
```

---

# Bibliotecas não encontradas

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

---

# Erro com controlador OpenFlow

Utilize a topologia configurada sem controlador.

---

# 🚀 Melhorias Futuras

* Integração com iPerf3;
* Inferência em tempo real;
* Dashboard Grafana;
* Redes neurais profundas;
* Dockerização do projeto;
* API Flask/FastAPI;
* Monitoramento contínuo.

---

# 👨‍💻 Autores

## João Victor Coelho Trigueiro
## Anderson Gabriel Souza do Nascimento

Instituto Federal da Paraíba (IFPB)

Curso: Redes de Computadores

---

#
