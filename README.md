## Apresentação

Para este trabalho, foi criado uma aplicação que permite ao usuário gerar senhas mais seguras, pois o mesmo gera uma lista de caracteres, incluindo letras maiusculas, minúsculas e caracteres especiais Com essa lista, é feito um sorteio de uma quantidade de caracteres de acordo com o número selecionado pelo usuário. 



## Divisão da equipe

| Membros | Responsabilidade |
| --- | --- |
| Breno Oliveira, Pedro Rocha | Desenvolvimento |
| Dayane Silva, Admilson Neto | Levantamento dos requisitos e documentação |
| Admilson Neto | Casos de teste |


## Requisitos Funcionais

| Requisitos | Código |
| --- | --- |
| A aplicação deve gerar números inteiros aleatórios  | Por meio da função '''getRandomNumbers''' conseguimos gerar uma lista de números aleatórios ao usar List Comprehension |
| A aplicação deve gerar uma senha tendo como base uma lista de caracteres | Por meio da função '''getPassword''' conseguimos pegar uma lista de caracteres e usar os números aleatórios gerados na função anterior para formar uma senha. Para isso, essa função se utiliza de Cloure do python para ter uma função interna a ela. |
| A aplicação deve permitir que o usuário insira uma quantidade de caracteres | Por meio do input de informações do python conseguimos fazer isso na linha 35 ao solicitar essa informação e na linha 36 onde pegamos a informação digitada pelo usuário. |
| A aplicação deve destacar a senha gerada | Por meio da função '''markPassword''' que recebe a senha e destaca ela por meio de marcações do python, colando o texto em negrito, sublinhado e com a cor verde. |

## Requisitos Não Funcionais

| Requisitos | Código |
| --- | --- |
| A aplicação deve permitir concatenar strings | Por meio de uma lambda na linha 9 conseguimos concatenar string. |
| A aplicação deve ter uma função de alta ordem para unir elementos de um array | Por meio da função joinList que recebe uma função e faz um join das strings dessa segunda função.  |
| A aplicação deve ser de fácil compilação | Temos um Main na linha 39 que com o simples clique permite executar toda a aplicação. |
