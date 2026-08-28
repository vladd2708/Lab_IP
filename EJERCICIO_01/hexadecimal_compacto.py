numero = 456
hexadecimal=""
digitos="0123456789ABCDEF" 
while numero > 0:
    hexadecimal = digitos[numero%16]+hexadecimal
    numero=numero//16
print(hexadecimal or "0")