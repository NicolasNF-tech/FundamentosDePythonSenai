n1=int(input("qual o numero a sequencia vai iniciar"))
n2=int(input("qual o numero a sequencia vai terminar"))
intervalo=int(input("intervalo da sequencia: "))
for x in range(n1, n2+1, intervalo):
    print(f"x vale:{x}")