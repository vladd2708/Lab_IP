n=int(input("ingrese un numero:"))
i=2
primo=True
while i<n:
    if n%i==0:
        primo=False
    i=i+1
if primo:
    print("es un numero primo")
else:
    print("no es un numero primo")