n=int(input("digite um numero entre 0 e 9999: "))

c4=n//1000
r4=n%1000
c3=r4//100
r3=r4%100
c2=r3//10
r2=r3%10
c1=r2
if(10000>n or n>9999):
    print()
    print("numero invalido")
    print()
else:
    print(f"{c1}{c2}{c3}{c4}")