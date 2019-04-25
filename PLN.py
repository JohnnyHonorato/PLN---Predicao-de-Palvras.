import re
from collections import Counter

regex = "[a-zA-ZçÇãÃõÕáÁéÉíÍóÓúÚâÂêÊîÎôÔûÛàÀ]+"

data = open("shakespeare.txt").read()

tokens = re.findall(regex, data)
tokens_count = Counter(tokens)

def p_bigram(w1, w2):
    count_w1 = tokens_count[w1]
    count_w1w2 = 0
    for i in range(len(tokens)):
        if tokens[i] == w1 and tokens[i+1] == w2:
            count_w1w2 += 1
    return count_w1w2/count_w1 

def p_trigram(w1, w2, w3):
    count_w1 = tokens_count[w1]
    count_w1w2w3 = 0
    count_w1w2 = 0
    for i in range(len(tokens)):
        if tokens[i] == w1 and tokens[i+1] == w2:
            count_w1w2 += 1
    for i in range(len(tokens)):
        if tokens[i] == w1 and tokens[i+1] == w2 and tokens[i+2] == w3:
            count_w1w2w3 += 1
    if(count_w1w2 == 0):
        return 0
    return count_w1w2w3/count_w1w2

def retonarProbabilidadesComUmaPalavra(w1):
    lista = []
    lista2 = []
    for i in tokens:
        lista.append(i)
        lista2.append(p_bigram(w1, i))
    data = dict(zip(lista, lista2))
    return data

def retonarListaComTresMaioresProbabilidade(data):
    lista = []
    for item in sorted(data, key = data.get):
        lista.append(item)
    lista.reverse()
    return lista

def retonarProbabilidadesComDuasPalavra(w1, w2):
    lista = []
    lista2 = []
    for i in tokens:
        lista.append(i)
        lista2.append(p_trigram(w1, w2, i))
    data = dict(zip(lista, lista2))
    return data

print ("1- BIGRAMA \n2- TRIGRAMA")
num = int(input())
if(num == 1):
    palavra = input("Digite uma palavra: ")
    data = retonarProbabilidadesComUmaPalavra(palavra)
    lista = retonarListaComTresMaioresProbabilidade(data)
    print("Maior probabilidade:", lista[0])
    print("Segunda maior probabilidade:", lista[1])
    print("Terceira maior probabilidade:", lista[2])
if(num == 2):
    palavra = input("Digite duas palavra: ")
    lista = palavra.split(' ')
    data = retonarProbabilidadesComDuasPalavra(lista[0], lista[1])
    lista = retonarListaComTresMaioresProbabilidade(data)
    print("Maior probabilidade:", lista[0])
    print("Segunda maior probabilidade:", lista[1])
    print("Terceira maior probabilidade:", lista[2])