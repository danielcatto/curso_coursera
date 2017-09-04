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
        print("a raiz desta equa��o �",x)
    else:
        if (d < 0):
            print("esta equa��o n�o possui ra�zes reais")
        else:
            x = (-b + math.sqrt(d)) / (2 * a)
            y = (-b - math.sqrt(d)) / (2 * a)
            print("as ra�zes da equa��o s�o", x, "e", y)

main()

