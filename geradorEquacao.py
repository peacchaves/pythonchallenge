from random import choice
from random import randint
      

def fazEquacao():
    
    tamanhoLinha = randint(1, 1000)    # variável que recebe um número aleatório entre 1 e 1k p/ definir o num. de caract. de cada equação
    equacao = ''
    
    for i in range (tamanhoLinha):
        valores = choice(['a', 'b', 'c', '2', '3','(', ')', '+', '-', '*'])  # var. que receberá estes carac. aleatoriamente
        equacao += (valores)
              
    return equacao



with open ("equacoes.txt", "w", encoding="utf-8") as arquivo:
    
    qtasLinhas = randint(1, 10000)  # variável que recebe aleatoriamente um número entre 1 e 10k para definir quantidade de linhas
    
    for i in range(qtasLinhas-1):   # -1 do for feito pra ultima linha não ficar vazia devido ao + '\n'      
        arquivo.write(fazEquacao() + '\n')  
        
    arquivo.write(fazEquacao()) 