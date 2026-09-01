numero = 9
binario = ""
while numero > 0: binario, numero = str(numero % 2) + binario, numero // 2
print(binario)