print()
print()
print()
print()
print("|**********************************************|")
print("|        Calculadora de Medias escolares       |")
print("|                     8.000                    |")
print("|**********************************************|")
print("|**********************************************|")
print()
print()

n1=float(input("digite sua nota do seu primeiro trimestre: "))
print()
n2=float(input("digite a sua nota do segundo trimestre: "))
print()
p1=int(input("digite o peso do prieiro trimestre: "))
print()
p2=int(input("digite o peso do segundo trimestre: "))
print()
p3=int(input("digite o peso do terceiro trimestre: "))
print()
mf=int(input("qual a media necessaria para passar em sua escola? "))
print()
q=input("o terceiro trimestre ja foi concluido?") .lower()
print()

m1=n1*p1
m2=n2*p2
mn=(mf*(p1+p2+p3)- (m1 + m2))/p3
if q=="sim":
    n3=float(input("digite sua nota do terceiro trimestre: "))
    m3=n3*p3
    if (m1+m2+m3)/(p1+p2+p3) >= mf:
        print("parabéns, você passou de ano 👏👏👏")
    else:
        print("repetiu😂😂😂")

if q=="não":
    if mn < 0:
        print("parabens voce ja passou de ano")
    else:
        print(f"voce precisa de {mn} pontos para passar")
print()