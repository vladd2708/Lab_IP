total = float(input("Total de la cuenta:"))
propina = float(input("Propina:"))
personas = int(input("Numero de personas:"))
propina = total*propina/100
total_final = total+propina
total_por_persona = total_final/personas

print("Total a pagar por persona: ", total_por_persona)
print("Total de la cuenta: ", total_final)
print("Total pago por persona: ", total_por_persona)
#prueba