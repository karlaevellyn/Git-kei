t1 = int(input("Adicione o tempo do nadador 1: "))

t2 = int(input("Adicione o tempo do nadador 2: "))

t3 = int(input("Adicione o tempo do nadador 3: "))

if t1 < t2 and t1 < t3:
    print("1 -> Medalha de ouro")
    if t2 < t3:
        print("2 -> Medalha de prata")
        print("3 -> Medalha de bronze")
    elif t3 < t2:
        print("3 -> Medalha de prata")
        print("2 -> Medalha de bronze")
elif t2 < t1 and t2 < t3:
    print("2 -> Medalha de Ouro")
    if t1 < t3:
        print("1 -> Medalha de prata")
        print("3 -> Medalha de bronze")
    elif t3 < t1:
        print("3")
        print("1")
elif t3 < t1 and t3 < t2:
    print("3 -> Medalha de ouro")
    if t2 < t1:
        print("2 -> Medalha de prata")
        print("1 -> Medalha de bronze")
    elif t1 < t2:
        print("1 -> Medalha de prata")
        print("2 -> Medalha de bronze")

