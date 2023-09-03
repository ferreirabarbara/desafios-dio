nomeHeroi = input("Insira o nome do Herói aqui: ")
xpHeroi = input("Insira o total de XP do herói: ")
mensagemHeroi = f"O Herói de nome {nomeHeroi} está no nível de "

if int(xpHeroi) < 1000:
    nivelHeroi = "Ferro"
    print(mensagemHeroi + nivelHeroi)
elif 1000 < int(xpHeroi) < 2001:
    nivelHeroi = "Bronze"
    print(mensagemHeroi + nivelHeroi)
elif 2000 < int(xpHeroi) < 5001:
    nivelHeroi = "Prata"
    print(mensagemHeroi + nivelHeroi)
elif 6000 < int(xpHeroi) < 7001:
    nivelHeroi = "Ouro"
    print(mensagemHeroi + nivelHeroi)
elif 7000 < int(xpHeroi) < 8001:
    nivelHeroi = "Platina"
    print(mensagemHeroi + nivelHeroi)
elif 8000 < int(xpHeroi) < 9001:
    nivelHeroi = "Ascendente"
    print(mensagemHeroi + nivelHeroi)
elif 9000 < int(xpHeroi) < 10001:
    nivelHeroi = "Imortal"
    print(mensagemHeroi + nivelHeroi)
elif 10000 < int(xpHeroi): 
    nivelHeroi = "Radiante"
    print(mensagemHeroi + nivelHeroi) 