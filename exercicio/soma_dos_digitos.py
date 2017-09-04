#recebe um numero inteiro com um string
valor_str =input("digite um numero inteiro: ")
#verifica o tamanho do texto e armazena tamanho na variavel valor_len que ira ser a
#quantidade de voltas do laço - 1
valor_len = len(valor_str)
#inicializa as variaveis que irão ser usadas
valor_total = 0
i = 0
valor_int = 0
#cria o laço
while(i <= valor_len-1):
    #converte o caracter da posição [0] da string em um inteiro
    valor_int = int(valor_str[i])
    #faz-se a soma e quarda na varialvel valor_total
    valor_total = valor_total + valor_int
    #soma um na variazel de controle do laço
    i+=1
#depois de sair do laço printa o resultado na tela
print(valor_total)
