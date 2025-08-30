# 🌌 Visualizador de Órbitas de Asteroides

Este projeto é uma aplicação interativa em Python desenvolvida com `CustomTkinter`, `matplotlib` e `pandas`, 
que permite visualizar e comparar parâmetros orbitais de asteroides ao longo do tempo a partir de dados fornecidos em arquivos `.sal`.

## 🚀 Funcionalidades

- Interface gráfica moderna com `CustomTkinter`.
- Leitura otimizada de arquivos `.sal` contendo parâmetros orbitais.
- Geração de **6 gráficos automáticos** com base nas variáveis orbitais:
  - Semi-eixo maior (a)
  - Excentricidade (e)
  - Inclinação (i)
  - Longitude do nó ascendente (Ω)
  - Argumento do periélio (ω)
  - Anomalia média (M)
- Comparação visual de dois objetos (valores distintos de `N`) no mesmo gráfico.
- Escalas personalizadas para cada variável.
- Suporte a grandes volumes de dados com Git LFS.

## 📁 Estrutura

```plaintext
├── app.py                  # Arquivo principal da aplicação
├── data/
│   └── orbitas.sal         # Arquivo de entrada com dados orbitais
├── README.md               # Este arquivo
├── requirements.txt        # Bibliotecas necessárias
└── assets/ (opcional)      # Imagens ou arquivos adicionais

