# Introdução do Projeto de Estrutura de Dados
Título do Projeto: Gerenciador de Voos Aéreos

Autores: Artur Almeida Maldaner, Ricardo de Carvalho Nabuco e Tauã Valentim de Albuquerque Martins Frade

## Contexto de Aplicação:

O algoritmo consiste em uma tabela que apresenta informações essenciais sobre voos aéreos em um aeroporto. Cada nó na lista inclui o horário do voo, número do voo, destino e número do portão de embarque. O algoritmo visa implementar uma aplicação extremamente comum com o uso de conhecimentos sobre estruturas de dados e eficiência de algoritmos para construção da melhor aplicação . Para a conveniência dos usuários, os voos são automaticamente ordenados de maneira crescente com base em seus horários, facilitando a identificação rápida dos próximos voos programados. Este sistema tem como objetivo simplificar a experiência dos viajantes ao fornecer uma visualização intuitiva e ordenada das informações de voos no aeroporto. 

## Estruturas de Dados Utilizadas:

Durante a implementação do algoritmo de gerenciamento, decidimos por aplicar a estrutura da lista encadeada em forma de fila. Neste contexto, designamos o "head" da lista como o primeiro voo exibido na tabela, enquanto o "tail" representa o último. Essa escolha permite a ordenação eficiente dos elementos com base em seus horários, garantindo que a tabela seja apresentada de maneira crescente. Essa estratégia de utilização da lista encadeada em forma de fila proporciona uma gestão eficaz e dinâmica dos voos, contribuindo para a eficiência e desempenho do algoritmo de gerenciamento da tabela de voos aéreos. Com o intuito de manter o algoritmo em ordem crescente, utilizamos a ordenação de insertion sort, por esse algoritmo de ordenação ser especialmente bom para listas parcialmente ordenadas, que é o caso, após cada adição na tabela o algoritmo ajusta a posição do nó movendo as informações dele, para manter a tabela ordenada. Além disso para possibilitar a busca de um voo específica na tabela, utilizamos a busca binária, que permite a recuperação eficiente dos voos desejados para o usuário.  

## Pré-Requisitos para Execução:
- Ter o Python 3.0 instalado no computador operante
- Ter um interpretador python instalado ( Thonny, VsCode, etc)

## Instruções para Execução:
Execute o código do conteúdo do github através de: 
- Um interpretador próprio de preferência copiando o código.
- Execute através do vscode usando o codespace específico usando diretamente pelo código.

## Instruções de Uso:

Ao executar o programa pela primeira vez, perceberá que algumas opções são exibidas na interface: adicionar um voo, remover um voo, buscar um voo, emitir uma tabela de voos, editar status de voo e sair do progrma, que responderá ao input fornecido pelo usuário.

![image](https://github.com/ricardocnabuco/Projeto_ED/assets/33905219/528e423e-29fb-435d-baf4-fec3f1c678be)


### 1 . Adicionar voo
Caso o usuário escolher a primeira opção, de adicionar um voo, a interface vai mostrar duas opções, a de adicionar um voo na tabela de chegadas e de adicionar um voo na tabela de partida. O horario previsto de chegada ou partida do voo deve ser informado no formato hh:mm.

![image](https://github.com/ricardocnabuco/Projeto_ED/assets/33905219/8b88382b-f212-4dd2-b35f-9d6c2f4ad2a9)

#### Adicionar na tabela de chegada
Ao escolher a primeira das opções, de adicionar o voo na tabela de chegada, o algoritmo vai perguntar as informações do voo em questão, o horário previsto de chegada, o código do voo , o portão e a origem, e então vai adicionar o voo na tabela de chegadas.

![image](https://github.com/ricardocnabuco/Projeto_ED/assets/33905219/8a81f7ce-03fd-435b-ae26-4d094ddaf321)

#### Adicionar na tabela de partidas
Da mesma forma, ao escolher a segunda opção, o algoritmo vai perguntar informações similares, o horário previsto da saída, o código do voo, o portão e o destino, e tal como da última vez o programa vai adicionar o voo na tabela de partidas.

![image](https://github.com/ricardocnabuco/Projeto_ED/assets/33905219/3ed1b64b-7de6-4041-b4a8-4d8002345104)

### 2 . Remover voo
Quando o usuário escolher a opção de remover um voo, da mesma forma da funcão de adicionar na tabela, o programa vai perguntar de qual das duas tabelas o usuário quer remover um voo, da tabela de chegadas ou da de partidas.

![image](https://github.com/ricardocnabuco/Projeto_ED/assets/33905219/87bb6e76-a999-407a-a8fe-ece11b66ed4a)

Para os dois casos de remoção, o programa vai remover o voo que está na cabeça da lista correspondente escolhida, devido ao caráter de fila da estrutura usada no programa, com o intuito de simular uma tabela tradicional utilizada em aeroportos. Por exemplo, se a tabela a seguinte for real:

![image](https://github.com/ricardocnabuco/Projeto_ED/assets/33905219/8333fc0a-d40d-4fa0-8ae9-40a10509c5ac)

O programa vai remover sempre o voo que está no topo dela:

![image](https://github.com/ricardocnabuco/Projeto_ED/assets/33905219/238e0028-27b6-4840-8d6e-15827a0f2775)

E então a tabela terminará sem o seu voo do topo:

![image](https://github.com/ricardocnabuco/Projeto_ED/assets/33905219/9762ca8f-7d59-4034-81ea-1e4226e7bedd)

### 3 . Buscar voo

Após escolher a opção de buscar voos, primeiramente o programa vai solicitar de qual das duas listas o usuário deseja buscar um voo. E depois de escolher uma das duas opções, o algoritmo vai solicitar o código e o horário do voo.

![image](https://github.com/ricardocnabuco/Projeto_ED/assets/33905219/24dcf6e1-7fdd-4d72-b797-5db49ce1cacf)

Caso o código e o horário forneciido corresponda com algum voo que está regristado na tabela escolhida, o programa vai imprimir todas as informações do voo em questão.

![image](https://github.com/ricardocnabuco/Projeto_ED/assets/33905219/f95d1504-edd1-43b3-9b50-022a1fe48380)

### 4 . Emitir tabela de voos

Na função de emição da tabela, o programa vai solicitar qual das tabelas que o usuário quer acessar, e a tabela escolhida vai ser impressa.

![image](https://github.com/ricardocnabuco/Projeto_ED/assets/33905219/43d92d96-624b-4a2c-8bdc-7fb00b8d1671)

### 5 . Editar status de voo

Para mudar o status de voo, o programa vai novamente solicitar qual das tabelas o voo em questão está armazenado, e depois o código e número do voo a ser alterado, com o intuito de ser identificado.

![image](https://github.com/ricardocnabuco/Projeto_ED/assets/33905219/3642de8b-c3fe-4e6b-8fd2-0f03dec641d4)

E então, depois de localizar o voo, o programa vai perguntar para qual status você quer que o voo seja removido.

![image](https://github.com/ricardocnabuco/Projeto_ED/assets/33905219/c3ac870d-a941-4cbd-8d64-d24ef2f3e6b1)

No fim o resultado será alterado na tabela correspondente, como ilustrado a seguir:

![image](https://github.com/ricardocnabuco/Projeto_ED/assets/33905219/fb2a9e28-4fe2-4c2b-b14e-fb730e234319)

## Referências Bibliográfica

- GitHub da máteria de Estrutura de Dados.
- Narasimha Karumanchi, Data Structure and Algorithmic Thinking with python.



