numero = 9                                           #aqui estamos indicando el numero
binario = ""                                         #aqui estamos dando la señal de lo que tiene que aparecer como binario
while numero > 0: binario, numero = str(numero % 2) + binario, numero // 2   #aqui estamos realizando la conversión a binario
print(binario)