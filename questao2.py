def check_letter_a(string):
    # Converte a string para minúsculas e conta quantas vezes 'a' aparece
    count = string.lower().count('a')
    
    # Verifica se a letra 'a' está presente e retorna a quantidade
    if count > 0:
        return f"A letra 'a' aparece {count} vezes na string."
    else:
        return "A letra 'a' não está presente na string."

# Exemplo de string informada no código
string = "Target"
print(check_letter_a(string))