# 1º: Cria uma lista pra armazenar os resultados da variável 'candidato'.
resultados = []

# 2º: Cria um laço de repetição com as condições que vão receber os inputs.
while True:
    nome = input("Digite o nome do candidato: ")
    entrevista = input("Informe a nota da entrevista: ")
    teorico = input("Informe a nota do teste teórico: ")
    pratico = input("Informe a nota do teste prático: ")
    soft = input("Informe a nota da avaliação de soft skills: ")

# 3º: Criar uma variável que vai pegar todos os dados digitados nos inputs e juntar em uma coisa só. Cada item dentro da lista vai ser um vetor, começando do 0.
    candidato = (nome, entrevista, teorico, pratico, soft)
    resultados.append(candidato)

# 3º: Nessa parte basicamente vai ser gerada uma variável que vai funcionar como uma estrutura condicional, ou seja, foi
#     criada a variável 'continuar' que vai receber uma informação, e, a partir da informação recebida (nesse caso 's' ou 'n'), vai
#     gerar uma reação. No caso da variável criada, ela diz basicamente: caso a informação que o usuário digitar seja 'n', então pare
#     o laço de repetição, else, ou seja, se não, então 'Digite s/n'.
    continuar = input("Deseja adicionar outro candidato? (s/n): ")
    if continuar.lower() == 'n':
        break
    else:
        print('Digite s/n')

# 3º: Criar uma segunda lista para armazenar os resultados 'formatados', ou seja, os resultados que vão ser filtrados
#     de acordo com o que se pede na variável 'resultado_formatado' (repare que a lista e a variável têm quase o mesmo
# nome, mas são diferentes.
resultados_formatados = []

# 3º: Aqui foi criada basicamente uma estrutura condicional que vai pegar a variável 'candidato' (lá de cima) e vai dizer:
#     'Para candidatos na lista armazenada 'resultados', então: aí cria uma variável abaixo onde você vai colocar
#      a forma como vai ser o print na tela. Utiliza-se a variável candidato pois é nela que contém
#     o conjunto das notas dos candidatos, e é por isso que aqui embaixo está f"{candidato[0]}e{candidato[1]}_t{candidato[2]}_p{candidato[3]}_s{candidato[4]}"
#     esses números 0, 1, 2, 3 e 4 são os vetores que representam os itens dentros dessa variável, ou seja, 'nome', 'entrevista',
#     'teórico', 'prático' e 'soft'. esse f que está antes de tudo que dizer 'format', que vai determinar o formato que vai ser o print, no
#     exemplo abaixo, o 'format' vai garantir que o print fique como, por exemplo, "Candidato: robson e3_t3_p3_s3".
#     essa parte 'resultados_formatados.append(resultado_formatado)' pega a formatação gerada e inclui esse candidato lá na lista armazenada 'resultados_formatados'.
for candidato in resultados:
    resultado_formatado = f"{candidato[0]}e{candidato[1]}_t{candidato[2]}_p{candidato[3]}_s{candidato[4]}"
    resultados_formatados.append(resultado_formatado)


resultados_formatados = []

# 3º: Aqui foi criada basicamente uma estrutura condicional que vai pegar a variável 'candidato' (lá de cima) e vai dizer:
#     Para o candidato X que está na lista armazenada resultado:
#     Se 1 for menor ou igual ao SEGUNDO vetor da variável candidato, ou seja 'entrevista' (descrito como [1]) eessa mesma variável for menor ou igual a 5, e assim
#     para os outros filtros que deseja colocar. OU SEJA, simplificando: existem dois valores, nesse caso, igual ou maior que 1 e igual ou menor que 5, ou seja, entre 1 e 5,
#     então se o vetor [1] for dentros do intervalo entre 1 e 5, então 'resultados_formatados.append(resultado_formatado)' que siginifica: pega a formatação gerada e inclui esse candidato
#     lá na lista armazenada 'resultados_formatados'.

for candidato in resultados:
    if 1 <= int(candidato[1]) <= 5 and 1 <= int(candidato[2]) <= 5 and 1 <= int(candidato[3]) <= 7 and 1 <= int(candidato[4]) <= 5:
        resultado_formatado = f"Candidato(a): {candidato[0]} e{candidato[1]}_t{candidato[2]}_p{candidato[3]}_s{candidato[4]}"
        resultados_formatados.append(resultado_formatado)

# 3º: No fim, vai ser impressa a LISTA 'resultados_formatados', que vai puxar os resultados de acordo com o filtro que foi colocado, porém,
#     já formatados da forma como é pedido para que apareça, sendo "Candidato: robson e3_t3_p3_s3", pois já foi formatada lá na primeira parte
#     'for candidato in resultados:'
print(resultados_formatados)


