class Largura:

    def __init__(self, graph, start, goal):
        """
        Classe que implementa a busca em largura
        :param graph: grafo do mapa
        :param start: nó inicial
        :param goal: nó objetivo
        """
        self.graph = graph
        self.start = start
        self.path = []
        self.queue = [self.start]
        self.visited = set()
        self.goal = goal
        self.pai = {self.start: (0, 0)}

    def search(self):
        """
        Algoritmo Busca em largura
        :return:
        """

        # Enquanto a fila não estiver vazia, Executa em Todos os nós
        while self.queue:
            # Pega o primeiro nó da fila
            node = self.queue.pop(0)

            # Se o nó não foi visitado
            if node not in self.visited:
                self.visited.add(node)  # Marca o nó como visitado
                self.path.append(node)  # Adiciona o nó ao caminho

                # Verifica se os vizinhos do nó
                for neighbor in self.graph.neighbors(node):

                    if neighbor not in self.pai:  # Se o vizinho não tem pai
                        self.pai[neighbor] = (node, 0)  # Armazena o pai e o custo

                    if neighbor not in self.visited:  # Se o vizinho não foi visitado
                        self.queue.append(neighbor)  # Adiciona o vizinho a fila

    def best_path(self):
        """
        Extrai o melhor caminho
        :return: melhor caminho
        """
        path_best = []  # Caminho final
        no_atual = self.goal  # Nó atual é o objetivo

        # Reconstrua o caminho a partir do objetivo, seguindo os pais
        while no_atual != self.start:
            path_best.append(no_atual)  # Adiciona o nó atual ao caminho
            no_atual = self.pai[no_atual][0]  # Pega o pai do nó atual

        path_best.append(self.start)  # Adiciona o nó inicial ao caminho
        path_best.reverse()  # Inverte o caminho

        return path_best
