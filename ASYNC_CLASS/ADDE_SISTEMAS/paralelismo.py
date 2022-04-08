"""
PARALELISMO

Imagine que voce quer fazer um jantar para 10 amigos.
passos:

- lavar os vegetais - 5 minutos de tempo de execução
- cortar os vegetais - 13 minutos de tempo de execução
- cozinhar os vegetais - 30 minutos de tempo de execução
- servir o jantar - 2 minutos de tempo de execução

Vendo esse processo podemos pensar em alguma forma de otimização de processos.

Imagina que voce queira reduzir o cozimento para 250 minutos.

Se alguem começar a te ajudar, logo, a execução em paralelo irá reduzir o tempo de execução.

Mas temos que ver que nesse caso, cada pessoa cozinha em sua propria cozinha, e não disputa um espaço.

Ou seja, o paralelismo acontece quando o computador tem varios "cores". E existem processos rodando em ao menos dois deles.

O PARALELISMO acontece atraves de execução de diferentes processos.

----------------------------------------------------------------------

CONCORRENCIA / SIMULTANEIDADE / CONCURRENCY

Podemos ver que o maior gargalo acontece quando vamos cozinhar.

Pergunta: quantos pratos posso cozinhar por vez no forno. Se pudessemos cozinhar os 10 pratos de uma vez, vamos economizar 270 minutos.

Nesse caso, não vamos usar recurso algum de outra cozinha, simplesmente aproveitamos da capacidade de um recurso ocioso.

A concorrencia acontece dentro de um mesmo processo, aproveitando a ociosidade de um recurso.

Poderiamos aplicar a concorrencia as outras etapas.

Concorrencia acontece dentro de uma thread, que esta sendo executada dentro de um processo. Um processo pode ter varias threads. E essas
threads podem compartilhar recursos entre elas, por exemplo o forno.

----------------------------------------------------------------------

QUANDO USAR UM OU OUTRO?

Se a app Python esta executando operações vinculadas a CPU, como processamento de numeros ou manipulação de texto, opte pelo paralelismo.
A simultaneidade nao trará muitos beneficios nesses cenários.

"""