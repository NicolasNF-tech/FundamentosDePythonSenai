idade=int(input("Qual é a sua idade? "))
ingresso=input("voce tem ingresso? (sim ou não): ").lower()


if not(idade < 18 and ingresso == "não") :
    print("seja bem vindo a festa")
else:
    print("voce não pode entrar na festa")