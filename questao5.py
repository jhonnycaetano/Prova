#String de entrada.
string = 'Exemplo de string para ser invertida'

#Inverter a string.
string_invertida = ''
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

#Imprimir a string invertida.
print(string_invertida)
