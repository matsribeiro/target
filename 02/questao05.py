def inverter_string(s):
    # Converte a string em uma lista para manipulação
    lista = list(s)
    
    # Inicializa as variáveis para os índices
    inicio = 0
    fim = len(lista) - 1
    
    # Troca os caracteres das extremidades em direção ao centro
    while inicio < fim:
        lista[inicio], lista[fim] = lista[fim], lista[inicio]
        inicio += 1
        fim -= 1
    
    # Converte a lista de volta para uma string
    return ''.join(lista)

# Entrada de string pelo usuário
string_original = input("Digite a string a ser invertida: ")

# Inverter a string
string_invertida = inverter_string(string_original)

# Exibir o resultado
print("String invertida:", string_invertida)
