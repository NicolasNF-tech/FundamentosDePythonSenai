# Distribuição de cédulas: receba um valor inteiro em reais e determine a menor quantidade de cédulas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5, R$ 2 e moedas de R$ 1 necessárias para representar esse valor.
v=int(input("Digite a sua quantidade de dinheiro: "))

duz=v //200
restoduz=v % 200
cem=restoduz // 100
restoc=restoduz %100
cinq=restoc//50
restocinq=restoc%50
vin=restocinq//20
restovin=restocinq%20
dez=restovin//10
restodez=restovin%10
cinco=restodez//5
restocinco=restodez%5
dois=restocinco//2
restodois=restocinco%2
um=restodois//1
print("voce precisara de ")
if(duz>0):
    print(f"{duz} nota(s) de 200")
if (restoduz>0)and cem>0:
    print(f" {cem} nota(s) de 100 ")
if(restoc>0)and cinq>0:
    print(f"{cinq} nota(s) de 50")
if(restocinq>0)and vin>0:
    print(f"{vin} nota(s) de 20")
if(restovin>0)and dez>0:
    print(f"{dez} nota(s) de 10")
if(restodez>0)and cinco>0:
    print(f"{cinco} nota(s) de 5")
if(restocinco>0)and dois>0:
    print(f"{dois} nota(s) de 2")
if(restodois>0)and um>0:
    print(f"{um} nota(s) de 1")