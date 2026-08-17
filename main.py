"""Caça ao Tesouro — jogo simples de terminal.

Execute com: python main.py
"""

import random


def pedir_palpite(limite):
    """Lê um número válido ou encerra o jogo quando o jogador digita 'sair'."""
    while True:
        entrada = input(f"Escolha um número de 1 a {limite} (ou 'sair'): ").strip().lower()
        if entrada == "sair":
            return None
        try:
            numero = int(entrada)
            if 1 <= numero <= limite:
                return numero
        except ValueError:
            pass
        print(f"Digite um número inteiro entre 1 e {limite}.")


def jogar():
    limite = 20
    tentativas = 5
    segredo = random.randint(1, limite)

    print("\n=== CAÇA AO TESOURO ===")
    print(f"O tesouro está escondido em uma casa de 1 a {limite}.")

    for rodada in range(1, tentativas + 1):
        print(f"\nTentativa {rodada} de {tentativas}")
        palpite = pedir_palpite(limite)

        if palpite is None:
            print(f"Jogo encerrado. O tesouro estava na casa {segredo}.")
            return
        if palpite == segredo:
            pontos = (tentativas - rodada + 1) * 100
            print(f"Você encontrou o tesouro! Pontuação: {pontos} pontos.")
            return
        if palpite < segredo:
            print("Pista: o tesouro está em uma casa maior.")
        else:
            print("Pista: o tesouro está em uma casa menor.")

    print(f"\nFim de jogo. O tesouro estava na casa {segredo}.")


def main():
    while True:
        jogar()
        novamente = input("\nJogar novamente? (s/n): ").strip().lower()
        if novamente != "s":
            print("Até a próxima!")
            break


if __name__ == "__main__":
    main()