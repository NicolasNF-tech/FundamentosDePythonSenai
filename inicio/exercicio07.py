#7. Receba nome, cargo e salário e acrescente 10%

#entrada

nome=input("digite seu nome: ")
cargo=input("Digite seu cargo: ")
Salario=float(input("Digite seu salário: "))
porcentagem=int(input("digite a porcentagem de aumento salarial: "))
#processamento

SalarioComAcressimo= Salario + Salario/100*porcentagem

#Saida

print(f"{nome} o salario de {cargo}, anteriormente {Salario}, recebeu um acressimo de {porcentagem}%  e agora passou a ser {SalarioComAcressimo}")