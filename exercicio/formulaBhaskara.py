# -*- coding: latin-1 -*-
import math
def delta(a, b, c):
    return b ** 2 - 4 * a * c

def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    d = delta(a, b,c)
    if(d== 0):
        x = (-b + math.sqrt(d)) / (2  * a)
        print("a raiz desta equação é",x)
    else:
        if (d < 0):
            print("esta equação não possui raízes reais")
        else:
            x = (-b + math.sqrt(d)) / (2 * a)
            y = (-b - math.sqrt(d)) / (2 * a)
            print("as raízes da equação são", x, "e", y)

main()

