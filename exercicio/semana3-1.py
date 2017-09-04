import math
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))


delta = b ** 2 - 4 * a * c
x =  (-b + delta) / (2 * a)
y = (-b - delta) / (2 * a)

if(delta < 0):
    print("negativo reprovado")
    print ("valor real para x = ",x, "e x = ",x)
else:
    print ("valor real para x = ",y, "e x = ",y)






