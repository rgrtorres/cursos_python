numero = int(input("Digite um número: "))
div = 0
for x in range(1, numero+1):
    restoDivisao = numero % x;
    print(x, restoDivisao)

    if restoDivisao == 0:
        div = div + 1
    
if div == 2:
    print("O número {} é primo.".format(numero))
else:
    print("O número {} não é primo".format(numero))