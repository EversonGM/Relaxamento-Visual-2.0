import random
import os
import sys
import time
from getpass import getpass

# --- Configurações ---
new_var = "programacao", "python", "computador", "chave", "internet",
    "desenvolvedor", "algoritmo", "teclado", "monitor", "script",
    "seguranca", "rede", "sistema", "arquivo", "variavel", "desafio",
    "futebol", "amistade", "conhecimento", "rotina"
PALAVRAS = [
    new_var
]

FORCAS = [
    [
        "  _______     ",
        " |/      |    ",
        " |            ",
        " |            ",
        " |            ",
        " |            ",
        " |            ",
        "_|___         "
    ],
    [
        "  _______     ",
        " |/      |    ",
        " |      (_ )  ",
        " |            ",
        " |            ",
        " |            ",
        " |            ",
        "_|___         "
    ],
    [
        "  _______     ",
        " |/      |    ",
        " |      (_ )  ",
        " |       |    ",
        " |       |    ",
        " |            ",
        " |            ",
        "_|___         "
    ],
    [
        "  _______     ",
        " |/      |    ",
        " |      (_ )  ",
        " |      \\|    ",
        " |       |    ",
        " |            ",
        " |            ",
        "_|___         "
    ],
    [
        "  _______     ",
        " |/      |    ",
        " |      (_ )  ",
        " |      \\|/   ",
        " |       |    ",
        " |            ",
        " |            ",
        "_|___         "
    ],
    [
        "  _______     ",
        " |/      |    ",
        " |      (_ )  ",
        " |      \\|/   ",
        " |       |    ",
        " |      /     ",
        " |            ",
        "_|___         "
    ],
    [
        "  _______     ",
        " |/      |    ",
        " |      (_ )  ",
        " |      \\|/   ",
        " |       |    ",
        " |      / \\  ",
        " |            ",
        "_|___         "
    ]
]


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def escolher_palavra(dificuldade):
    if dificuldade == "1":
        filtradas = [p for p in PALAVRAS if len(p) <= 7]
    elif dificuldade == "2":
        filtradas = PALAVRAS[:]
    else:
        filtradas = [p for p in PALAVRAS if len(p) >= 8]
    if not filtradas:
        filtradas = PALAVRAS[:]
    return random.choice(filtradas).upper()


def desenhar_layout(palavra, letras_descobertas, usadas, erros, max_erros, dificuldade):
    # Preparar bordas e painel lateral
    largura_total = 70
    painel = []
    # Forca
    forca = FORCAS[erros]
    # Palavra oculta
    palavra_exibida = " ".join(letras_descobertas)
    usadas_exibidas = ", ".join(sorted(usadas)) if usadas else "(nenhuma)"
    status = [
        f"Dificuldade: { {'1':'Fácil','2':'Médio','3':'Difícil'}.get(dificuldade,'Médio') }",
        f"Erros: {erros}/{max_erros}",
        f"Letras usadas: {usadas_exibidas}",
        "",
        "Digite letra ou palavra",
        "Inteira para arriscar.",
    ]
    # Monta linhas com forca + painel
    linhas = []
    altura = max(len(forca), len(status) + 1)
    for i in range(altura):
        parte_forca = forca[i] if i < len(forca) else " " * 15
        if i == 0:
            indicador = "╔" + "═" * (largura_total - 2) + "╗"
        elif i == altura - 1:
            indicador = "╚" + "═" * (largura_total - 2) + "╝"
        else:
            # montar conteúdo central
            if i == 1:
                centro = f"  Palavra: {palavra_exibida}"
            elif i == 3:
                centro = ""
            else:
                centro = ""
            # preencher espaço
            conteudo = centro.ljust(40)
            painel_texto = status[i - 1] if 0 <= i - 1 < len(status) else ""
            linha = f"║ {parte_forca}  {conteudo}│ {painel_texto.ljust(20)} ║"
            linhas.append(linha)
            continue
        # borda superior/inferior
        linhas.append(indicador)

    # Imprime título e corpo
    print("┌" + "─" * (largura_total - 2) + "┐")
    print(f"│{' Jogo da Forca '.center(largura_total - 2)}│")
    print("├" + "─" * (largura_total - 2) + "┤")
    # Linhas custom: desenhar forca + painel manualmente para manter legibilidade
    # Vamos simplificar: mostrar forca à esquerda, infos à direita
    for i in range(len(forca)):
        parte_forca = forca[i]
        if i == 0:
            palavra_line = f"Palavra: {palavra_exibida}"
        elif i == 1:
            palavra_line = f"Dificuldade: { {'1':'Fácil','2':'Médio','3':'Difícil'}.get(dificuldade,'Médio') }"
        elif i == 2:
            palavra_line = f"Erros: {erros}/{max_erros}"
        elif i == 3:
            palavra_line = f"Letras usadas: {usadas_exibidas}"
        else:
            palavra_line = ""
        esquerda = parte_forca.ljust(17)
        direita = palavra_line.ljust(40)
        print(f"│ {esquerda} {direita} │")
    # Linha de separação
    print("├" + "─" * (largura_total - 2) + "┤")
    # Espaço para aviso final
    print(f"│ {' '.ljust(largura_total - 4)} │")
    print("└" + "─" * (largura_total - 2) + "┘")


def jogo():
    while True:
        limpar_tela()
        print("=== Jogo da Forca ===")
        print("1) Fácil  2) Médio  3) Difícil")
        dificuldade = input("Escolha a dificuldade (1/2/3): ").strip()
        if dificuldade not in {"1", "2", "3"}:
            dificuldade = "2"

        # opção de palavra personalizada
        print("\nDeseja inserir sua própria palavra secreta? (S/N)")
        usar_personalizada = input(">> ").strip().upper()

        if usar_personalizada == "S":
            while True:
                palavra = getpass("Digite a palavra secreta (só a outra pessoa deve ver): ").strip().upper()
                if palavra.isalpha():
                    break
                else:
                    print("A palavra precisa conter apenas letras. Tente novamente.")
        else:
            palavra = escolher_palavra(dificuldade).upper()

        letras_descobertas = ["_" for _ in palavra]
        tentativas_erradas = 0
        usadas = set()
        max_erros = len(FORCAS) - 1

        # loop principal
        while True:
            limpar_tela()
            desenhar_layout(palavra, letras_descobertas, usadas, tentativas_erradas, max_erros, dificuldade)

            if "_" not in letras_descobertas:
                print("\n🎉 Você ganhou! Palavra:", palavra)
                break
            if tentativas_erradas >= max_erros:
                print("\n💀 Você perdeu. A palavra era:", palavra)
                break

            chute = input("\nSeu chute: ").strip().upper()
            if not chute:
                continue

            if chute in usadas:
                print("Você já tentou isso. Tente outra coisa.")
                time.sleep(1.2)
                continue

            if len(chute) > 1:
                if chute == palavra:
                    letras_descobertas = list(palavra)
                    continue
                else:
                    tentativas_erradas += 1
                    usadas.add(chute)
                    print("Palavra incorreta.")
                    time.sleep(1.2)
                    continue

            if len(chute) == 1 and chute.isalpha():
                usadas.add(chute)
                if chute in palavra:
                    for idx, letra in enumerate(palavra):
                        if letra == chute:
                            letras_descobertas[idx] = chute
                    print("Boa! Letra correta.")
                else:
                    tentativas_erradas += 1
                    print("Letra não está na palavra.")
                time.sleep(1)
            else:
                print("Entrada inválida.")
                time.sleep(1)

        resp = input("\nQuer jogar de novo? (S/N): ").strip().upper()
        if not resp.startswith("S"):
            print("Obrigado por jogar. Até mais!")
            break


if __name__ == "__main__":
    try:
        jogo()
    except KeyboardInterrupt:
        print("\nSaindo do jogo...")
