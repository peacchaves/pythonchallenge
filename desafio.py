def verificar(expressao): 
    pilha = [] 

    for caractere in expressao: 
        if caractere == '(': 
            pilha.append(caractere)   # se um "(" é identificado, será adicionado a pilha

        elif caractere == ')': 

            if ((len(pilha) > 0)):   # se um "(" já tiver sido identificado anteriormente, será removido
                pilha.pop() 

            else: 
                return "incorrect"  # se a pilha está vazia e um ")" foi identificado, a equação está "incorreta"

    if len(pilha) == 0:
        return "correct"   # pilha vazia = tudo certo

    else:
        return "incorrect"  # pilha com caractere = incorreto
  
  
# entrada = "2(ax)"         # -> Entrada manual
# print(verificar(entrada))  

with open ("equacoes.txt", "r", encoding="utf-8") as arquivo:  # Entrada "automática"  
    equacoes = reaarquivo.dlines()                 
    
    for linha in equacoes:
        print(verificar(linha))