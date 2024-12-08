# Trabalho de Implementação de Algoritmos de Busca

## Escopo

O trabalho consiste em implementar um sistema de navegação automática de um agente utilizando os algoritmos de busca em largura, profundidade, gulosa e A*. O agente deve ser capaz de calcular automaticamente a melhor rota para chegar a qualquer ponto de um ambiente representado através de um grafo que conecta seus vértices a áreas, locais ou partes do caminho onde o agente pode navegar.

O grafo representa um cenário fictício que você deve criar, onde o agente irá tentar encontrar um prêmio (estado objetivo) que se encontra em algum local diferente de onde o agente inicia no ambiente (nó inicial). O grafo deve ter pelo menos 30 vértices. 

Além do prêmio final, durante o percurso, o agente também deve coletar recompensas que estão espalhadas no mapa. Os algoritmos de busca cega devem pegar as recompensas que aparecerem nos vértices visitados durante a verificação do caminho que leva ao prêmio final. Já os algoritmos com heurística devem ter em sua heurística uma forma de avaliar se é compensador deslocar-se da rota que leva para o prêmio final para pegar recompensas que estejam em vértices próximos durante esse caminho.

### Tipos de Terrenos e Custos

O ambiente por onde o agente irá navegar é formado por diversos tipos de terrenos, e em cada tipo de terreno o agente tem um grau de dificuldade diferente para andar. A seguir estão os tipos de terrenos que compõem o ambiente:

- **Sólido e plano** – Custo: +1
- **Rochoso** – Custo: +10
- **Arenoso** – Custo: +4
- **Pântano** – Custo: +20

A melhor rota para chegar a um determinado ponto do ambiente é a rota que tem o menor custo.

## Requisitos do Trabalho

- As figuras de exemplo mostram ideias para o mapa do ambiente que deve ser desenvolvido. Os seguintes símbolos devem ser utilizados:
  - **▓**: Paredes (onde o agente não pode passar)
  - **Espaços em branco de diferentes cores**: Locais onde o agente pode andar (cada cor representa um tipo de terreno)
  - **☺**: Agente
  - **$**: Recompensas

  É permitido utilizar outros símbolos de sua preferência para representar os elementos. A quantidade de recompensas no ambiente deve ser de no mínimo 5.

- Após calcular a melhor rota, o programa deve mostrar a movimentação do agente seguindo a rota calculada.
- O agente, durante sua rota, deve tentar pegar o máximo de recompensas possíveis.
- O algoritmo deve ser capaz de perceber quando não existe nenhum caminho para chegar ao destino ou se existem paredes, becos ou pontos sem saída (exemplo: uma sala sem entradas ou uma parede que impede o caminho de continuar).
  
- Além de encontrar a melhor rota, é necessário realizar um comparativo entre os resultados dos algoritmos em relação a:
  - Tempo de execução
  - Quantidade de nós expandidos na memória

## Considerações Iniciais

A melhor maneira de começar o trabalho é pensando na função heurística que será utilizada pelos algoritmos Guloso e A*. Os algoritmos devem ser implementados de forma correta e o código organizado.

## Conclusão

Este trabalho visa implementar a navegação de um agente através de um ambiente com diferentes tipos de terrenos, utilizando os algoritmos de busca para calcular a melhor rota. A implementação deve ser eficiente, com comparações entre os algoritmos baseadas em tempo de execução e no número de nós expandidos.
