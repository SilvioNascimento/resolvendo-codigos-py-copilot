def soma(a: float, b: float) -> float:
    return a + b

def subtracao(a: float, b: float) -> float:
    return a - b

def multiplicacao(a: float, b: float) -> float:
    return a * b

def divisao(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b

def formatar(valor: float) -> str:
    return str(int(valor)) if valor.is_integer() else str(valor)

def validar_valor(mensagem:str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Deve digitar apenas números.")


operacoes = {
    '+': soma,
    '-': subtracao,
    '*': multiplicacao,
    '/': divisao
}

num1 = validar_valor("Informe um valor: \t")

while True:
    operador = input("Informe um operador (+, -, *, /). Para encerrar, digite 0: \t")

    if operador == '0':
        print("Encerrando o programa...")
        break

    if operador not in operacoes:
        print("Operador inválido.")
        continue

    try:
        num2 = validar_valor("Informe outro valor: \t")
        resultado = operacoes[operador](num1, num2)
    except ValueError:
        print("Erro: valor inválido.")
        continue
    except ZeroDivisionError as erro:
        print(f"Erro: {erro}")
        break

    print(f"Resultado = \t{formatar(resultado)}")
    num1 = resultado