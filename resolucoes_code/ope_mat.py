# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def soma(valor1:float, valor2:float) -> float:
    return valor1 + valor2


def subtracao(valor1:float, valor2:float) -> float:
    return valor1 - valor2


def multiplicacao(valor1:float, valor2:float) -> float:
    return valor1 * valor2


def divisao(valor1:float, valor2:float) -> float:
    return valor1 / valor2


def exibir_valor_str(valor:float) -> str:
    if valor.is_integer():
        valor_inteiro = int(valor)
        return str(valor_inteiro)
    else:
        return str(valor)


def validar_valor(mensagem:str) -> float:
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Deve digitar apenas números.")


operadores = ['+', '-', '*', '/']

num1 = validar_valor("Informe um valor: \t")

while True:
    operador = str(input("Informe um operador (+, -, *, /). Para encerrar, digite 0: \t"))

    if operador == '0':
        print("Encerrando o programa...")
        break

    if operador not in operadores:
        print("Erro: Informe um dos operadores aceitáveis (+, -, *, /)")
        continue

    num2 = validar_valor("Informe outro valor: \t")

    if operador == '+':
        resultado = soma(num1, num2)
    elif operador == '-':
        resultado = subtracao(num1, num2)
    elif operador == '*':
        resultado = multiplicacao(num1, num2)
    elif operador == '/':
        try:
            resultado = divisao(num1, num2)
        except ZeroDivisionError:
            print("ERRO: Não é possível dividir um valor por zero!")
            print("Encerrando o programa devido a gravidade do erro...")
            break

    print(f'Resultado = \t{exibir_valor_str(resultado)}')
    num1 = resultado