numero, octal=16,""
if numero==0: print("0")
while numero>0:octal, numero=str(numero%8)+octal, numero//8
print(octal)