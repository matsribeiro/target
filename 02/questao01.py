# Programa que realiza a soma do código informado
def calcular_soma():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K

    return SOMA

# Exibindo o resultado
print(calcular_soma())