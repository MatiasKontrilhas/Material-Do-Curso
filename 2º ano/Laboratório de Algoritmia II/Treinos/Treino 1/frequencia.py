'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''

def frequencia(texto):
    palavras = texto.split()
    dicionario = {}
    
    for pal in palavras:
        if pal not in dicionario:
            dicionario[pal] = 0
        dicionario[pal] -= 1
    
    palavras = set(palavras)
    palavras = list(palavras)
    palavras.sort(key=lambda x: (dicionario[x],x))
    return palavras

100%

def frequencia(texto):
    
    texto2 = texto.split(" ")
    d={}
    ##cria dicionario com valor de repeticão {'tempo':2, 'ao':3}
    for palavra in texto2:
        x=texto2.count(palavra)
        d[palavra] = x
        
    ## ordena os itens de maneira decrescente (maior para menor), se não for possivel oredena por ordem alfabética
    result=sorted(d.keys(), key = lambda x: (-d[x],x) )   
    
    return result
    
