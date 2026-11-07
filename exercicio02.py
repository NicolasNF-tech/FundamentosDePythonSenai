#2. Receba ano de nascimento e ano atual. Calcule idade e semanas.
 #entrada
anoDeNascimento= int(input("digite o seu ano de nascimento: "))
anoAtual= int(input("digite o ano atual: "))
#processamento
idade = anoAtual - anoDeNascimento
idadeEmSemanas = 4 * 12 * idade
#saida
if(idade<0):
    print()
    print("você digitou os dados erraos pois nâo é possivel ter nascido após o ano atual")
if(idade>0):
    print()
    print(f"Sua idade em anos é {idade} anos")
    print()
    print(f"sua idade em semanas é {idadeEmSemanas} semanas")

