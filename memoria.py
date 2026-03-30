import random
import time
import os


temp = "🦣🦣🐪🐪🐯🐯🦓🦓🐢🐢🐋🐋🦜🦜🐧🐧"
figuras = list(temp)

jogo = []
apostas = []

def preenche_matriz():
    embaralhadas = figuras[:]  # cópia para não destruir a lista original
    random.shuffle(embaralhadas)
    for i in range(4):
        jogo.append([])
        apostas.append([])
        for j in range(4):
            jogo[i].append(embaralhadas[i * 4 + j])
            apostas[i].append("♦️")

preenche_matriz()

def mostra_tabuleiro():
    print("   1   2   3   4")
    for i in range(4):
        print(i + 1, end="")
        for j in range(4):
            print(f" {jogo[i][j]} ", end="")
        print("\n")
    print("Memorize a posição dos bichos no tabuleiro...")
    time.sleep(2)

    print("Contagem Regressiva: ", end="")
    for i in range(10, 0, -1):
        print(i, end=" ", flush=True)
        time.sleep(1)

mostra_tabuleiro()

def mostra_apostas():
    print("   1   2   3   4")
    for i in range(4):
        print(i + 1, end="")
        for j in range(4):
            print(f" {apostas[i][j]} ", end="")
        print("\n")

def faz_aposta(num):
    while True:
        mostra_apostas()
        posicao = input(f"{num}ª Coordenada (linha e coluna, ex: 12): ")
        if len(posicao) != 2 or not posicao.isdigit():
            print("Informe uma dezena válida (ex: 12, 23, 31...)")
            time.sleep(2)
            continue
        x = int(posicao[0]) - 1
        y = int(posicao[1]) - 1
        if not (0 <= x <= 3 and 0 <= y <= 3):
            print("Coordenada inválida, use valores entre 1 e 4")
            time.sleep(2)
            continue
        if apostas[x][y] != "♦️":
            print("Coordenada já revelada. Tente outra")
            time.sleep(2)
            continue
        apostas[x][y] = jogo[x][y]
        return x, y

############################################################################
acertos = 0
tentativas = 0

while acertos < 8:
    x1, y1 = faz_aposta(1)
    x2, y2 = faz_aposta(2)
    tentativas += 1

    mostra_apostas()

    if jogo[x1][y1] == jogo[x2][y2]:
        print("✅ Par encontrado!")
        acertos += 1
    else:
        print("❌ Não formam um par. As cartas serão escondidas novamente.")
        apostas[x1][y1] = "♦️"
        apostas[x2][y2] = "♦️"

    time.sleep(2)

mostra_apostas()