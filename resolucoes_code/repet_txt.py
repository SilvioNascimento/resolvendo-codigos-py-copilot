# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

string = str(input("Digite uma string: "))

try:
    valor = int(input("Digite um valor: "))
    print((string + ' ') * valor)

except ValueError:
    print('Erro: Digite apenas um valor inteiro')
