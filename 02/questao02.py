def fibonacci_sequence(limit):
    # Função para gerar a sequência de Fibonacci até o limite informado
    fib_sequence = [0, 1]
    while fib_sequence[-1] < limit:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

def check_fibonacci(number):
    # Gera a sequência de Fibonacci até o número informado
    fib_sequence = fibonacci_sequence(number)
    
    # Verifica se o número está na sequência
    if number in fib_sequence:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} não pertence à sequência de Fibonacci."

# Exemplo de uso
number = 13
print(check_fibonacci(number))