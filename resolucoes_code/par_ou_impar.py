def par_ou_impar(valor:int) -> str:
    return "par" if valor % 2 == 0 else "ímpar"


def main() -> None:
    try:
        valor = int(input("Informe um valor inteiro: "))
        resultado = par_ou_impar(valor)
        print(f"O valor {valor} é {resultado}")

    except ValueError:
        print("Não foi possível converter para um valor inteiro")

if __name__ == "__main__":
    main()