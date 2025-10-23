def soma(nd):
    cont=0
    for c in range(0,nd):
        n=int(input (f"digite o {c+1}º número: "))
        cont+=n
    return cont

nd = int (input("digite a quantidade de números que quer somar: "))
n=soma(nd)
print(f"a soma dos seus números é: {n}")
