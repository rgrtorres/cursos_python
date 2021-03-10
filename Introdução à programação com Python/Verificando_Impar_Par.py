while True:
    numero = int(input("Insira um número:"))

    for x in range(0, numero+1):
        if x % 2 == 0:
            print("{} é par".format(x))
        else:
            print("{} é impar".format(x))

    print("Loop finzalizado!")