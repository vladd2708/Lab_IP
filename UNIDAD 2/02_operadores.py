operador=input("ingrese un operador(+,-,*,/):")
if operador=="+":
    o1=input("ingrese el primer numero:")
o2=input("ingrese el segundo numero:")
resultado=o1+operador+o2
resultado=eval(resultado)
print("el resultado de la suma es:",resultado)