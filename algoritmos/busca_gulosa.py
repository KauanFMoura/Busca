
class Gulosa:

    def __init__(self, graph, start, goal):
        """
        Função que implementa a busca gulosa
        :param graph: Grafo do mapa
        :param start: nó inicial
        :param goal: nó objetivo
        """
        self.graph = graph
        self.start = start
        self.goal = goal
        self.visited_nodes = set()
        self.path = []

    def search(self):
        """
        Algoritmo busca gulosa
        :return:
        """
        current_node = self.start # Nó atual

        # Enquanto a fila não estiver vazia
        for _ in range(len(self.graph.G.nodes)):

            # Se o nó atual já foi visitado, evita loops
            if current_node in self.visited_nodes:
                break

            self.visited_nodes.add(current_node) # Marca o nó atual como visitado
            self.path.append(current_node) # Adiciona o nó ao caminho

            # Se o nó atual é o objetivo, para a busca
            if current_node == self.goal:
                break

            less_cost = float('inf') # Custo inicial, inicia como infinito para sempre encontrar um custo menor

            # Verifica os vizinhos do nó atual, para encontrar o melhor proximo caminho
            for neighbor in self.graph.G.neighbors(current_node):
                # Se o vizinho não foi visitado
                if neighbor not in self.visited_nodes:
                    cost = self.graph.G.nodes[neighbor]['heuristic'] # Custo do vizinho

                    # Se o custo do vizinho é menor que o custo atual
                    if cost < less_cost:
                        less_cost = cost
                        current_node = neighbor # Atualiza o nó atual


