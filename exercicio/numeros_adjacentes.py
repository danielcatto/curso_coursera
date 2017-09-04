#recebe um numero inteiro com um string
valor_str =input("digite um numero inteiro: ")
#verifica o tamanho do texto e armazena tamanho na variavel valor_len que ira ser a
#quantidade de voltas do laço - 1
valor_len = len(valor_str)
#inicializa as variaveis que irão ser usadas
valor_ant = -11990
i = 0
resp = False
valor_int = 0
parada = True
#cria o laço
while(i <= valor_len-1 and parada != False):
    #converte o caracter da posição [0] da string em um inteiro
    valor_atu = int(valor_str[i])
    if(valor_atu == valor_ant):
        valor_ant = valor_atu
        resp = True
        parada = True
    else:
        valor_ant = valor_atu
    i+=1

if(resp):
    print("sim")
else:
    print("não")

