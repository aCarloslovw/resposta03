import json

# Função para calcular os dados
def calcular_faturamento(arquivo):
    with open(arquivo) as f:
        dados = json.load(f)
    
    faturamentos = dados["faturamento"]
    
    # Filtrar valores de faturamento que não sejam zero
    valores = [d['valor'] for d in faturamentos if d['valor'] > 0]
    
    if not valores:
        return "Não há faturamento para calcular."
    
    # Cálculo do menor e maior faturamento
    menor_faturamento = min(valores)
    maior_faturamento = max(valores)
    
    # Cálculo da média mensal
    media_faturamento = sum(valores) / len(valores)
    
    # Contar dias com faturamento acima da média
    dias_acima_media = sum(1 for valor in valores if valor > media_faturamento)
    
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "media_faturamento": media_faturamento,
        "dias_acima_media": dias_acima_media
    }

# Chamar a função e imprimir os resultados
resultado = calcular_faturamento('faturamento.json')

# Impressão formatada
if isinstance(resultado, str):
    print(resultado)
else:
    print("Resultados do Faturamento Mensal:")
    print(f"Menor Faturamento: R$ {resultado['menor_faturamento']:.2f}")
    print(f"Maior Faturamento: R$ {resultado['maior_faturamento']:.2f}")
    print(f"Média Mensal: R$ {resultado['media_faturamento']:.2f}")
    print(f"Número de dias com faturamento acima da média: {resultado['dias_acima_media']}")
