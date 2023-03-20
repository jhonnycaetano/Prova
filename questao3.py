faturamento_diario = [1500, 2000, 1800, 2200, 1900, 1700, 2100, 2300, 2400, 2000, 1700, 1900, 2200, 2100, 1900, 2000, 1800, 2100, 2300, 2200, 1900, 2000, 2100, 2400, 2200, 2000, 2100, 2200, 2000, 2300, 2200]

#Menor valor de faturamento diário.ArithmeticError().
menor_faturamento = min(faturamento_diario)
print("Menor valor de faturamento diário:", menor_faturamento)

#Maior valor de faturamento diário.
maior_faturamento = max(faturamento_diario)
print("Maior valor de faturamento diário:", maior_faturamento)

#Média mensal de faturamento diário.
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

#Número de dias com faturamento diário superior à média mensal.
dias_acima_media = sum(1 for faturamento in faturamento_diario if faturamento > media_mensal)
print("Número de dias com faturamento diário superior à média mensal:", dias_acima_media)
