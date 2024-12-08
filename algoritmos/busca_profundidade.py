import networkx as nx

class Profundidade:

    def __init__(self, graph, start, goal):
        """
        Classe que implementa o algoritmo de busca em profundidade
        :param graph: Grafo do mapa
        :param start: nó inicial
        :param goal: nó objetivo
        """
        self.graph = graph
        self.start = start
        self.path = []
        self.stack = [self.start]
        self.visited = set()
        self.goal = goal
        self.pai = {self.start: (0, 0)}


    def search(self):
        """
        Busca em profundidade
        :return:
        """

        # Enquanto a pilha não estiver vazia
        while self.stack:
            node = self.stack.pop() # Pega o último nó da pilha

            # Se o nó for o objetivo, para a busca
            if node == self.goal:
                break

            # Se o nó não foi visitado
            if node not in self.visited:
                self.visited.add(node) # Marca o nó como visitado
                self.path.append(node) # Adiciona o nó ao caminho

                # Para cada vizinho do nó
                for neighbor in self.graph.neighbors(node):
                    if neighbor not in self.pai: # Se o vizinho não tem pai
                        self.pai[neighbor] = (node, 0) # Adiciona o pai do vizinho

                    if neighbor not in self.visited: # Se o vizinho não foi visitado
                        self.stack.append(neighbor) # Adiciona o vizinho à pilha

    def best_path(self):
        """
        Extrai o melhor caminho
        :return: melhor caminho
        """
        path_best = [] # Caminho final
        no_atual = self.goal # Nó atual é o objetivo

        # Reconstrua o caminho a partir do objetivo, seguindo os pais
        while no_atual != self.start:
            path_best.append(no_atual) # Adiciona o nó atual ao caminho
            no_atual = self.pai[no_atual][0]  # Pega o pai do nó atual

        path_best.append(self.start) # Adiciona o nó inicial ao caminho
        path_best.reverse() # Inverte o caminho

        return path_best
