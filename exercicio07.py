#7. Receba nome, cargo e salário e acrescente 10%

#entrada

nome=input("digite seu nome: ")
cargo=input("Digite seu cargo: ")
Salario=float(input("Digite seu salário: "))

#processamento

SalarioComAcressimo= Salario + (Salario/10)

#Saida

print(f"{nome} o salario de {cargo}, anteriormente {Salario}, recebeu um acressimo de 10%  e agora passou a ser {SalarioComAcressimo}")