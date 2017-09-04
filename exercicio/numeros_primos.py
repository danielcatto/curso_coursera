valor = int(input("Digite um numero inteiro"))
contar_divisao_inteira = 1
resto = 0
mesmo = 0
i=1
sim = False
while(i <= valor and sim != True):
    resto += valor % i
    if(resto == 0):
        contar_divisao_inteira += 1
    i+=1
if(contar_divisao_inteira >2):
    print("não primo")
else:
    print("primo")
