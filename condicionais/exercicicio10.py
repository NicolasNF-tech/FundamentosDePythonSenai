print()
print()
print("|**********************************************|")
print("|      Calculadora de Preços e Acressimos      |")
print("|                  Versão 1.0                  |")
print("|**********************************************|")
print("|**********************************************|")
print()
print()
preco=int(input("digite o preço pago no produto: "))
print()
lucro=int(input("digite a porcentagem de lucro: "))
print()
precofin=preco+ ((preco/100)*lucro)
print()
if lucro<50:
    alerta=input("*ALERTA* essa margem de lucro é muito baixa, deseja continuar? ").lower()
    print()
    if alerta== "sim":
        print(f"o preço final, com a margem de lucro de {lucro}% será de {precofin}")
    for alerta in ["não"]:
        print("Digite um percentual acima de 50%") 


else:
    print(f"o preço final, com a margem de lucro de {lucro}% será de {precofin}")