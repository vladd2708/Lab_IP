edad = 19
tiene_credencial = True
tiene_adeudo = True

if edad >= 18:
    es_mayor_de_edad = True

documento_valido = tiene_credencial
sin_adeudo = not tiene_adeudo
autorizado = es_mayor_de_edad or documento_valido or sin_adeudo

print("Autorizado")
#prueba