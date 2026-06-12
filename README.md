# Predição de Eventos de Alta Latência em Jogos Online utilizando Machine Learning

Projeto desenvolvido para a disciplina de **Avaliação de Desempenho em Redes de Computadores** do IFPB.

O objetivo do projeto é classificar o estado de uma rede em três categorias — **normal**, **moderado** ou **severo** — utilizando métricas de desempenho de rede e algoritmos de Machine Learning.

## Autores

* João Victor Coelho Trigueiro
* Anderson Gabriel Souza do Nascimento

## Objetivo

Desenvolver uma solução capaz de prever eventos de degradação de Qualidade de Serviço (QoS), como lag em jogos online, a partir de métricas de rede.

As métricas utilizadas são:

* Throughput
* Congestionamento
* Jitter
* Latência
* Perda de pacotes

## Tecnologias utilizadas

* Python 3
* Pandas
* Scikit-learn
* Matplotlib
* Joblib
* Git/GitHub

## Estrutura do projeto

```text
projeto-lag-ml/
├── dados/
│   ├── dataset_lag.csv
│   ├── dataset_lag_publico.csv
│   ├── network_dataset.csv
│   └── network_dataset_labeled.csv
├── modelos/
│   ├── decision_tree.pkl
│   ├── knn.pkl
│   ├── logistic_regression.pkl
│   ├── melhor_modelo_lag.pkl
│   ├── modelo_lag.pkl
│   └── random_forest.pkl
├── resultados/
│   ├── boxplot_congestion.png
│   ├── boxplot_jitter.png
│   ├── boxplot_latency.png
│   ├── boxplot_packet_loss.png
│   ├── boxplot_throughput.png
│   ├── comparacao_modelos_f1.png
│   ├── distribuicao_classes.png
│   ├── importancia_variaveis.csv
│   ├── importancia_variaveis.png
│   ├── matriz_confusao_melhor_modelo.png
│   └── metricas_modelos.csv
├── scripts/
│   ├── coletar_ping.py
│   ├── executar_experimentos.py
│   ├── gerar_graficos_dataset.py
│   ├── grafico.py
│   ├── predizer_lag.py
│   ├── preparar_dataset.py
│   ├── topologia.py
│   ├── treinar_modelo.py
│   └── treinar_modelos.py
└── README.md
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/joao-victor-ct/projeto-lag-ml.git
cd projeto-lag-ml
```

Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install pandas scikit-learn matplotlib joblib numpy
```

## Execução completa do projeto

Para executar todo o fluxo experimental automaticamente:

```bash
python3 scripts/executar_experimentos.py
```

Esse script executa:

1. Preparação do dataset;
2. Geração dos gráficos;
3. Treinamento dos modelos;
4. Comparação dos algoritmos;
5. Salvamento dos resultados.

## Testes disponíveis

### Teste 1 — Preparar o dataset

Executa o tratamento do dataset público e cria o arquivo `dataset_lag_publico.csv`.

```bash
python3 scripts/preparar_dataset.py
```

Saída esperada:

```text
Dataset preparado em: dados/dataset_lag_publico.csv
Distribuição das classes:
normal      747
moderado    171
severo       83
```

Esse teste verifica se o dataset foi carregado, tratado e rotulado corretamente.

---

### Teste 2 — Gerar gráficos do dataset

```bash
python3 scripts/gerar_graficos_dataset.py
```

Esse teste gera os gráficos de análise exploratória.

Arquivos esperados na pasta `resultados/`:

```text
distribuicao_classes.png
boxplot_congestion.png
boxplot_jitter.png
boxplot_latency.png
boxplot_packet_loss.png
boxplot_throughput.png
```

Para abrir os gráficos:

```bash
xdg-open resultados/distribuicao_classes.png
xdg-open resultados/boxplot_latency.png
xdg-open resultados/boxplot_jitter.png
xdg-open resultados/boxplot_packet_loss.png
xdg-open resultados/boxplot_throughput.png
```

---

### Teste 3 — Treinar e comparar modelos

```bash
python3 scripts/treinar_modelos.py
```

Esse teste treina e compara os seguintes algoritmos:

* Random Forest
* Decision Tree
* KNN
* Logistic Regression

Saída esperada aproximada:

```text
Resultados dos modelos:
Random Forest        0.9601
Decision Tree        0.9534
KNN                  0.8970
Logistic Regression  0.7906

Melhor modelo: Random Forest
```

Esse teste verifica:

* Acurácia;
* Precisão macro;
* Recall macro;
* F1-score macro;
* Tempo de inferência;
* Melhor modelo encontrado.

Arquivos gerados:

```text
resultados/metricas_modelos.csv
resultados/comparacao_modelos_f1.png
resultados/matriz_confusao_melhor_modelo.png
resultados/importancia_variaveis.csv
resultados/importancia_variaveis.png
modelos/melhor_modelo_lag.pkl
```

---

### Teste 4 — Abrir comparação dos modelos

```bash
xdg-open resultados/comparacao_modelos_f1.png
```

Esse gráfico mostra a comparação dos modelos usando F1-score.

O melhor modelo encontrado foi o **Random Forest**, com desempenho superior aos demais.

---

### Teste 5 — Abrir matriz de confusão

```bash
xdg-open resultados/matriz_confusao_melhor_modelo.png
```

A matriz de confusão mostra os acertos e erros do melhor modelo nas classes:

* normal
* moderado
* severo

Esse teste ajuda a verificar se o modelo consegue diferenciar corretamente os níveis de degradação da rede.

---

### Teste 6 — Abrir importância das variáveis

```bash
xdg-open resultados/importancia_variaveis.png
```

Também é possível visualizar os valores em CSV:

```bash
cat resultados/importancia_variaveis.csv
```

Resultado obtido:

```text
congestion    0.2678
jitter        0.2321
packet_loss   0.2135
throughput    0.1711
latency       0.1154
```

Interpretação:

* O congestionamento foi a variável mais importante;
* Jitter e perda de pacotes também tiveram forte impacto;
* Throughput teve influência intermediária;
* Latência apresentou menor importância relativa no modelo.

---

### Teste 7 — Predição manual de cenário normal

```bash
python3 scripts/predizer_lag.py 0.1 5 0.1 5 0
```

Formato dos parâmetros:

```text
throughput congestion jitter latency packet_loss
```

Esse teste simula uma rede com baixa latência, baixo jitter, baixa perda e pouco congestionamento.

---

### Teste 8 — Predição manual de cenário moderado

```bash
python3 scripts/predizer_lag.py 1.2 40 10 80 2
```

Saída esperada aproximada:

```text
Classificação prevista: moderado
Probabilidades:
moderado: 57.50%
normal: 6.00%
severo: 36.50%
```

Esse teste simula uma rede com degradação intermediária.

---

### Teste 9 — Predição manual de cenário severo

```bash
python3 scripts/predizer_lag.py 3.0 90 40 180 8
```

Saída esperada aproximada:

```text
Classificação prevista: severo
Probabilidades:
severo: 76.50%
moderado: 21.00%
normal: 2.50%
```

Esse teste simula uma rede com alta latência, alto jitter, alta perda de pacotes e congestionamento elevado.

---

### Teste 10 — Verificar os arquivos de saída

```bash
ls dados
ls modelos
ls resultados
ls scripts
```

Esse teste verifica se todos os arquivos necessários foram criados corretamente.

Arquivos principais esperados:

```text
dados/dataset_lag_publico.csv
modelos/melhor_modelo_lag.pkl
resultados/metricas_modelos.csv
resultados/comparacao_modelos_f1.png
resultados/matriz_confusao_melhor_modelo.png
resultados/importancia_variaveis.png
```

---

### Teste 11 — Verificar métricas dos modelos

```bash
cat resultados/metricas_modelos.csv
```

Resultado obtido:

```text
modelo,acuracia,precisao_macro,recall_macro,f1_macro,tempo_inferencia_ms
Random Forest,0.9601,0.9198,0.8858,0.9006,0.0753
Decision Tree,0.9534,0.8976,0.8659,0.8797,0.0043
KNN,0.8970,0.8184,0.7276,0.7651,0.0243
Logistic Regression,0.7906,0.6439,0.7057,0.6672,0.0105
```

Esse teste demonstra a comparação quantitativa entre os algoritmos.

---

## Resultados obtidos

| Modelo              | Acurácia | Precisão Macro | Recall Macro | F1-Score Macro | Tempo de Inferência |
| ------------------- | -------: | -------------: | -----------: | -------------: | ------------------: |
| Random Forest       |   96,01% |         91,98% |       88,58% |         90,06% |            0,075 ms |
| Decision Tree       |   95,35% |         89,77% |       86,60% |         87,97% |            0,004 ms |
| KNN                 |   89,70% |         81,84% |       72,77% |         76,51% |            0,024 ms |
| Logistic Regression |   79,07% |         64,40% |       70,57% |         66,73% |            0,010 ms |

O melhor modelo foi o **Random Forest**, apresentando maior acurácia e maior F1-score.

## Análise da importância das variáveis

Após o treinamento do modelo Random Forest, foi realizada uma análise de importância das variáveis para identificar quais métricas de rede tiveram maior influência na classificação dos estados de QoS.

### Resultados obtidos

| Variável    | Importância |
| ----------- | ----------: |
| Congestion  |      26,78% |
| Jitter      |      23,21% |
| Packet Loss |      21,35% |
| Throughput  |      17,11% |
| Latency     |      11,54% |

### Interpretação dos resultados

O congestionamento foi a variável mais relevante para o modelo, representando aproximadamente 26,78% da importância total. Esse resultado indica que a saturação da rede exerce forte influência sobre a qualidade do serviço, impactando diretamente a experiência dos usuários.

O jitter apareceu como a segunda variável mais importante (23,21%). Isso demonstra que a variação do atraso entre pacotes possui grande impacto em aplicações sensíveis a tempo real, como jogos online, chamadas VoIP e videoconferências.

A perda de pacotes (Packet Loss) apresentou importância de 21,35%, evidenciando que falhas na entrega dos pacotes também são determinantes para a degradação da qualidade da conexão.

O throughput apresentou importância intermediária (17,11%), contribuindo para a classificação dos estados da rede, porém com menor influência do que congestionamento, jitter e perda de pacotes.

A latência apresentou a menor importância relativa (11,54%). Embora seja uma métrica tradicionalmente associada à qualidade da conexão, os resultados sugerem que parte de sua influência já está representada por métricas correlacionadas, como congestionamento, jitter e perda de pacotes.

### Conclusão da análise

Os resultados demonstram que a utilização conjunta de múltiplas métricas de rede fornece uma representação mais completa do comportamento da QoS. O modelo identificou que congestionamento, jitter e perda de pacotes são os principais fatores para distinguir entre estados normais, moderados e severos de degradação da rede.

A análise de importância das variáveis também contribui para a interpretabilidade do modelo, permitindo compreender quais métricas possuem maior impacto na tomada de decisão do algoritmo.


## Discussão dos resultados

Os resultados demonstram que algoritmos de Machine Learning conseguem classificar estados de degradação de QoS com boa precisão.

O modelo Random Forest obteve o melhor desempenho geral, alcançando acurácia de aproximadamente **96%** e F1-score macro de aproximadamente **90%**. Isso indica que o modelo conseguiu identificar padrões entre métricas de rede e estados de qualidade da conexão.

A Decision Tree apresentou desempenho próximo ao Random Forest, porém com menor robustez. O KNN apresentou desempenho intermediário, enquanto a Logistic Regression obteve o pior resultado, indicando que o problema não possui separação linear simples.

O tempo de inferência de todos os modelos foi muito baixo, indicando viabilidade para aplicações em tempo quase real.

## Conclusão

O projeto demonstrou que é possível utilizar métricas de rede e algoritmos de Machine Learning para prever estados de degradação de QoS em redes de computadores.

A solução implementada permite:

* Preparar e rotular dados de rede;
* Gerar gráficos de análise;
* Treinar diferentes modelos;
* Comparar desempenho dos algoritmos;
* Salvar o melhor modelo;
* Realizar predições manuais;
* Avaliar a importância das variáveis;
* Reproduzir todos os experimentos automaticamente.

O Random Forest apresentou o melhor desempenho, demonstrando ser uma alternativa viável para classificação de eventos de alta latência e degradação de qualidade em redes.
