def check_brackets(string):
    stack = []

    # Testando cada caractere da string
    # Caracteres diferentes de '(' e ')' são ignorados
    for char in string:
        match char:
            case '(':
                stack.append(char)
            case ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False

    # Pilha vazia -> Correto (True)
    # Pilha não vazia -> Incorreto (False)
    return len(stack) == 0


if __name__ == '__main__':
    output = []
    n = int(input())

    #Testando cada linha de entrada
    for i in range(n):
        str = input()

        if check_brackets(str):
            output.append("correct")
        else:
            output.append("incorrect")

    #Imprimindo os resultados de cada linha
    for result in output:
        print(result)
