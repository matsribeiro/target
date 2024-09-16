import json
import os

def calcular_faturamento(arquivo_json):
    # Verifique se o arquivo JSON existe
    if not os.path.isfile(arquivo_json):
        raise FileNotFoundError(f"O arquivo {arquivo_json} não foi encontrado.")

    # Leitura e processamento do arquivo JSON
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)

    # Verifique a estrutura do JSON lido
    if not isinstance(dados, list) or not all(isinstance(item, dict) and 'valor' in item for item in dados):
        raise ValueError("O arquivo JSON não está no formato esperado. Deve ser uma lista de dicionários com a chave 'valor'.")

    # Filtra apenas os valores de faturamento, ignorando os dias sem faturamento
    faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]
    
    if not faturamento:
        return None, None, 0
    
    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)
    media_mensal = sum(faturamento) / len(faturamento)
    
    dias_acima_da_media = sum(1 for dia in dados if dia['valor'] > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Caminho para o arquivo JSON
arquivo_json = 'C:/Users/Admin/Documents/target/02/dados.json'

# Chamada da função e exibição dos resultados
try:
    menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_faturamento(arquivo_json)
    print(f"Menor valor de faturamento ocorrido em um dia do mês: R$ {menor_faturamento:.2f}")
    print(f"Maior valor de faturamento ocorrido em um dia do mês: R$ {maior_faturamento:.2f}")
    print(f"Número de dias com faturamento diário superior à média mensal: {dias_acima_da_media}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
