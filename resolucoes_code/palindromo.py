def eh_palindromo(palavra: str) -> bool:
    """
    Pede uma string como parâmetro e retorna um valor booleano afirmando se ela é ou não um palíndromo.
    """
    return palavra == palavra[::-1]


def validar_palavra(mensagem: str) -> str:
    """
    Garante que seja informado uma palavra, e não uma frase
    """
    while True:
        palavra = input(mensagem).strip()
        partes = palavra.split()

        if len(partes) == 1:
            return palavra
        else:
            print("Informe uma palavra, e não uma frase")


def main() -> None:
    palavra = validar_palavra("Informe uma palavra: ")
    resultado = eh_palindromo(palavra)
    if resultado == True:
        print(f"A palavra '{palavra}' é palíndromo")
    else:
        print(f"A palavra ´{palavra}´ não é palíndromo")


if __name__ == "__main__":
    main()