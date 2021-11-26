# pythonchallenge

 Nesta pasta contém três arquivos(sem contar este), que vou explicar por etapas,
começando pelo "desafio.py".


	-> Função verificar

 De forma resumida, usei o método "pilha", toda vez que um "(" é identificado,
ele é enviado para ela. 

No momento que um ")" é encontrado, temos dois cenários:

 1- Um "(" já foi encontrado anteriormente, então este mesmo "(" será removido da pilha e nada séra adicionado.

 2- A pilha está vazia, e não podemos começar um parêntese fechando-o, logo, a função retorna "incorrect" imediatamente.

 Ao final da função, quando executada, se a pilha estiver vazia, significa que está tudo certo e teremos "correct"
como retorno, caso contrário(se houver algum caractere na pilha) o retorno será "incorrect".


	-> Entradas

 Neste código, há duas entradas diferentes, sendo elas:
 
 1- Entrada manual, qual você pode digitar a função que deseja verificar manualmente
(Será necessário descomentá-la e comentar toda a entrada número 2).

 2- Entrada "automática", qual lê cada linha de um arquivo .txt que pode ser gerado no *código complementar*
(Esta já se encontra configurada e pronta para uso).


	-> Código complementar

 O arquivo denominado "geradorEquacao.py" foi criado com a intenção de testar o código principal,
é um gerador bem simples de equações, que não serão perfeitas, mas suficientes para o teste.

 Primeiramente ele dispõe de uma função que faz uso da biblioteca random, que o permite definir de forma
aleatória o tamanho da linha de cada equação de forma aleatória (inicialmente configurado para definir
de 1 a 1000 caracteres).

 Após ter gerado a equação, ele fará mais uma vez uso da lib random para definir o número de equações
(uma em cada linha e inicialmente configurado para entre 1 e 10000 linhas). 

 Finalizando, o código ao ser executado "vai digitar" todas as equações definidas de forma aleatória no arquivo
com o nome "equacoes.txt" (caso o arquivo já exista, substituirá seu conteúdo, se não, criará um novo).



 Muito obrigado pela atenção, espero que a explicação tenha sido útil e que você tenha gostado do meu trabalho.
