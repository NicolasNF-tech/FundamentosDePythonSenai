print()
print()
print("|**********************************************|")
print("|          Programa Reajuste Salarial          |")
print("|                  Versão 1.0                  |")
print("|**********************************************|")
print("|**********************************************|")
print()
print()
#entrada
salario=float(input("digite seu salario:"))
#processamento
salarioaj= salario*1.3
#saida
if salario <=500:
    print(f"seu salario de R${salario} recebeu um reajuste de 30% e passou a ser {salarioaj}")
else:
    print("você não tem direio a reajuste")