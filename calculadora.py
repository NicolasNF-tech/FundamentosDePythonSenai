#entrada
n1=float(input("qual o primeiro numero deseja realizar uma operacao: "))
n2=float(input("qual o segundo numero deseja realizar uma operacao: "))
operacao=input("qual operacao deseja realizar (+,-,*,/,^): ")
#processamento
divisao=n1/n2
soma=n1+n2
subtracao=n1-n2
multiplicacao=n1*n2
potenciacao=n1**n2
#saida
if(operacao=="/"):
    print(f"{n1} / {n2} = {divisao}")
elif(operacao=="*"):
    print(f"{n1} * {n2} = {multiplicacao}")
elif(operacao=="+"):
    print(f"{n1} + {n2} = {soma}")
elif(operacao=="-"):
    print(f"{n1} - {n2} = {subtracao}")
elif(operacao=="^"):
    print(f"{n1} ^{n2} = {potenciacao}")
else:
    print("operacao invalida") 