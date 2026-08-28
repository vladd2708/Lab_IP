numero = 456

if numero == 0:
    print("0")

hexadecimal = ""

while numero > 0:
    residuo = numero % 16

    if residuo == 10:
        residuo = "A"
    elif residuo == 11:
        residuo = "B"
    elif residuo == 12:
        residuo = "C"
    elif residuo == 13:
        residuo = "D"
    elif residuo == 14:
        residuo = "E"
    elif residuo == 15:
        residuo = "F"

    hexadecimal = str(residuo) + hexadecimal
    numero = numero // 16

print(hexadecimal)