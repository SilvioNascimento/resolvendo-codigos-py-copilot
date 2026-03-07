def validar_valor_inteiro(mensagem: str) -> int:
    """
    Solicita ao usuário um número inteiro válido.
    """
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: Deve digitar apenas um valor inteiro.")


def validar_valor_flutuante(mensagem: str) -> float:
    """
    Solicita ao usuário um número decimal válido.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Deve digitar apenas um valor flutuante.")


def validar_nota(mensagem: str) -> float:
    """
    Solicita ao usuário uma nota válida.
    """
    while True:
        nota = validar_valor_flutuante(mensagem)
        if 0 <= nota <= 10:
            return nota
        else:
            print("Nota inválida. Informe uma nota aceitável.")


def calcular_media(lista_numeros: list[float]) -> float:
    """
    Calcula a média aritmética de uma lista de notas.
    """
    return sum(lista_numeros)/len(lista_numeros)


def registrar_notas(qtd_valores: int) -> list[float]:
    """
    Coleta uma quantidade específica de notas do usuário.
    """
    # 1ª forma:
    # lista_notas = []

    # for i in range(qtd_valores):
    #     nota = validar_nota(f"Informe a {i+1}ª nota: ")
    #     lista_notas.append(nota)

    # return lista_notas

    # 2ª forma
    return [
        validar_nota(f"Informe a {i+1}ª nota: ")
        for i in range(qtd_valores)
    ]


def ler_quantidade_notas() -> int:
    """
    Garante que o usuário informe pelo menos 2 notas.
    """
    while True:
            qtd_notas = validar_valor_inteiro("Quantas notas deseja registrar? ")

            if qtd_notas > 1:
                return qtd_notas

            print("Erro: a quantidade de notas deve ser maior que 1.")


def main() -> None:
    """
    Função principal do programa.
    """
    qtd_notas = ler_quantidade_notas()
    lista_notas = registrar_notas(qtd_notas)
    media = calcular_media(lista_notas)
    print(f"Média: {media:.2f}")

if __name__ == "__main__":
    main()