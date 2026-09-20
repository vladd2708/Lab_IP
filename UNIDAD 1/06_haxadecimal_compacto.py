numero = 456                        #aqui estamos indicando el numero.
hexadecimal=""                      #aqui estamos dando la señal de lo que tiene que aparecer como hexadecimal.
digitos="0123456789ABCDEF"          #aqui estamos indicando los caracteres que se van a utilizar en el programa.
while numero > 0:                   #aqui estamos realizando la conversion a hexadecimal.
    hexadecimal = digitos[numero%16]+hexadecimal
    numero=numero//16
print(hexadecimal or "0")            #aqui estamos indicando el resultado en hexadecimal.