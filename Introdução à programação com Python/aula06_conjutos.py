# conjunto = {1,2,3,4}
# conjunto.add(7)
# conjunto.discard(2)
# print(conjunto)

conjunto = {1,2,3,4,5}
conjunto2 = {5,7,9,10}
conjunto_uniao = conjunto.union(conjunto2)
print("União: {}".format(conjunto_uniao))

conjunto_intercepcao = conjunto.intersection(conjunto2)
print("Conjunto Intercepção: {}".format(conjunto_intercepcao))

conjunto_diferenca = conjunto.difference(conjunto2)
print("Conjunto diferença: {}".format(conjunto_diferenca))

conjunto_diferenca2 = conjunto2.difference(conjunto)
print("Conjunto diferença2: {}".format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print("Conjunto Diferença Simetrica: {}".format(conjunto_diff_simetrica))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

conjuntoo = {10, 20, 30, 40, 50}
conjuntoo.discard(40)
print(conjuntoo)