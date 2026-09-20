numero, octal=16,""                        #aqui estamos indicando el numero.
if numero==0: print("0")                  #aqui estmaos dando la señal de lo que tiene que aparecer como octal.
while numero>0:octal, numero=str(numero%8)+octal, numero//8              #aqui estamos realizando la conversión a octal.
print(octal)                              #aqui estamos imprimiendo el resultado de la conversion a octal.