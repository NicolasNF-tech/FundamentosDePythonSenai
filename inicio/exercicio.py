
#1. Recaba a idade em anos e imprima em meses, dias, horas e meses

idade= int(input("digite a idade: ")) #pega o texto e convertee para número

# processamento
idadeEmMeses=idade * 12
idadeEmDias=idade * 365
idadeEmHoras=idadeEmDias * 24
idadeEmMinutos=idadeEmHoras * 60
idadeEmSegundos=idadeEmMinutos * 60
Nascimento=2026 - idade
#saída
if idade>117:
    print("parabéns você é a pessoa mais velha do mundo")
print(f"Sua idade em Meses é {idadeEmMeses} meses 👍")
print()
print(f"Sua idade em dias é {idadeEmDias} dias")
print()
print(f"Sua idade em horas é {idadeEmHoras} horas")
print()
print(f"Sua idade em minutos é {idadeEmMinutos} minutos")
print()
print(f"Sua idade em segundos é {idadeEmSegundos} segundos")
print(f"você nasceu em {Nascimento}")