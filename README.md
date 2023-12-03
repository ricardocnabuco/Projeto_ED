# Introdução do Projeto de Estrutura de Dados
Título do Projeto: Gerenciador de Voos Aéreos

Autores: Artur Almeida Maldaner, Ricardo de Carvalho Nabuco e Tauã Valentim de Albuquerque Martins Frade

## Contexto de Aplicação:

O algoritmo consciste em uma tabela que apresenta informações essenciais sobre voos aéreos em um aeroporto. Cada nó na lista inclui o horário do voo, número do voo, destino e número do portão de embarque. O algoritmo visa facilitar aos viajantes uma visualização clara e rápida dos voos disponíveis. Para a conveniência dos usuários, os voos são automaticamente ordenados de maneira crescente com base em seus horários, facilitando a identificação rápida dos próximos voos programados. Este sistema tem como objetivo simplificar a experiência dos viajantes ao fornecer uma visualização intuitiva e ordenada das informações de voos no aeroporto. 

## Estruturas de Dados Utilizadas:

Durante a implementação do algoritmo de gerenciamento, decidimos por aplicar a estrutura da lista encadeada em forma de fila. Neste contexto, designamos o "head" da lista como o primeiro voo exibido na tabela, enquanto o "tail" representa o último. Essa escolha permite a ordenação eficiente dos elementos com base em seus horários, garantindo que a tabela seja apresentada de maneira crescente. Essa estratégia de utilização da lista encadeada em forma de fila proporciona uma gestão eficaz e dinâmica dos voos, contribuindo para a eficiência e desempenho do algoritmo de gerenciamento da tabela de voos aéreos. Com o intuito de manter o algoritmo em ordem crescente, utilizamos a ordenação de insertion sort, após cada adição na tabela o algoritmo ajusta a posição do nó para manter a tabela ordenada. Além disso para possibilitar a busca de um voo específica na tabela, utilizamos a busca binária, que permite a recuperação eficiente dos voos desejados para o usuário.  
