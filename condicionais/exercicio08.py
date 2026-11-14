nome=input("digite seu nome: ")
cargo=input("digite seu cargo: ")
salario=float(input("qual o seu salário"))


salarioacr=salario*1.1
if salario <1000:
    print(f"{nome}, o salario de seu cargo de {cargo} anteriormente de {salario:.2f} recebeu um acrecimo de 10% e agora será {salarioacr:.2f}  ")
else:
    print(f"{nome},o salario do seu cargo de{cargo} se manterá o mesmo")
