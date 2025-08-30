
import matplotlib.pyplot as plt

variaveis = [
    ('a',     "Evolução do semi-eixo maior (a)\npara N = {n}",                     "Semi-eixo maior (a)"),
    ('e',     "Variação da excentricidade orbital (e)\ncom o tempo para N = {n}",  "Excentricidade (e)"),
    ('i',     "Mudança da inclinação orbital (i)\nao longo do tempo para N = {n}", "Inclinação (i)"),
    ('nodo',  "Longitude do nó ascendente (Ω)\ncom o tempo para N = {n}",          "Longitude do Nó (nodo)"),
    ('argper',"Evolução do argumento do periélio (ω)\ncom o tempo para N = {n}",   "Argumento do Periélio"),
    ('anomed',"Comportamento da anomalia média (M)\ncom o tempo para N = {n}",     "Anomalia Média (anomed)")
]

def criar_grafico(x, y, titulo, ylabel):
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(x, y, color='#1A2A80', linestyle='-', linewidth=1.5)
    ax.set_title(titulo)
    ax.set_xlabel("Tempo (t)")
    ax.set_ylabel(ylabel)
    ax.set_xticks(list(range(0, 21)))
    fig.tight_layout()
    plt.close()
    return fig


def gerar_grafico_comparativo(x1, y1, x2, y2, titulo, ylabel, label1, label2):
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot(x1, y1, color='#1A2A80', linestyle='-', label=f'N = {label1}')
    ax.plot(x2, y2, color="#E60F0F", linestyle='-', label=f'N = {label2}')
    ax.set_title(titulo)
    ax.set_xlabel("Tempo (t)")
    ax.set_ylabel(ylabel)
    ax.set_xticks(list(range(0, 21)))
    ax.legend()
    fig.tight_layout()
    plt.close()
    return fig

